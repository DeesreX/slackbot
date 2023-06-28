import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Initialize the Slack client
token = "xapp-1-A05EY4CRC9F-5508150684449-6b01d55fe14e37396538ba8db7d666752efcc68961dc2df3e37ddd76c82cff7c"
client = WebClient(token=token)

def send_message(channel, message):
    try:
        response = client.chat_postMessage(channel=channel, text=message)
        print("Message sent successfully")
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")

def read_messages(channel):
    try:
        response = client.conversations_history(channel=channel)
        messages = response["messages"]
        for message in messages:
            print(f"{message['user']}: {message['text']}")
    except SlackApiError as e:
        print(f"Error reading messages: {e.response['error']}")

# Example usage
send_message("#general", "Hello, Slack!")
read_messages("#general")
