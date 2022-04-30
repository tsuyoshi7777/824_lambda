resource "aws_cloudwatch_log_group" "lambda_Check" {
  name              = "/aws/lambda/lambda_Check"
  retention_in_days = 7
}

resource "aws_cloudwatch_log_group" "lambda_Crawling" {
  name              = "/aws/lambda/lambda_Crawling"
  retention_in_days = 7
}

resource "aws_cloudwatch_log_group" "lambda_read_dynamodb" {
  name              = "/aws/lambda/lambda_read_dynamodb"
  retention_in_days = 7
}
