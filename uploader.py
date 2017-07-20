import requests

filename = 'foundFaces.png'
url = 'https://3hu6o5otw7.execute-api.us-east-1.amazonaws.com/dev/upload'
files = {'file': open(filename, 'rb')}

response = requests.request('POST', url, files=files)

print(response.text)

if(response.status_code == 200):
    payload = '{\"location\": \"officeMac\"}'
    url = 'https://3hu6o5otw7.execute-api.us-east-1.amazonaws.com/dev/suspects/' + filename
    headers = {
    'content-type': 'application/json'
    }
    response = requests.request('PUT', url, data=payload, headers=headers)
    print(response.text)

print('done')
