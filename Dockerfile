FROM ubuntu:16.04

MAINTAINER Demi.Goldberg@gmail.com

EXPOSE 80
EXPOSE 8800

RUN apt-get update
RUN apt-get install -y apache2 python-setuptools libapache2-mod-wsgi python-six
RUN mkdir -p /var/www/html/example
COPY . /var/www/html/example
WORKDIR /var/www/html/example

CMD ["python", "hello.py","8800"]
