import requests

se = requests.session()
se.auth = ('Katasraj','Katasraj111#')

#url = 'https://api.github.com/user/repos'
url = 'https://github.com/'
response = se.get(url)
print(response.status_code)