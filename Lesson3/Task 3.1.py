def division():
    x = int(input("Введите первое число "))
    y = int(input("Введите второе число "))
    if not y != 0:
        print("Делить на ноль нельзя")
        exit()

    division_xy = x / y
    return division_xy


result = division()
print(result)
