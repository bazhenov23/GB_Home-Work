first_run = int(input("Сколько пробежали в первый день в км "))
runs_all = int(input("Общая протяженность пути в км "))
result_days = 1
result_km = first_run

while result_km < runs_all:
        first_run = first_run + 0.1 * first_run
        result_days += 1
        result_km = result_km + first_run

print(f"Вы достигнете требуемых показателей на %.d день" % result_days)




