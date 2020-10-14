r_list = [23, 'text', 456, 45.3, None]
n = 0
while n < len(r_list):
    print(f"{r_list[n]} - {type(r_list[n])}".replace('<class ', '').replace('>', ''))
    n += 1

