from boto3.dynamodb.conditions import Key, Attr
import boto3
import json


def update_dynamodb(id, stock, add_stock, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table_name  = "product"
    dynamotable = dynamodb.Table(table_name)

    response = dynamotable.update_item(
        Key={
            'id': id,
        },
        UpdateExpression="set stock=:s",
        ExpressionAttributeValues={
            ':s': add_stock
        },
        ReturnValues="UPDATED_NEW"
    )
    return response
