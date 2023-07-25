def filter_list(list_to_filter, value_type):
    return list(filter(lambda elem: type(elem) is value_type,
                       list_to_filter))


res = filter_list([1, 10, 'abc', True, 5.5], int)
print(res)
