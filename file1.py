import json

a = {
    'name': 'Ram',
    'course': 'django'
}

print(type(a))

b = json.dumps(a)
print(b)

print(type(b))

l1 = json.loads(b)
print(type(l1))
print(l1)


f = open('msg.json', 'w')
f.write(b)

with open('msg.json', 'r') as f:
    b = json.load(f)
    print(b)
    print(type(b))