import requests
from behave import given, when, then
from apiValidation1 import response_json
from postAPI import Addbook_Response
from utilities.resources import *
from payload import *


@given('The book details which needs to be added to Library')
def step_implementation():
    print("************ Adding the Book ************")
    post_url = getConfig()['API']['endpoint'] + APIresources.addBook
    headers = {'Content-Type': 'application/json'}
    query = 'select * from Books'

    assert Addbook_Response.status_code == 200


@when('we execute the addbook postAPI method')
def step_impl(context):
    Addbook_Response = requests.post(post_url, json=buildPayloadFromDB(query), headers=headers)


@then('book is successfully added')
def step_impl(context):
    print(Addbook_Response.json())
    bookID = Addbook_Response.json()['ID']
    print(bookID)
    assert response_json["Msg"] == 'successfully added'

