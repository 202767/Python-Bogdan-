from sys import getsizeof
squares_gen = (num*num for num in range(10000))
print(getsizeof(squares_gen))
print(type(squares_gen))

for num in squares_gen:
    print(num)
    if num == 100:
        break

squares_list = [num*num for num in range(10000)]

print(getsizeof(squares_list))
print(type(squares_list))
