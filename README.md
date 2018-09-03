# Phenopolis 

## Example dataset 
Example dataset includes s3://phenopolis/testdata bucket that contains different files for NA12878 exome sequenced sample:
* fastq files downloaded from ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase3/data/NA12878 
* aligned bam file (bwa mem)
* VCF files with deep variant calls 
* JSON annotation files of deep variant calls 
* exome target manifest file downloaded from  https://dl.dnanex.us/F/D/y61fXf4qz5G8F4QvXz14bkYQ5Q9Yy5q5JPf1K3kg/agilent_sureselect_human_all_exon_v5_b37_targets.bed

This dataset could be found and attached to Datasets 
![parameters](https://github.com/lifebit-ai/Phenopolis/blob/master/phenopolis.png "")


## BWA 
This docker container contains:
* BWA mem binary
* pre-indexed genome reference for hg19
* samtools to derive bam file from bwa sam output 
The input could be two paired-end fastq files or a merged one, python wrapper automatically adapts to the input.
The number of threads is one by default for bwa, but set to the number of cpus by the wrapper. Deploit allows us to complete these operations through graphical UI and we will be using in this document. 

First, we set parameters of the container. We specify paired-end reads through two inputs (separately for first and second read) and reference file.
![parameters](https://github.com/lifebit-ai/Phenopolis/blob/master/bwa1.png "")

Next we select job execution 
 
![parameters](https://github.com/lifebit-ai/Phenopolis/blob/master/bwa2.png "")

Runtime on c5.2xlarge instance from fastq to bam is 4.3h, on-demand cost 1.65 USD.


## DeepVariant 
DeepVariant represents nextflow workflow rather than docker as it is composed of several separate steps. Notwithstanding different implementations, the interface to deep variant is usefully the same as in case of docker containers. 


Since we are using exome input following best practices, we specify the following arguments in the first input form (as in the screenshot)
* bam_folder = analysis will run on all samples in the folder
* exome = flag to specify that exome training model is used 
* bed = an accompanying path to file with bed regions, the calls will be mode only in those regions limiting effect of off-target enrichemnt
* hg19 (genome reference flag) 
* output sample name 

![parameters](https://github.com/lifebit-ai/Phenopolis/blob/master/DV1.png "")

Next we select job execution 
 
![parameters](https://github.com/lifebit-ai/Phenopolis/blob/master/DV2.png "")
Runtime on c5.2xlarge instance from fastq to bam is 0.3h, 0.1 USD.


## Cellbase 
Thie docker container includes CellBase  variant annotation engine. 
To run in the platform first set the parameters of the container:
* i = input vcf 
* s = genome reference 
* o = output 

![parameters](https://github.com/lifebit-ai/Phenopolis/blob/master/cellbase1.png "")

Next select job execution 
 
![parameters](https://github.com/lifebit-ai/Phenopolis/blob/master/cellbase2.png "")
Runtime on c5.2xlarge instance from fastq to bam is 0.3h, 0.1 USD.
