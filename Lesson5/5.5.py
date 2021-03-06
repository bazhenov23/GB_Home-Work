"""
Необходимо создать (не программно) текстовый файл, где
каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их
количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название
предмета и общее количество занятий по нему. Вывести словарь на экран.
"""

schedule = {}
with open('text5.txt', 'r') as abc:
    for line in abc:
        subject, a, b, c = line.split()
        schedule[subject] = int(a) + int(b) + int(c)
    print(f'Общее количество часов по предмету - \n {schedule}')
