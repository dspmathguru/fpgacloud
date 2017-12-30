#!/usr/bin/env python
# Stop the instance that this command is run in
#    Assumes you have permission through a role to do this

import boto3
import MyMetaData

if __name__ == "__main__":
  myMetaData = MyMetaData.MyMetaData().meta
  zone = myMetaData['placement']['availability-zone']
  print(zone)
  ec2 = boto3.resource('ec2', region_name=zone)
  ec2.instances.filter(InstanceId=myMetaData['instance-id']).stop()
