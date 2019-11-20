#!/usr/bin/env bash

SOURCE="${BASH_SOURCE[0]}"
SCRIPT_FILE_PATH=`/usr/bin/readlink -e ${SOURCE}`
SCRIPT_DIR=`/usr/bin/dirname ${SCRIPT_FILE_PATH}`
APP_PATH=`/usr/bin/dirname ${SCRIPT_DIR}`
PYTHON_PATH=${APP_PATH}/rtsp/python/bin

if [[ $# -eq 1 ]]; then
    ${PYTHON_PATH}/python ${APP_PATH}/autodeploy/auto_deploy.py $1
else
    ${PYTHON_PATH}/python ${APP_PATH}/autodeploy/auto_deploy.py
fi
