import json

with open('sample1.json', 'r') as f1:
    data1 = json.load(f1)


with open('sample2.json', 'r') as f2:
    data2 = json.load(f2)

assert data1==data2
