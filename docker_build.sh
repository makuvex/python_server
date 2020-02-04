docker build -t corona:0.1 .
docker run -d -p 5000:5000 -it --name corona corona:0.1 /bin/sh
