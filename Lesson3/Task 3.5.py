def my_sum():
    sum_res = 0
    ex = False
    while not ex:
        number = input("Введите ряд чисел или нажмите Q для выхода ").split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f"Промежуточный результат {sum_res}")
    print(f"Финальный итог {sum_res}")


my_sum()
