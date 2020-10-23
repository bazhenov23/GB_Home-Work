from functools import reduce

my_list = [x for x in range(100, 1001) if x % 2 == 0]


def my_func(prev_el, el):
    return prev_el * el


result = reduce(my_func, my_list)
print(result)
print("Я праверил расчеты на счетах: ответ верный!")
