#!/bin/bash

echo "Executing Post-API Helpers"

# echo "aws sts get-caller-identity"
# aws sts get-caller-identity
# aws ec2 describe-regions

echo "----- Access folder: CD \API_Helpers -------"
cd $DEFAULT_PATH/$CUSTOMIZATION/api_helpers/

python3 ./delete_vpc.py