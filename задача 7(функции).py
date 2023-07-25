def merge_list_to_dict(list_one, list_two):
    new_zip = zip(list_one, list_two)
    new_dict = dict(new_zip)
    return (new_dict)


list_one = ['asd', 23, True]
list_two = [1 + 4j, 2.5, ('sfsv', 'wsvs')]

print(merge_list_to_dict(list_one, list_two))
