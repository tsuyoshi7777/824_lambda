# AWS_login

resource "null_resource" "ecr_lambda_push" {
  provisioner "local-exec" {
    command = "aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin aws-id.dkr.ecr.ap-northeast-1.amazonaws.com"
  }



  # lambda_read_dynamodb

  provisioner "local-exec" {
    command = "docker build -t lambda_read_dynamodb -f ../Dockerfiles/lambda_read_dynamodb_Dockerfile ."
  }

  provisioner "local-exec" {
    command = "docker tag lambda_read_dynamodb:latest aws-id.dkr.ecr.ap-northeast-1.amazonaws.com/lambda_read_dynamodb:latest"
  }

  provisioner "local-exec" {
    command = "docker push aws-id.dkr.ecr.ap-northeast-1.amazonaws.com/lambda_read_dynamodb:latest"
  }



  # lambda_Crawling

  provisioner "local-exec" {
    command = "docker build -t lambda_crawling -f ../Dockerfiles/lambda_Crawling_Dockerfile ."
  }

  provisioner "local-exec" {
    command = "docker tag lambda_crawling:latest aws-id.dkr.ecr.ap-northeast-1.amazonaws.com/lambda_crawling:latest"
  }

  provisioner "local-exec" {
    command = "docker push aws-id.dkr.ecr.ap-northeast-1.amazonaws.com/lambda_crawling:latest"
  }



  # lambda_Check

  provisioner "local-exec" {
    command = "docker build -t lambda_check -f ../Dockerfiles/lambda_Check_Dockerfile ."
  }

  provisioner "local-exec" {
    command = "docker tag lambda_check:latest aws-id.dkr.ecr.ap-northeast-1.amazonaws.com/lambda_check:latest"
  }

  provisioner "local-exec" {
    command = "docker push aws-id.dkr.ecr.ap-northeast-1.amazonaws.com/lambda_check:latest"
  }


}
