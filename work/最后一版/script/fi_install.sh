#!/bin/bash
if [[ ${USER} != "root" ]]; then
    echo "only the root user can run this script, now the user is ${USER}"
    exit 1
fi
script_abs=$(readlink -f "$0")
script_dir=$(dirname $script_abs)
cd ${script_dir}
python ./third/third.py install &> /dev/null

if [[ $1 == "" ]];then
    read -p "please input 'install or uninstall' : " choice
fi
if [[ $1 != "" ]];then
    choice=$1
fi
if [[ $choice == "install" ]];then
    python run.py install
fi
if [[ $choice == "uninstall" ]];then
    python run.py uninstall
fi

if [[ $choice == "retry" ]];then
    python run.py retry
fi
