resource "aws_lambda_function" "lambda_read_dynamodb" {
  function_name    = "lambda_read_dynamodb"
  role             = aws_iam_role.iam_for_lambda.arn
  package_type     = "Image"
  image_uri        = "${aws_ecr_repository.lambda_read_dynamodb.repository_url}:latest"
  lifecycle {
    create_before_destroy = true
  }
  depends_on = ["null_resource.ecr_lambda_push"]
}
