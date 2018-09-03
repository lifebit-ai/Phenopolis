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
The number of threads is one by default for bwa, but set to the number of cpus by the wrapper.
Set parameters of container

![parameters](https://github.com/lifebit-ai/Phenopolis/blob/master/bwa1.png "")

Next select job execution 
 
![parameters](https://github.com/lifebit-ai/Phenopolis/blob/master/bwa2.png "")
Runtime on c5.2xlarge instance from fastq to bam is 0.3h, 0.1 USD.

An example of docker command: docker run -v /localdata/:/data lifebitai/cellbase:4.5.6-v3  -i /data/NA12878.exome.vcf -s 'hsapiens' -o /data/NA12878.exome 

Runtime on c5.2xlarge instance from fastq to bam is 4.3h, on-demand cost 1.65 USD.


## DeepVariant 
Thie docker container Deepvariant.
Set arameters of container

![parameters](https://github.com/lifebit-ai/Phenopolis/blob/master/DV1.png "")

Next select job execution 
 
![parameters](https://github.com/lifebit-ai/Phenopolis/blob/master/DV2.png "")
Runtime on c5.2xlarge instance from fastq to bam is 0.3h, 0.1 USD.


## Cellbase 
Thie docker container CellBase. To run in the platform first:
Set arameters of container

![parameters](https://github.com/lifebit-ai/Phenopolis/blob/master/cellbase1.png "")

Next select job execution 
 
![parameters](https://github.com/lifebit-ai/Phenopolis/blob/master/cellbase2.png "")
Runtime on c5.2xlarge instance from fastq to bam is 0.3h, 0.1 USD.
