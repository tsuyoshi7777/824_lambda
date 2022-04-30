import line, update_dynamodb
import boto3
import json

# Crawling.py(楽天 & Amazon) → sqs(add_stock) → Check.py
def lambda_handler(event, context):
    for record in event["Records"]:
       payload   = record["body"]
       print("payload", payload, sep="\n")
       payload   = eval(payload)
       print("payload_e", payload, sep="\n")
       url       = payload['url']
       id        = payload["id"]
       stock     = payload["stock"]
       add_stock = payload["add_stock"]
       name      = payload["name"]

       print('id',id, sep="\n")
       print('name',name, sep="\n")
       print('stock',stock, sep="\n")
       print('add_stock',add_stock, sep="\n")

       if stock == "0" and add_stock == "1":
           # LINE通知（在庫復活）
           line.stock_availability(payload)
           # dynamodbのstock値更新
           update_response = update_dynamodb.update_dynamodb(id, stock, add_stock)
           print('updateできました', update_response, sep="\n")
           return update_response

       elif stock == "1" and add_stock == "0":
           # LINE通知（在庫なくなる）
           line.stock_not_availability(payload)
           # dynamodbのstock値更新
           update_response = update_dynamodb.update_dynamodb(id, stock, add_stock)
           print('updateできました', update_response, sep="\n")
           return update_response
