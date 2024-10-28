import requests
import json

get_response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'Rahul Shetty2'})

# response_string = get_response.text
# print(response_string)
#
# print("Type of response: ",type(response_string))
#
# dict_response = json.loads(response_string)
# print(type(dict_response))
#
# print(dict_response[0]['isbn'])


response_json = get_response.json()
print(response_json[0]['isbn'])

assert get_response.status_code == 200

print("Headers ", get_response.headers)

assert get_response.headers['Content-Type'] == 'application/json;charset=UTF-8'

print('Cookies: ', get_response.cookies)


