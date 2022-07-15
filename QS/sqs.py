import queue
import boto3

sqs = boto3.resource('sqs')

# Create the queue
# queue = sqs.create_queue(QueueName='test-3')
# print(queue.url)
# print(queue.attributes)

# Use an existing queue
# queue = sqs.get_queue_by_name(QueueName='test')
# print(queue.url)

# List all available queues
# for q in sqs.queues.all():
#     print(q.url)

# Send message to a queue
# queue = sqs.get_queue_by_name(QueueName='test-3')
# queue.send_message(MessageBody='Hello World!')

# Send bulk messages to queue
# queue = sqs.get_queue_by_name(QueueName="test")
# count = 0
# messages = []
# for i in range(0, 5):
#     messages.append({
#         "Id": str(count),
#         "MessageBody": f"Another ordir is in {count}"
#     })
#     count += 1

# queue.send_messages(Entries=messages)


# Read Messages
queue = sqs.get_queue_by_name(QueueName="test")
for message in queue.receive_messages(
    AttributeNames=["All"],
    MaxNumberOfMessages=10,
):
    print(message.body)
    message.delete()
