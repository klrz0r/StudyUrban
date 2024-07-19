my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
length_my_list = len(my_list)
while index < length_my_list:
    if my_list[index] == 0:
        index += 1
        continue
    if my_list[index] > 0:
        print (my_list[index])
        index += 1
    else:
        break
