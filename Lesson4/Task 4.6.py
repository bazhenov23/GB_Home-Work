from itertools import cycle

number = int(input("Введите первое число списка "))
my_list = [x for x in range(number, number + 10)]
print(my_list)

count = 1
for y in cycle(my_list):
    if count > 1:
        break
    print(my_list)
    count += 1
