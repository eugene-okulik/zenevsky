number = 46
while True:
    user_input = (input('Введите загаданное число: '))
    if user_input.isnumeric():
        if int(user_input) == number:
            print('Поздравляю! Вы угадали!')
            break
        print('Попробуйте снова')
    else:
        print('Вы ввели не число!')
