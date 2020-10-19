def my_func():
    x = int(input("Введите положительное число "))
    y = int(input("Введите степень (целое отрицательное числ) "))
    if y >= 0:
        print("Вы ввели положительное число, попробуйте еще раз")
        exit()
    result = x ** y
    return result


user_result = my_func()
print(user_result)
