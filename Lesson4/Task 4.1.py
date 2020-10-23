from sys import argv

try:
    user, time_work, salary, bonus = argv
    result = (int(time_work) * int(salary)) + int(bonus)
    print(f"Заработная плата сотрудника составляет {result}")
except ValueError:
    print("Not a number")

