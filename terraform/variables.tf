locals {
  # Enable Harness.io CICD features?
  enable_cicd_harness = (
    length(trim(var.cicd_harness_account)) > 0 &&
    length(trim(var.cicd_harness_role))
  )
}
variable "tf_role_name" {
  type        = string
  description = ""
  default     = "terraform-admin"
}

variable "cicd_harness_account" {
  type        = string
  description = ""
  default     = ""
}

variable "cicd_harness_role" {
  type        = string
  description = "Create trust relationship with harness delegate role in the nd-idp-prod AWS account"
  # arn:aws:iam::{accountnum}:role/idp-harness-svc-non-prod or arn:aws:iam::{accountnum}:role/idp-harness-svc-prod (PROD vs NON-PROD)
  default = ""
}
