my_list = [i * j for i in range(2, 7) for j in range(2, 7)]
new_list = [el for el in my_list if my_list.count(el) < 2]

print(f'Исходный список {my_list}')
print(f'Новый список {new_list}')

