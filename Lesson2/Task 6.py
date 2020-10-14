goods = []
features = {'Наименование': '', 'Цена': '', 'Количество': '', 'Еденицы измерения': ''}
analytics = {'Наименование': [], 'Цена': [], 'Количество': [], 'Еденицы измерения': []}
n = 0
feature_ = None
control = None
while True:
    control = input("Для ввода информации нажмите 'Enter', для вывода информации нажмите '111'").upper()
    n += 1
    if control == '111':
        print(f'\n Текущая информация \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Укажите {f} товара №{n}: ')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((n, features))

