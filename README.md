# AWS Lambda + Docker + Terraform + Python + Selenium スクレイピング開発

AWS Lambda + Docker + Terraform + Python + Selenium + SQS + DynamoDB + CloudwatchEvents + LINE がリソースです。

Terraformで、AWSのリソースは全て作成しています。（S3、DynamoDB以外）

アプリの内容は、ECサイトにある目的の商品の在庫状況変化をLINEで通知するものになります。

商品データ（商品名、URL、在庫状況など）を表の形でcsvに記載し、そのデータをS3経由でDynamoDBに格納。（この処理は、CloudFormationで行なっています。）

CloudwatchEventsの定期実行をトリガーにLambdaがDynamoDBからデータ（商品URL）を取り出し、SQSに送信経由して並列処理をし、もう一つのLambdaで商品データのURLを元にスクレイピング。

在庫状況を取得したら、またSQSへ送信し、並列処理経由で別のLambdaが在庫状況データをチェック。

在庫状況に変化があれば、LINE通知と DynamoDBへの値更新を行います。
