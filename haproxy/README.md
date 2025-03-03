Reference article: https://www.haproxy.com/blog/how-to-run-haproxy-with-docker

Note that we are covering how to run HAProxy, not the HAProxy Kubernetes Ingress Controller.

1. sudo docker network create --driver=bridge haproxy-net


2. Run application

$ sudo docker run -d \
   --name web1 --net haproxy-net jmalloc/echo-server:latest
   
$ sudo docker run -d \
   --name web2 --net haproxy-net jmalloc/echo-server:latest
   
$ sudo docker run -d \
   --name web3 --net haproxy-net jmalloc/echo-server:latest


3. Run docker:

 sudo docker run -d \
   --name local-haproxy \
   --net haproxy-net \
   -v $(pwd):/usr/local/etc/haproxy:ro \
   -p 80:80 \
   -p 8404:8404 \
   haproxytech/haproxy-alpine:2.4

#Run with the local python

```sh
   sudo docker run -d \
      --name local-haproxy \
      -v $(pwd):/usr/local/etc/haproxy:ro \
      -p 80:80 \
      -p 8404:8404 \
      haproxytech/haproxy-alpine:2.4
```

# todo : document how run haproxy pointing to the local instance - deprecate the other server that we dont own the control (no sense for a sandbox goal)


docker official images:

- HAProxy (Alpine Linux base)- https://hub.docker.com/r/haproxytech/haproxy-alpine

- HAProxy (Ubuntu base) – https://hub.docker.com/r/haproxytech/haproxy-ubuntu

- HAProxy (Debian base) – https://hub.docker.com/r/haproxytech/haproxy-debian


4. Delete if required

```sh
   sudo docker stop web1 && sudo docker rm web1 && 
   sudo docker stop web2 && sudo docker rm web2 &&
   sudo docker stop web3 && sudo docker rm web3 &&
   sudo docker stop local-haproxy && sudo docker rm local-haproxy &&
   sudo docker network rm haproxy-net
```