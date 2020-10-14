quantity = int(input("Укажите количество элементов списка "))
my_list = []

i = 0
while i < quantity:
    my_list.append(input(f"Введите элемент №{i + 1}: "))
    i += 1

n = 0
for el in range(int(len(my_list) / 2)):
    my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]
    n += 2

print(my_list)
