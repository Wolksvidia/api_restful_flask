items = []

items.append({'name': 'algo'})
items.append({'name': 'algo2'})
items.append({'name': 'algo3'})
items.append({'name': 'algo4'})
items.append({'name': 'algo5'})
items.append({'name': 'algo6'})
items.append({'name': 'algo7'})


item = next(filter(lambda i: i['name'] == 'algo3', items), None)
print(type(item))

item.update({'name': 'algo3++'})

print(item)

print(items)