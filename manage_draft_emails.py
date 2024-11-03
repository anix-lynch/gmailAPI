from pathlib import Path
from gmail_api import init_gmail_service, list_draft_email_messages, create_draft_email, \
                      get_draft_email_message_details, send_draft_email, delete_draft_email

# Create the Gmail API service
client_file = 'client_secret.json'
service = init_gmail_service(client_file)

# create a draft email
to_address = 'datadummyacct@gmail.com'
email_subject = 'Test Email Draft API'
email_body = 'This is a test email draft created using the Gmail API.'

attachment_dir = Path('./attachments')
attachment_files = list(attachment_dir.glob('*'))

response_draft_email = create_draft_email(
    service,
    to_address, 
    email_subject, 
    email_body, 
    body_type='plain',
    attachment_paths=attachment_files
)
print(response_draft_email)

# List draft email
drafts = list_draft_email_messages(service)

for draft in drafts:
    draft_detail = get_draft_email_message_details(service, draft['id'])
    print(draft_detail)

# send draft email
for draft in drafts:
    draft_detail = get_draft_email_message_details(service, draft['id'])
    send_draft_email(service, draft['id'])
    print(f"Draft email '{draft_detail['subject']}' sent successfully.")

# Delete Draft Email
drafts = list_draft_email_messages(service)
for draft in drafts:
    delete_draft_email(service, draft['id'])
    print(f"Draft email '{draft['id']}' deleted successfully.")