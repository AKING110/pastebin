# Code By AKING
# Pastebin api: https://pastebin.com/api
import requests

api_key = 'jewD-SVI_6YcrQ_RW45qq_-rEw0iiqis'
text_to_upload = 'This is the text I want to upload to Pastebin.'
#file_to_uplaod = open('/sdcard/XD.py','r').read()
url = 'https://pastebin.com/api/api_post.php'

data = {
    'api_dev_key': api_key,
    'api_option': 'paste',
    'api_paste_code': text_to_upload,
    'api_paste_private': '1',
    'api_paste_expire_date': 'N',
}

response = requests.post(url, data=data)

if response.status_code == 200:
    paste_url = response.text
    print(f'Paste created successfully: {paste_url}')
else:
    print('Error creating paste:', response.text)
