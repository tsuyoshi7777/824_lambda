resource "aws_lambda_function" "lambda_Check" {
  function_name    = "lambda_Check"
  role             = aws_iam_role.iam_for_lambda.arn
  timeout          = 300
  memory_size      = 384
  package_type     = "Image"
  image_uri        = "${aws_ecr_repository.lambda_Check.repository_url}:latest"
  lifecycle {
    ignore_changes = [image_uri]
  }
  depends_on = ["null_resource.ecr_lambda_push"]
}

resource "aws_lambda_event_source_mapping" "sqs_stock_check" {
  event_source_arn = aws_sqs_queue.sqs_stock_check.arn
  function_name    = aws_lambda_function.lambda_Check.arn
}
