import requests
from utilities.configurations import *
from utilities.resources import *
from payload import *


print("************ Adding the Book ************")
post_url = getConfig()['API']['endpoint']+APIresources.addBook
headers = {'Content-Type':'application/json'}
Addbook_Response = requests.post(post_url,json=addBookPayload('abcd'),headers=headers)

assert Addbook_Response.status_code == 200
print(Addbook_Response.json())

bookID = Addbook_Response.json()['ID']

print("************ Deleting the Book ************")
delete_url = getConfig()['API']['endpoint']+APIresources.deleteBook
delete_Response = requests.post(delete_url,json={"ID":bookID})
print(delete_Response.json())
assert delete_Response.status_code == 200






