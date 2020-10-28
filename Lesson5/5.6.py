"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней
прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами
и их прибылями, а также словарь со средней прибылью. Если фирма получила
убытки, также добавить ее в словарь (со значением убытков).
"""

import json

profit_list = {}
average_profit_list = {}
profit = 0
average_profit = 0
i = 0

with open('text6.txt', 'r') as file:
    for line in file:
        name, org, earning, damage = line.split()
        profit_list[name] = int(earning) - int(damage)
        if profit_list.setdefault(name) >= 0:
            profit = profit + profit_list.setdefault(name)
            i += 1
    if i != 0:
        average_profit = profit / i
    else:
        print(f'Все компании работают в убыток')

    average_profit_list = {'Average_profit': round(average_profit)}
    profit_list.update(average_profit_list)
    print(f'\nПрибыльные компании - {profit_list}\n')

with open('text6.json', 'w') as write_js:
    json.dump(profit_list, write_js)

    js_str = json.dumps(profit_list)
    print(js_str)
