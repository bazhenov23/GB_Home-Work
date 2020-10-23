from random import shuffle

my_list = [i * j for i in range(2, 5) for j in range(4, 7)]
print(f'Исходный список {my_list}')
shuffle(my_list)
new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {new_list}')

