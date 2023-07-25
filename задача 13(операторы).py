my_name = 'Bogdan'
my_hobby = 'Running'
time = 8
periodicity = 'Week'
# info = my_name + ' likes ' + my_hobby + ' at ' + str(time) + " o'clock"
info = f"{my_name} Likes {my_hobby} At {str(time)} O\'clock"

info_new = f"{my_name} Was {my_hobby} {time} Times A {periodicity}"

print(info)
print(info_new)
