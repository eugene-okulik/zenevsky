def repeater(func):
    def wrapper(*args, count):
        result = list(map(lambda x: func(*args), range(count)))
        return result

    return wrapper


@repeater
def simple_function(text):
    print(text)


@repeater
def another_simple_function(a, b):
    c = a * b
    print(c)


simple_function('print me', count=2)
another_simple_function(2, 3, count=4)
