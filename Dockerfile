FROM ubuntu:16.04 # base linux ubuntu image
MAINTAINER makuvex "makuvex7@gmail.com"

RUN apt-get update
RUN apt-get install -y nginx  #install nginx
RUN echo "hello i am ubuntu container"

WORKDIR /etc/nginx #set CMD command on path

CMD ["nginx", "-g", "daemon off;"]  #run nginx with background mode

EXPOSE 80 #open web server port 80
