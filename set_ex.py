cities = {'Las Vegas', 'Paris', 'Moscow'}
print(cities)

cities.add('Burma')
print(cities)

cities.remove('Moscow')
print(cities)
print(len(cities))
print('Paris' in cities)

for city in cities:
    print(city)