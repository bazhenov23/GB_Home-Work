"""
Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""
salary = []
poor = []
with open('text3.txt', 'r') as my_file:
    my_list = my_file.readlines()
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
    salary.append(i[1])

print(f'Оклад меньше 20.000 {poor}.\nCредний оклад {sum(map(int, salary)) / len(salary)}')
my_file.close()
