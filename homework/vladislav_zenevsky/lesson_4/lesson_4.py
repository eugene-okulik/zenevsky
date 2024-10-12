my_dict = {
    'tuple': (1, 2.5, 'text', True, None, 'last'),
    'list': ['', 2, 9.9, 52, 'test'],
    'dict': {
        'id': 999,
        'first_name': 'Vlad',
        'last_name': 'Zen',
        'age': 29,
        'test': True
    },
    'set': {'qa', 'auto', 5, 25, 11}
}

print(my_dict['tuple'][-1])
my_dict['list'].append(111)
my_dict['list'].pop(1)
my_dict['dict'][('i am a tuple',)] = 'you can trust me'
my_dict['dict'].pop('test')
my_dict['set'].add(100)
my_dict['set'].remove('qa')

print(my_dict)
