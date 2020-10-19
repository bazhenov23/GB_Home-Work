def info():
    name = input("Введите имя ")
    surname = input("Введите фамилию ")
    year = int(input("Введите год рождения "))
    city = input("Введите город ")
    email = input("Введите адрес электронной почты ")
    telephone = input("Введите номер телефона ")
    info_user = (
        f"Пользователь {name} {surname}   Год рождения {year}   Город {city}   Электорнный адрес {email}   Телефон {telephone}")
    return info_user


user = info()
print(user)
