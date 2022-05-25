import requests
import json


print('Creating a repo for us to use in the scenario...')
url = 'https://lfvvlgcpn8.execute-api.us-east-1.amazonaws.com/prod/create_repo'
result = requests.get(url)


print('\n\nSuccess!!\n\n')

body = result.json()['body']
data = json.loads(body)

repo_name = data['repo_name']
repo_url = data['repo_url'].replace('.git', '')

with open('/root/repo_name', 'w') as f:
    f.write(repo_name)

print('Your repo is named {}.'.format(repo_name))
print('You can access your repo at {}'.format(repo_url))
