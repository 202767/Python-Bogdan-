def dict_to_list(dict):
    result = []
    for key, value in dict.items():
        if isinstance(value, int):
            value *= 2
        result.append((key, value))
    return result


my_dict = {'name': 'Ann',
           'age': 20,
           'country': 'Russia'}
my_list = dict_to_list(my_dict)
print(my_list)
