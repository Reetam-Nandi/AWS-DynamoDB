import boto3
import json

dynamo = boto3.client('dynamodb')
def lambda_handler(event, context):

    operation = event['httpMethod'] 
    if operation == 'GET': #Only need Primary Key Value and Table Name
        response = dynamo.get_item(Key=event['body'],TableName=event['TblName'])
        resdict = {
        "PhoneNumber":response['Item']['phonenumber']['S'],
        "Name":response['Item']['uname']['S'],
        "Email":response['Item']['mailid']['S'],
        "Address":response['Item']['pass']['S']
        }
        return (resdict)
    elif operation == 'DELETE': #Only need Primary Key Value and Table Name 
        dynamo.delete_item(Key=event['body'],TableName=event['TblName'])
        return ("Delete Successful")
    elif operation == 'POST': #Needs Items to be inserted and Table Name
        dynamo.put_item(Item=event['body2'],TableName=event['TblName'])
        return ("Insert Successful")
    elif operation == 'PUT': #Needs Key, UpdateExpression, ExpressionAttributeValues and Table Name
        dynamo.update_item(Key=event['body'],TableName=event['TblName'],
        UpdateExpression=event['UE'],ExpressionAttributeValues=event['EAV'])
        return ("Update Successful")
    else:
        print("Possible Operations are GET, POST, PUT & DELETE only\n")
        
# Documentation : https://boto3.amazonaws.com/v1/documentation/api/1.9.42/reference/services/dynamodb.html?highlight=dynamodb.#client