################## BASE IMAGE ######################
FROM ubuntu:18.04 
FROM python:3.6

################## INSTALLATION ######################
WORKDIR /app
COPY settings.xml $HOME/m2
RUN apt-get update && apt-get upgrade -y 
RUN apt-get install default-jdk -y 
RUN wget http://mirror.vorboss.net/apache/maven/maven-3/3.5.4/binaries/apache-maven-3.5.4-bin.tar.gz 
RUN tar xzvf apache-maven-3.5.4-bin.tar.gz && export PATH=/app/apache-maven-3.5.4/bin:$PATH
RUN wget https://github.com/opencb/cellbase/releases/download/v4.5.6/cellbase-4.5.6.tar.gz
RUN tar xzvf cellbase-4.5.6.tar.gz

ENTRYPOINT ["cellbase-4.5.6/bin/cellbase.sh", "variant-annotation", "-t", "8"]
