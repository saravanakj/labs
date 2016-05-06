import requests

# Set the request parameters
url = 'https://server/api/controller/action/'
headers = {'Authorization':'token abcd', 'Content-Type':'application/json'}

response = requests.get(url,headers=headers)
print(response.status_code)
