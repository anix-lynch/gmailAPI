from pathlib import Path
from google_apis import create_service
from gmail_api import init_gmail_service, create_draft_email

# Create the Gmail API service
client_file = 'client_secret.json'
service = create_service(client_file)

to_address = '<recipient email address>'
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