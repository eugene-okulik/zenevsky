string_1 = 'результат операции: 42'
string_2 = 'результат операции: 514'
string_3 = 'результат работы программы: 9'

result_1 = int(string_1[string_1.index(':') + 2:]) + 10
result_2 = int(string_2[string_2.index(':') + 2:]) + 10
result_3 = int(string_3[string_3.index(':') + 2:]) + 10

print(result_1, result_2, result_3)
