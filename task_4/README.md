# Task 4. Nginx + lite-server's + JSON-server's

## Prerequisites

Install docker and docker-compose. Done tasks: 2, 3.

## Links

* https://hub.docker.com/_/nginx
* http://nginx.org/en/docs

## Description

* Pull docker image "nginx".
* Create docker-compose.yaml for containers:
  * nginx
  * lite-server's (no port forwarding)
  * JSON-server's (no port forwarding)
* Scale lite-server containers up to 3.
* Scale JSON-server containers up to 3.
* Deploy containers and test the result.

## Goals

* Setup volumes mounting
* Setup ports forwarding
* Setup environment
* Check availability of REST resources in container
