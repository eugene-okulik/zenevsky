words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for word, qty in words.items():
    printed_word = ''
    i = 0
    while i < qty:
        printed_word += word
        i += 1
    print(printed_word)
