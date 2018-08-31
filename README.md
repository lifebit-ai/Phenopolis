# Phenopolis 

## BWA 
This docker container contains:
* BWA mem binary
* pre-indexed genome reference for hg19
* samtools to derive bam file from bwa sam output 
The input could be two paired-end fastq files or a merged one, python wrapper automatically adapts to the input.
The number of threads is one by default for bwa, but set to the number of cpus by the wrapper.
Runtime on c5.2xlarge instance from fastq to bam is 4.3h, on-demand cost 1.65 USD.

## Cellbase 
Thie docker container CellBase.
Runtime on c5.2xlarge instance from fastq to bam is 0.3h, 0.1 USD.
