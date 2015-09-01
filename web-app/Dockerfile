FROM ubuntu:14.04 
MAINTAINER Mr.Mohammed Syed 
RUN sudo apt-get update
RUN sudo apt-get install -y python-dev libmysqlclient-dev python3.4 python-pip
RUN sudo pip install MySQL-python Flask==0.10.1
WORKDIR /usr/local/webappcontainer/
EXPOSE 5000
