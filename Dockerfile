FROM maven:openjdk

COPY . /automation

WORKDIR /automation

RUN ["mvn", "dependency:go-offline"]