second_original = int(input("Введи количество для расчета времени: "))

hour = second_original // 3600
minute = (second_original - 3600 * hour) // 60
second = second_original - (3600 * hour) - (60 * minute)

print(f"Как-то так: {hour:02}:{minute:02}:{second:02}")
