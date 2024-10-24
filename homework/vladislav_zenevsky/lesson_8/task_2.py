import sys

sys.set_int_max_str_digits(100000)


def fibonacci_generator():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


indices_to_print = [5, 200, 1000, 100000]

i = 1
for number in fibonacci_generator():
    if i in indices_to_print:
        print(number)
    if i > max(indices_to_print):
        break
    i += 1
