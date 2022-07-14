from inspect import Attribute
import boto3

client = boto3.client('dynamodb')

# TODO: get item
# response = client.get_item(
#     TableName='student',
#     Key={"student_id": {"N": "2"}},
#     AttributesToGet=["student_id", "age", "name", "gender"]
# )

# print(response["Item"])

# TODO: delete item
# response = client.delete_item(
#     TableName="student",
#     Key={"student_id": {"N": "1"}},
# )

# TODO: put item ~ Create new item

# with more than 1 attribute
# response = client.put_item(
#     TableName="student",
#     Item={"student_id": {"N": "10"}, "name": {"S": "Trevor"},
#           "age": {"N": "41"}, "gender": {"S": "M"}}
# )

# with less than 1 attribute
# response = client.put_item(
#     TableName="student",
#     Item={"student_id": {"N": "12"}, "name": {"S": "John"}}
# )

# TODO: update item
"""
Trong khi update item có thể thêm luôn attribute mới vào
"""
# response = client.update_item(
#     TableName='student',
#     Key={"student_id": {"N": "2"}},
#     AttributeUpdates={"height": {"Value": {"N": "1.6"}, "Action": "PUT"}}
# )
