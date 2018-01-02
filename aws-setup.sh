#!/bin/bash
# Setup for AWS Amazon Linux environments

if [-f /etc/redhat-release]
then
  # Centos or RedHat
  sudo yum update -y
  sudo yum install yum-utils -y
  sudo yum groupinstall development -y
  sudo yum install https://centos7.iuscommunity.org/ius-release.rpm -y
  sudo yum install python36u -y
else
  # Amazon OS
  sudo yum install python36-devel python36-pip -y
fi

# get the directory of this file
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR

# a difficult way to get .venv created as there is some issue on Amazon Linux
#   with module venv
python3.6 -m venv --without-pip .venv
source .venv/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python
deactivate
source .venv/bin/activate

pip install -r requirements.txt

# should add check if this was already added
echo -e \
  "\n### auto added by fpgacloud/aws-setup.sh\nexport PATH=$PATH:~/fpgacloud/.venv/bin:~/fpgacloud/bin\n" \
  >> ~/.bashrc
