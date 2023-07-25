def filter_list(my_list, type_of_list):
    result = []
    for item in my_list:
        if type(item) == type_of_list:
            result.append(item)
    return result


my_list = filter_list([True, 'abc', 15, 25], int)
print(my_list)
