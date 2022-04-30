resource "aws_sqs_queue" "sqs_dynamodb" {
  name                       = "sqs_dynamodb"
  visibility_timeout_seconds = 300
}

resource "aws_sqs_queue" "sqs_stock_check" {
  name                       = "sqs_stock_check"
  visibility_timeout_seconds = 300
}
