#!/bin/bash

echo "Executing Post-API Helpers"

cd $DEFAULT_PATH/$CUSTOMIZATION/api_helpers/

# Must define region if running manually
# export AWS_DEFAULT_REGION=us-west-2
python3 ./delete_vpc.py '172.31.0.0/16'

python3 ./delete_dhcp.py