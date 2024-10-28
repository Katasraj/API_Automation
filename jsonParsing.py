import json

courses = '{"name":"RahulShetty", "languages":["Java", "Python"]}'

''' Loads method parse json string and it returns dictonary'''
dict_courses = json.loads(courses)

print(dict_courses)
#print(type(dict_courses))

dict_courses['languages'].append('CPP')
print(dict_courses)

print()
print("************************ Parse Content from json file ************************")

with open('sample1.json', 'r') as f:
    data = json.load(f)

print(data)
print(data['quiz']['maths']['q1']['options'])
print(data['quiz']['maths']['q2']['options'])
print(data['quiz']['maths']['q2']['answer'])

data['quiz']['maths']['q2']['answer'] = 9
print(data)
