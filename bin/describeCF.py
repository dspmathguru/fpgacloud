#!/usr/bin/env python3

import boto3
import pprint
import argparse

parser = argparse.ArgumentParser(
    description='describes the specified cloudformation stack')
parser.add_argument('stack_name', action='store',
                    default=None,
                    help='stack name or arn for stack')
parser.add_argument('-r', '--region', action='store',
                    default='us-west-2',
                    help='region name')

args = parser.parse_args()

client = boto3.client('cloudformation', region_name=args.region)

try:
  rsp = client.describe_stacks(
      StackName=args.stack_name)
  pp = pprint.PrettyPrinter(indent=2)
  pp.pprint(rsp)
except:
  if args.stack_name:
    print('Stack "' + args.stack_name + '" not found in region' + args.region)
