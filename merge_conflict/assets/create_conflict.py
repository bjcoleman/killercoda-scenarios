import requests
import json


url = 'https://obdgyysqtjcbxqvwuhepgruqmq0lufey.lambda-url.us-east-1.on.aws/'

with open('/root/repo_name') as f:
    repo_name = f.read().strip()

json_data = {'repo_name': repo_name}

result = requests.post(url, json=json_data)
