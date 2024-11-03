from pathlib import Path
from gmail_api import init_gmail_service, download_attachments_parent, download_attachments_all

client_file = 'client_secret.json'
service = init_gmail_service(client_file)

user_id = 'me'
msg_id = '<message_id>'
download_dir = Path('./downloads')

download_attachments_parent(service, user_id, msg_id, download_dir)
# download_attachments_all(service, user_id, msg_id, download_dir)
