list_of_dict = [{'name': 'Valya',
                 'surname': 'Ivanova'},
                {'age': 3,
                 'sex': 'female'},
                {'job': 'accountant',
                 'country': 'Russia'}]

name_dict, age_dict, job_dict = list_of_dict


def dict_unpack(first, second):
    return print(first, second)


print(dict_unpack(first=name_dict['name'], second=name_dict['surname']))
print(dict_unpack(first=age_dict['age'], second=age_dict['sex']))
print(dict_unpack(first=job_dict['job'], second=job_dict['country']))
