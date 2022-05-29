FROM python:latest

RUN apt update && apt upgrade \
	&& apt install -y postgresql postgresql-contrib \
	&& apt install sudo \
	&& apt clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

