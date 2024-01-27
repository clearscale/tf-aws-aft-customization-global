import json
import boto3


client = boto3.client('ec2', region_name='us-east-1')

# filters = [*]
# vpcs = list(ec2.vpcs.filter(Filters=filters))

vpcs = client.describe_vpcs()

print(vpcs)