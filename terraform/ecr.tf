# lambda_read_dynamodb

resource "aws_ecr_repository" "lambda_read_dynamodb" {
  name                 = "lambda_read_dynamodb"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}


# lambda_Crawling

resource "aws_ecr_repository" "lambda_Crawling" {
  name                 = "lambda_crawling"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}


# lambda_Check

resource "aws_ecr_repository" "lambda_Check" {
  name                 = "lambda_check"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
