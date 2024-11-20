def calc_decorator(func):
    def wrapper(first, second, operation):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        if first < 0 or second < 0:
            operation = '*'
        return func(first, second, operation)

    return wrapper


@calc_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


entered_first = int(input('First number: '))
entered_second = int(input('Second number: '))
entered_operation = input('Operation: ')

print(calc(entered_first, entered_second, entered_operation))
