resource "aws_lambda_function" "lambda_Crawling" {
  function_name    = "lambda_Crawling"
  role             = aws_iam_role.iam_for_lambda.arn
  timeout          = 300
  memory_size      = 4000
  package_type     = "Image"
  image_uri        = "${aws_ecr_repository.lambda_Crawling.repository_url}:latest"
  lifecycle {
    create_before_destroy = true
  }
  depends_on = ["null_resource.ecr_lambda_push"]
}

resource "aws_lambda_event_source_mapping" "sqs_dynamodb" {
  event_source_arn = aws_sqs_queue.sqs_dynamodb.arn
  function_name    = aws_lambda_function.lambda_Crawling.arn
}
