#!/bin/bash

docker-compose down -v --remove-orphans
docker-compose build application
docker-compose run application bash
docker-compose down -v --remove-orphans
