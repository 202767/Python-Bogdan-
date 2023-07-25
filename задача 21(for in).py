dict = {'name': 'Anna',
        'age': 20,
        'country': 'Russia'}

new_dict = {key.upper(): value for key, value in dict.items()}

print(new_dict)
print(dict)
