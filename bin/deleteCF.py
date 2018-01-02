#!/usr/bin/env python3

import boto3
import argparse
import pprint

parser = argparse.ArgumentParser(
    description='deletes the specified cloudformation stack')
parser.add_argument('stack_name', action='store',
                    help='stack name or arn for stack')
parser.add_argument('-r', '--region', action='store',
                    default='us-west-2',
                    help='region name')

args = parser.parse_args()

client = boto3.client('cloudformation', region_name=args.region)
rsp = client.delete_stack(StackName=args.stack_name)
