FROM ubuntu:20.04

RUN apt -qq update

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata

RUN apt -qq install -y git python3 ffmpeg python3-pip


RUN git clone https://github.com/rooted-cyber/Zee5-Downloader-1
RUN cd Zee*;pip3 install --no-cache-dir -r requirements.txt

RUN cd Zee*;bash start.sh
