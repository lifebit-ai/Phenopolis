################## BASE IMAGE ######################
FROM ubuntu:18.04 
FROM python:3.6

################## INSTALLATION ######################
WORKDIR /app
COPY bwaWrapper.py /app

################## ORIGINAL GENOME REFERENCE SOURCES ######################
# https://deepvariant-data.s3.amazonaws.com/genomes/hg19/hg19.fa ===> hg19.fa 
# https://deepvariant-data.s3.amazonaws.com/genomes/h38/GRCh38.p10.genome.fa ===> GRCh38.fa

COPY hg19* /app/

RUN wget https://github.com/lh3/bwa/archive/v0.7.17.tar.gz && \
	tar xvfz v0.7.17.tar.gz && \
	cd bwa-0.7.17 && make && cp bwa /app

RUN wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 && \
    tar xvjf samtools-1.9.tar.bz2 && \
	cd samtools-1.9 && ./configure --prefix=/app && make && make install && cp samtools /app 

ENV PATH "$PATH:/app/samtools-1.9:" 	  

ENTRYPOINT [ "python3", "./bwaWrapper.py" ]
