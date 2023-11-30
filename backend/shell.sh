#!/bin/bash
set -e

current_dir=$(pwd)

cd ../

docker-compose down -v --remove-orphans
docker-compose build application
docker-compose run application bash
docker-compose down -v --remove-orphans

cd $current_dir