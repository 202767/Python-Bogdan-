while True:
    first_num = int(input("Print first num: "))
    second_num = int(input("Print second num: "))
    if second_num != 0:
        print(first_num / second_num)
    else:
        print("Can't be divide by 0 ")
    answer = input("Do you want to continue? ")
    if answer == 'yes':
        continue
    break
