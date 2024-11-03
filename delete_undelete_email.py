from gmail_api import init_gmail_service, search_emails, get_email_message_details, trash_email, \
                      batch_trash_emails, untrash_email, modify_email_labels, empty_trash

client_file = 'client_secret.json'
service = init_gmail_service(client_file)

# Gives you the flexibility to add more layers to filter emails
query='From:me'
email_messages = search_emails(service, query, max_results=5)
for email_message in email_messages:
    email_message_detail = get_email_message_details(service, email_message['id'])
    trash_email(service, 'me', email_message['id'])
    print(f'Email "{email_message_detail['subject']}" moved to trash.')

# untrash
query='in:trash'
email_messages = search_emails(service, query, max_results=100)
for email_message in email_messages:
    email_message_detail = get_email_message_details(service, email_message['id'])
    print(f'Email "{email_message_detail['subject']}" will be moved to inbox.')
    untrash_email(service, 'me', email_message['id'])
    # reattach inbox label
    modify_email_labels(service, 'me', email_message['id'], add_labels=['INBOX'])

# batch delete
target_emails = []
query='Subject:Resource File"'
email_messages = search_emails(service, query, max_results=5)
for email_message in email_messages:
    email_message_detail = get_email_message_details(service, email_message['id'])
    print(f'Email "{email_message_detail['subject']}" will be moved to trash.')
    target_emails.append(email_message['id'])

batch_trash_emails(service, 'me', target_emails)

# empty trash folder
empty_trash(service)