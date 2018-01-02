#!/usr/bin/env python3

import boto3
import argparse
import pprint

parser = argparse.ArgumentParser(
    description='deletes the specified cloudformation stack')
parser.add_argument('stack_name', action='store',
                    help='stack name or arn for stack')
parser.add_argument('template_name', action='store',
                    help='template file name')
parser.add_argument('-r', '--region', action='store',
                    default='us-west-2',
                    help='region name')

args = parser.parse_args()

file_name = args.template_name
stack_name = args.stack_name

with open(file_name, "r") as myfile:
  data = myfile.read()

client = boto3.client('cloudformation', region_name=args.region)

rsp = client.create_stack(StackName=stack_name, TemplateBody=data,
                          Parameters=[{'ParameterKey': 'CIDRRange',
                                       'ParameterValue': '10.100.0.0'}],
                          OnFailure='DELETE')

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(rsp)
