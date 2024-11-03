from gmail_api import init_gmail_service, create_label, list_labels, modify_label, delete_label, get_label_details

client_file = 'client_secret.json'
service = init_gmail_service(client_file)

# iterate over the labels list and create each label
labels = ['Client Projects', 'Shopping', 'Free Movies', 'Personal', 'Patreon']
labels_patreon = ['Posts', 'News Letter', 'Promotions']
created_labels = []

for label in labels:
    try:
        label = create_label(service, label)
        created_labels.append(label)
        if label['name'] == 'Patreon':
            patreon_label_id = label['id']
            for sub_label in labels_patreon:
                print('creating sub label', f'{label['name']}/{sub_label}')
                create_label(service, f'{label['name']}/{sub_label}')
    except Exception as e:
        print(f'Label creation failed for "{label}": {e.reason}')

# list all labels
gmail_labels = list_labels(service)
for gmail_label in gmail_labels:
    print(gmail_label)
    print('-' * 50)

# get details of a specific label
get_label_details(service, created_labels[0]['id'])

# modify the label
modify_label(service, created_labels[0]['id'], name='Misc', color={'textColor': '#eaa041', 'backgroundColor': '#285bac'})
modify_label(service, created_labels[1]['id'], color={'textColor': '#7a2e0b', 'backgroundColor': '#7a2e0b'})

# delete the label
labels_to_delete = list_labels(service)
for label_ in labels_to_delete:
    if label_['type'] == 'user':
        delete_label(service, label_['id'])
        print(f"Deleted label: {label_['name']}")