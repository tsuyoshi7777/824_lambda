import boto3
import json

def send_to_sqs(message, queue_name):
    sqs = boto3.resource('sqs')

    try:
        queue = sqs.get_queue_by_name(QueueName=queue_name)
    except:
        queue = sqs.create_queue(QueueName=queue_name)

    message_json = json.dumps(message)
    response  = queue.send_message(MessageBody=message_json)

    return response
