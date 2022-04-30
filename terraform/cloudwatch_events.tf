resource "aws_cloudwatch_event_rule" "sample" {
    name                = "sample"
    description         = "sample"
    schedule_expression = "cron(0 1 * * ? *)"
}

resource "aws_cloudwatch_event_target" "sample" {
    rule      = aws_cloudwatch_event_rule.sample.name
    target_id = "lambda_read_dynamodb"
    arn       = aws_lambda_function.lambda_read_dynamodb.arn
}
