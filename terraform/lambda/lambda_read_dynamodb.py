import send_to_sqs
import boto3


# dynamodb
dynamodb    = boto3.resource('dynamodb')
table_name  = 'product'
dynamotable = dynamodb.Table(table_name)

# sqs_queue
queue_name  = 'sqs_dynamodb'

def handler(event, context):

    response = dynamotable.scan()
    items = response["Items"]

    for item in items:
        send_to_sqs.send_to_sqs(item, queue_name)
        # sqs(dynamodb) → Crawling.py

    return items
