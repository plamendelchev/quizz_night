#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

IMAGE_DIR="$(cd $(dirname ${BASH_SOURCE[0]}) >/dev/null 2>&1 && cd ../docker/uwsgi_base/ && pwd)"

docker build -t quizz_uwsgi:base "${IMAGE_DIR}"
