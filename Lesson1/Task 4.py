numb = abs(int(input("Введите целое положительное число ")))
max = numb % 10
while numb >= 1:
    n = numb // 10
    if numb % 10 > max:
        max = numb % 10
    if numb > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break
