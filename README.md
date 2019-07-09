Instructions

Architecture

Events -> Amazon SNS -> AWS Lambda -> Telegram

Create a Telegram bot http://t.me/botfather

Create an SNS Topic or use an exist

Create a Lambda Function

Create environment variables in the Lambda Function

BOT_ID = Your Telegram BOT ID. Example: 123456789:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
CHAT_ID = Is your channel ID or your BOT chat window id

Paste the code TelegramNotifier.py in the Function code

Add SNS trigger

Test publishing a message