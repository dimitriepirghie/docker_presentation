
# Set the base image
FROM ubuntu:latest

# File Author/ Maintainer
MAINTAINER Dimitrie Pirghie "dimitriepirghie94@gmail.com"

# Add the application resources URL
# RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list

# Update sources
RUN apt-get update -y

# Install python
RUN apt-get install -y python python-pip

# Install app dependencies

COPY . /tweets_viewer

#Set default WD CMD Will execute
WORKDIR /tweets_viewer


RUN pip install -r requirements.txt

# Expose ports

ENTRYPOINT ["python"]

CMD ["tweets_viewer.py"]
