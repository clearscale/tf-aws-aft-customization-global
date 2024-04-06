# API Helpers

API helpers perform actions that cannot be performed within Terraform.

## Delete Default VPCs

AFT is supposed to delete the default VPCs, but there is known bug in AFT that [will not be fixed in the 1.x major version release](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/issues/393#issuecomment-1743705097). AWS has outlined their reasons why in [issue #142](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/issues/142#issuecomment-1178228741). To workaround this, we've implemented a Python customization to delete the default VPCs globally as the accounts are created.

[delete_vpc.py](./delete_vpc.py) script will delete the "out of the box VPCs".

There are two sets of VPCs that are created automatically that should be deleted if not used.

1. Default VPCs created with any new account
   CIDR: `172.31.0.0/16`
   Default VPC: true
   https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html

2. AWS Control Tower VPC
   CIDR: `172.31.0.0/16` (default range, configurable in Control Tower Account Factory settings)
   https://docs.aws.amazon.com/controltower/latest/userguide/vpc-concepts.html

Python script from `post-api-helpers.sh`

```
python3 ./delete_vpc.py '172.31.0.0/16'
```

## Delete DHCP Options

Similar to above, if AWS Control Tower has deleted the default VPC and replaced it with the Control Tower VPC, the default DHCP options for the default VPC will be left behind.

This will only delete DHCP options that are not attached to any VPC.

Python script from `post-api-helpers.sh`

```
python3 ./delete_dhcp.py
```