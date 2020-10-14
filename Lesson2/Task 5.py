my_list = [9, 7, 5, 3, 3, 2]
print(*my_list)
result_list = int(input("Введите число (111 - выход) "))

while result_list != 111:
    for el in range(len(my_list)):
        if my_list[el] == result_list:
            my_list.insert(el + 1, result_list)
            break
        elif my_list[0] < result_list:
            my_list.insert(0, result_list)
            break
        elif my_list[-1] > result_list:
            my_list.append(result_list)
            break
        elif my_list[el] > result_list > my_list[el + 1]:
            my_list.insert(el + 1, result_list)
            break
    my_list.pop(6)

    print(*my_list)
    result_list = int(input("Введите число "))
