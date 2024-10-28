'''
Send and Manage Cookies and Sending Attachments in API
https://httpbin.org/#/Cookies
'''

import requests

cookie = {'visit-month':'February'}
res = requests.get('http://rahulshettyacademy.com/',allow_redirects=False,cookies=cookie,timeout=5)
print(res.history)
print(res.status_code)

se = requests.session()
se.cookies.update({'visit-month':'February'})


res_cook = se.get('https://httpbin.org/cookies',cookies={'visit-year':'2022'})
print(res_cook.text)


print()
print('*********************** Attachments ***********************')
url = 'https://petstore.swagger.io/v2/pet/9843217/uploadImage'
files = {'file':open('/Users/nagamuralikotari/Desktop/PS/sw.png','rb')}
post_res = requests.post(url,files=files)
print(post_res.status_code)
print(post_res.text)
