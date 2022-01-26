from re import T


friend = {
    'name' : 'Max',
    'age' : 23,
    'has_car' : True
}

for key in friend:
    print(friend[key])

for item in friend.items():
    print(item)

for key, val in friend.items():
    print(key)
    print(val)