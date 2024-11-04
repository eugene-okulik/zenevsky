def finish_log(func):
    def wrapper(*args):
        result = func(*args)
        print('finished')
        return result

    return wrapper


@finish_log
def simple_function():
    print('text')


@finish_log
def another_simple_function(x):
    y = x * 2
    print(y)


simple_function()
another_simple_function(2)
