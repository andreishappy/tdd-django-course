#!/usr/bin/env bash
set -e

command="$@"

# Ensure that the pod is deleted
function cleanup {
    docker-compose down
}
trap cleanup EXIT
cleanup

docker-compose up --build -d
docker-compose run app python puppy_store/manage.py migrate
# block here
tail -f /dev/null
