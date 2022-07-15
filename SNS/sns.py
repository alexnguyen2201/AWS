import boto3

sns = boto3.client('sns')

# Create a new topic
# response = sns.create_topic(Name='demo_youtube_topic')
# print(response)

# List all topic
# response = sns.list_topics()
# print(response["Topics"])

# Public to topic
DEMO_YOUTUBE_TEST_TOPIC_SNS_ARN = 'arn:aws:sns:ap-southeast-1:913277152798:demo_youtube_topic'
for i in range(100):
    print(f"Publishing message: {i}")
    sns.publish(
        TopicArn=DEMO_YOUTUBE_TEST_TOPIC_SNS_ARN, Message=f"Hello World!, {i}"
    )
