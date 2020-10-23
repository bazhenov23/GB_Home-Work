from itertools import count
from math import factorial


def fgen():
    for i in count(1):
        yield factorial(i)


generator = fgen()
x = 0
for k in generator:
    if x < 5:
        print(k)
        x += 1
    else:
        break
