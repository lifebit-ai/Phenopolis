#!/usr/bin/python

import os
import sys
import argparse
import tempfile
import subprocess
import multiprocessing
import datetime
from subprocess import PIPE

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Simple BWA wrapper")
    parser.add_argument("-i", "--reads", dest='reads', action='append', help="Reads FASTA or FASTQ file to be aligned (either one file or read1/read2)", required = True)
    parser.add_argument("-r", "--reference", dest='reference', action="store", choices=["hs37d5", "GRCh38", "hg19"], help="Human genome reference", required = True)
    parser.add_argument("-o", "--outfile", dest='outfile', help="Output file or destination", required = True)
    args = parser.parse_args()
    # currently set default output path to docker container folder 
    if not (args.reads and args.reference and args.outfile):
        parser.print_help()
        parser.exit()
    vargs = vars(parser.parse_args())
    nCpus = multiprocessing.cpu_count()
    # start measuring time
    start = datetime.datetime.now()
    print("running BWA mem")
    # Align reads > sorted bam > save
    if len(vargs['reads']) == 1:
        reads = vargs['reads'][0]
        subprocess.call(f"./bwa mem -t {nCpus} {args.reference}.fa {reads} | \
                         samtools view -bS - | \
                         samtools sort -O BAM -o - - | \
                         samtools index - {args.outfile}", shell=True, stdout=PIPE, executable="/bin/bash")
    elif len(vargs['reads']) == 2:
        read1 = vargs['reads'][0]
        read2 = vargs['reads'][1]

        subprocess.call(f"./bwa mem -t {nCpus} {args.reference}.fa {read1} {read2}| \
                         samtools view -bS - | \
                         samtools sort -O BAM -o - - | \
                         samtools index - {args.outfile}", shell=True, stdout=PIPE, executable="/bin/bash")
    else:
        sys.exit("--reads should be specified either once or twice")             

    elapsed = datetime.datetime.now() - start

    with open(args.outfile + ".log", "w") as logfile:
        logfile.write(f"The BWA execution took {elapsed}.\n")            
