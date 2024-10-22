string_1 = 'результат операции: 42'
string_2 = 'результат операции: 54'
string_3 = 'результат работы программы: 209'
string_4 = 'результат: 2'


def simple_function(*args):
    for i in args:
        print((int(i[i.index(':') + 2:]) + 10))


simple_function(string_1, string_2, string_3, string_4)
