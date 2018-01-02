#!/usr/bin/env python3

import boto3
import pprint
import argparse

parser = argparse.ArgumentParser(
    description='describes the specified cloudformation stack')
parser.add_argument('stack_name', action='store',
                    default=None,
                    help='stack name or arn for stack')

args = parser.parse_args()

client = boto3.client('cloudformation')

try:
  rsp = client.describe_stacks(StackName=args.stack_name)
  pp = pprint.PrettyPrinter(indent=2)
  pp.pprint(rsp)
except:
  if args.stack_name:
    print('Stack "' + args.stack_name + '" not found')
