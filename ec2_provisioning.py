#!/usr/bin/env python3

"""
Practice script to provision an EC2 instance using Python.
"""

import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

instance = ec2.create_instances(
    ImageId='***',
    InstanceType='t3.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='***'
)

print(instance[0].id)

ami-0254b2d5c4c472488
new-python-key