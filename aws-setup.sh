#!/bin/bash
# Setup for AWS Amazon Linux environments

sudo yum install python36-devel python36-pip -y
sudo yum install direnv

# get the directory of this file
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR

python3.6 -m venv --without-pip .venv
source .venv/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python
deactivate
source .venv/bin/activate

pip install -r requirements.txt
