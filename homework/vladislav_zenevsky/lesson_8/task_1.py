import random


def take_your_money():
    salary = int(input('Please enter your salary: '))
    bonus = random.choice([True, False])
    if bonus:
        salary += random.randrange(1, 10000)
    return f'${salary}'


print(take_your_money())
