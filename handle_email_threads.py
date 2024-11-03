from gmail_api import init_gmail_service, get_email_messages, get_message_and_replies, _extract_body

# Create the Gmail API service
client_file = 'client_secret.json'
service = init_gmail_service(client_file)

email_messages = get_email_messages(service, max_results=1)
message_id = email_messages[0]['id']

message_chain = get_message_and_replies(service, message_id)
for message in message_chain:
    print('subject:', message['subject'])
    print('body:', message['body'])
    print('date:', message['date'])
    print('-' * 50)