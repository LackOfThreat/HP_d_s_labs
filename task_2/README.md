# Task 2. Lite-server

## Prerequisites

Install docker and docker-compose.

## Links

* https://hub.docker.com/_/node
* https://www.npmjs.com/package/lite-server

## Description

* Pull docker image "node".
* Create docker-compose.yaml for container with lite-server.
* Create static resources for container.
* Deploy container and test the result.

## Goals

* Setup volumes mounting
* Setup ports forwarding
* Setup environment
* Check availability of resources via port


## What was done

* App on python. Flask server which returns current time to HTML.
* Code for storage (local MongoDB).
* Connected volume, mongodb local container (127.17.0.1:27017). Each timestamp is stored in our volume and prints back every time we reload. Restart of container won't delete information.
* Environment vars in docker-compose.yml (timezone, etc)
* Resources (word in json format, which are used to print message on HTML). Changing it will lead to changes on printing words.