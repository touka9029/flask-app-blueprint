#!/bin/sh -exu

IMAGE_NAME=flask-app-blueprint:latest
CONTAINER_NAME=flask-app-blueprint

docker build -t $IMAGE_NAME .
docker run --name $CONTAINER_NAME -d -p 5000:5000 $IMAGE_NAME
