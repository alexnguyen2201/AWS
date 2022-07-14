# TODO
# ! 1. Create dynamo Table
# ! 2. Enable Data Stream to Kinesis
# ! 3. Create Lambda Function
# ! 4. Give Lambda Function new policy to perform all GET, LIST, DESC,
# ! 5. Trigger lambda function through Kinesis Message
# ! 6. Process Message in Lambda

import base64
import json


def lambda_handler(event, context):
    print("Lambda function invoked!")
    for record in event["Records"]:
        decoded_data = json.loads(base64.b64decode(
            record["kinesis"]["data"]).decode("utf-8"))

        print("Here is a message...")
        print(decoded_data)

        if decoded_data["eventName"] == "INSERT":
            inserted_data = decoded_data["dynamodb"]["NewImage"]
            # Send welcome email...
            print(
                f"New customer joined! Customer name is {inserted_data['name']['S']}")

        if decoded_data["eventName"] == "MODIFY":
            old_data = decoded_data["dynamodb"]["OldImage"]
            new_data = decoded_data["dynamodb"]["NewImage"]

            print(
                f"Customer updated! Old name was {old_data['name']['S']} and the new name is {new_data['name']['S']}")

        if decoded_data["eventName"] == "REMOVE":
            deleted_data = decoded_data["dynamodb"]["OldImage"]
            print(
                f"Customer removed! Send farewell email to: {deleted_data['name']['S']}")

    return {'statusCode': 200, 'body': json.dumps('Hello from Lambda!')}
