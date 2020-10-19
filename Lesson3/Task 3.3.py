def my_func():
    x = int(input("Первое число "))
    y = int(input("Второе число "))
    z = int(input("Третье число "))

    if x >= z and y >= z:
        result = x + y
    elif y < x < z:
        result = x + z
    else:
        result = y + z
    return result


user_result = my_func()
print(user_result)
