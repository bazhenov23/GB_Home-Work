"""
Создать класс TrafficLight (светофор) и определить у него один
атрибут color (цвет) и метод running (запуск). Атрибут реализовать
как приватный. В рамках метода реализовать переключение светофора
в режимы: красный, желтый, зеленый.
"""

from time import sleep


class TrafficLight:
    _color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'{TrafficLight._color[i]}')
            if i == 0:
                sleep(3)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(1)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
