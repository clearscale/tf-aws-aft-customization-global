# AFT: Global Account Customizations

Copy this repository, mark it as private, and enable custom features in [terraform/terraform.tfvars](./terraform/terraform.tfvars).

This repository contains the [Account Factory for Terraform (AFT) global account customizations](https://docs.aws.amazon.com/controltower/latest/userguide/aft-account-customization-options.html) and serves as a practical use case of the AFT account customizations logic. As described in the [AFT Code Repositories](https://github.com/clearscale/tf-aws-aft?tab=readme-ov-file#aft-code-repositories) section in the main AFT repo, AFT is a [GitOps](https://en.wikipedia.org/wiki/DevOps#:~:text=referenced%20as%20examples.-,GitOps,rolled%20back%20using%20version%2Dcontrolling.) solution and this is one of the five repositories related to deploying and managing accounts in AWS.

AWS Resources (customizations) can be created through Terraform or through Python, leveraging the API helpers. The customization execution is parameterized at runtime.

## What belongs here?

The purpose of this repository is to facilitate global account customizations. For instance, when a new account is provisioned through AFT, there might be a requirement to deploy an IAM role to *all* accounts immediately upon their creation. This illustrates the key application for the AFT *Global* Account Customization repository. In contrast, any account specific customizations should go in the [AFT Account Customization Repository](https://github.com/clearscale/tf-aws-aft-customization-account).

## What does *not* belong here?

Infrastructure as Code (IaC) scripts or code that are targeted at specific accounts should not be included here. See the [AFT Account Customization Repository](https://github.com/clearscale/tf-aws-aft-customization-account) for applying resources to individual accounts. However, Non-essential or non-foundational resources not related to account setup are also outside the scope of all AFT repositories. The aim is to maintain the AFT framework with a minimal a footprint.

## AFT Code Repositories

1. [Primary AFT Module](https://github.com/clearscale/tf-aws-aft)
2. [Account Definitions](https://github.com/clearscale/tf-aws-aft-accounts)
3. [Account Customizations](https://github.com/clearscale/tf-aws-aft-customization-account)
4. [Global Account Customizations](https://github.com/clearscale/tf-aws-aft-customization-global)
5. [Account Provisioning Customizations](https://github.com/clearscale/tf-aws-aft-customization-account-provisioning)

## Usage

To leverage Global Customizations, populate this repo as per the instructions below.

### Terraform

AFT provides Jinja templates for [Terraform](./terraform/) backend and providers. These render at the time Terraform is applied. If needed, additional providers can be defined by creating a providers.tf file.

To create Terraform resources, provide your own Terraform files (ex. main.tf, variables.tf, etc) with the resources you would like to create, placing them in the 'terraform' directory.

Currently, there is an example on how to create a [Harness.io](https://www.harness.io/)

### API Helpers

The purpose of [API helpers](./api_helpers/) is to perform actions that cannot be performed within Terraform.

#### Python

The [api_helpers/python](./api_helpers/python/) folder contains a requirements.txt, where you can specify libraries/packages to be installed via PIP.

#### Bash

Bash scripts in the [api_helpers](./api_helpers/) directory is where you define what runs before/after Terraform, as well as the order the Python scripts execute, along with any command line parameters. These bash scripts can be extended to perform other actions, such as leveraging the AWS CLI or performing additional/custom Bash scripting.

- [pre-api-helpers.sh](./api_helpers/pre-api-helpers.sh)- Actions to execute prior to running Terraform.
- [post-api-helpers.sh](./api_helpers/post-api-helpers.sh) - Actions to execute after running T