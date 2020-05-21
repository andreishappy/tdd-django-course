#!/usr/bin/env bash
set -e

command="$@"

docker build -t dev-image .
docker run -v "$(pwd):/code" --env DUMMY_DB=true dev-image "$@"
