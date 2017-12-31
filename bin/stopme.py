#!/usr/bin/env python
# Stop the instance that this command is run in
#    Assumes you have permission through a role to do this
# Basically a fancy way of saying 'sudo shutdown -h now'

import boto3
import MyMetaData

if __name__ == "__main__":
  myMetaData = MyMetaData.MyMetaData().meta
  region_name = myMetaData['placement']['availability-zone'][:-1]
  print(region_name)
  ec2 = boto3.resource('ec2', region_name=region_name)
  ec2.Instance(myMetaData['instance-id']).stop()
