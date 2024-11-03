from gmail_api import init_gmail_service, search_emails, modify_email_labels, get_email_message_details, map_label_name_to_id

client_file = 'client_secret.json'
service = init_gmail_service(client_file)

query = 'from:patreon'
email_messages = search_emails(service, query, max_results=5)
patreon_label_id = map_label_name_to_id(service, 'Patreon')

# add label "Patreon" to emails
for email_message in email_messages:
    email_message_detail = get_email_message_details(service, email_message['id'])
    if 'no-reply@patreon.com' in email_message_detail['sender']:
        modify_email_labels(service, 'me', email_message['id'], add_labels=[patreon_label_id, 'STARRED'])
        print(f"Adding 'Patreon' label to email: {email_message_detail['subject']}")
    
# remove label "Patreon" from emails
for email_message_ in email_messages:
    email_message_detail_ = get_email_message_details(service, email_message_['id'])
    if 'no-reply@patreon.com' in email_message_detail_['sender']:
        modify_email_labels(service, 'me', email_message_['id'], remove_labels=[patreon_label_id, 'STARRED'])
        print(f"Removing 'Patreon' label from email: {email_message_detail_['subject']}")

