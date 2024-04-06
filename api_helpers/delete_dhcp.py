#!/usr/bin/env python
# Must be the first line
from __future__ import print_function

import json
import boto3

VERBOSE = 1
THREADPOOL_MAX_WORKERS = 20

def get_regions(client):
  """ Build a region list """

  reg_list = []
  regions = client.describe_regions()
  data_str = json.dumps(regions)
  resp = json.loads(data_str)
  region_str = json.dumps(resp['Regions'])
  region = json.loads(region_str)
  for reg in region:
    reg_list.append(reg['RegionName'])

  print("Found regions:")
  print(reg_list)
  return reg_list

def get_used_dhcp(client):
  """ Get all used DHCP options by used VPCs """
  dhcp_list = []
  vpcs = client.describe_vpcs()
  vpcs_str = json.dumps(vpcs)
  resp = json.loads(vpcs_str)
  data = json.dumps(resp['Vpcs'])
  vpcs = json.loads(data)
  
  for vpc in vpcs:
    print("DHCP: {0} used by VPC {1}".format(vpc['DhcpOptionsId'], vpc['VpcId']))
    dhcp_list.append(vpc['DhcpOptionsId'])
  
  return dhcp_list

def get_dhcp(client, used_dhcp):
  """ Checks against used list above and finds unused DHCPs """
  dhcps = client.describe_dhcp_options()
  dhcp_str = json.dumps(dhcps)
  resp = json.loads(dhcp_str)
  data = json.dumps(resp['DhcpOptions'])
  dhcps = json.loads(data)
  
  dhcp_list = []
  for dhcp in dhcps:
    dhcp_id = dhcp['DhcpOptionsId']
    if dhcp_id in used_dhcp:
      print("DHCP: {0} found in list, ignoring... ".format(dhcp_id))
    else: 
      print("DHCP: {0} found NOT in list, adding to be deleted ".format(dhcp_id))
      dhcp_list.append(dhcp_id)
  
  return dhcp_list
  # print(data)

def del_dhcp(ec2, not_used_dhcp):
  """ Delete the DHCP options that are NOT used """
  
  for dhcp in not_used_dhcp:
    dhcp_resource = ec2.DhcpOptions(dhcp)
    try:
      print("Removing dhcp : ", dhcp_resource.id)
      dhcp_resource.delete(
        # DryRun=True
      )
    except boto3.exceptions.ClientError as e:
      print(e)

def main():
  client = boto3.client('ec2')
  regions = get_regions(client)

  for region in regions:
    try:
      client = boto3.client('ec2', region_name = region)
      ec2 = boto3.resource('ec2', region_name = region)
      
      # find used DHCP option sets - ones associated with VPC
      used_dhcp = get_used_dhcp(client)
      
      # find unused DHCP option sets
      not_used_dhcp = get_dhcp(client, used_dhcp)
      
      del_dhcp(ec2, not_used_dhcp)
      
    except boto3.exceptions.Boto3Error as e:
      print(e)
      exit(1)
    
  print('End of script -- Deleted all unused DHCP options')

if __name__ == "__main__":
  main()