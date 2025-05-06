import sys
import time

import requests

sys.set_int_max_str_digits(100000)


def fibonacci_generator():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


max_index = 100000

i = 1
for number in fibonacci_generator():
    if i <= max_index:
        print(number)
        requests.get('https://www.ya.ru')
        time.sleep(5)
    if i > max_index:
        break
    i += 1
