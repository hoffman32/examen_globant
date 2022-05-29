FROM python:latest

RUN apt update && apt upgrade \
	&& apt install -y postgresql postgresql-contrib \
	&& apt install sudo \
	&& apt -y install vim \
	&& apt -y install systemctl \
	&& apt -y install dbus \
	&& apt clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

