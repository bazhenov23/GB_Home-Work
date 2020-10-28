"""
Создать (программно) текстовый файл, записать в
него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле
и выводить ее на экран.
"""


def summary():
    try:
        with open('text4.txt', 'w+') as file_obj:
            line = input('Введите числа для определения их суммы через пробел:\n')
            file_obj.writelines(line)
            numbers = line.split()
            print(f"Сумма чисел: {sum(map(int, numbers))}")
    except IOError:
        print('Какая-то ошибка')
    except ValueError:
        print('Внимательно читайте условия!')


summary()
