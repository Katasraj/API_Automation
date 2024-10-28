import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'Rahul Shetty'})

print(type(response.json()))

for i in range(len(response.json())):
    if response.json()[i]['isbn'] == 'RS11':
        print(response.json()[i])


for actualbook in response.json():
    if actualbook["isbn"] == "RS1000":
        print("Actual Book: ",actualbook)
        break

expected_book = {"book_name": "Learn Appium Automation with Java", "isbn": "RS1000", "aisle": "2223"}


assert actualbook == expected_book