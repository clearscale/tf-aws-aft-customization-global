data "aws_iam_policy" "cicd_hardness_policy_admin" {
  count = (local.enable_cicd_harness) ? 1 : 0
  arn   = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:policy/Administrator"
}

data "aws_iam_policy_document" "cicd_hardness_policy_assume_role" {
  count = (local.enable_cicd_harness) ? 1 : 0
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "AWS"
      identifiers = ["arn:aws:iam::${var.cicd_harness_account}:${var.cicd_harness_role}"]
    }
  }
}

resource "aws_iam_role" "cicd_hardness_policy_document" {
  count               = (local.enable_cicd_harness) ? 1 : 0
  name                = var.tf_role_name
  assume_role_policy  = data.aws_iam_policy_document.cicd_hardness_policy_assume_role[0].json
  managed_policy_arns = [data.aws_iam_policy.cicd_hardness_policy_admin[0].arn]
}
