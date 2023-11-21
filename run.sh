#!/bin/bash

docker-compose down -v --remove-orphans
docker-compose build application
docker-compose up
docker-compose down -v --remove-orphans
