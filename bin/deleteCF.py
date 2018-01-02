#!/usr/bin/env python3

import boto3
import argparse

parser = argparse.ArgumentParser(
    description='deletes the specified cloudformation stack')
parser.add_argument('stack_name', action='store',
                    help='stack name or arn for stack')

args = parser.parse_args()

client = boto3.client('cloudformation')
rsp = client.delete_stack(StackName=args.stack_name)

print(rsp)
