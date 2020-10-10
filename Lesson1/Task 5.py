profit = float(input("Введите выручку компании "))
cost = float(input("Введите издержки компании "))
if profit > cost:
    print(f"Компания работает с прибылью. Рентабельность выручки составила {profit / cost:.1f}%")
    workers = int(input("Введите количество сотрудников "))
    print(f"Прибыль в расчете на одного сторудника сотавила {profit / workers:.1f}")
elif profit == cost:
    print("Компания работает в ноль")
else:
    print("Компания работает в минус")
