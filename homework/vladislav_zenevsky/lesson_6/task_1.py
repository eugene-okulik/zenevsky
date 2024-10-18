original_text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)

new_text = []
for word in original_text.split():
    if word.endswith(','):
        word = word.strip(',')
        new_text.append(f'{word}ing,')
    elif word.endswith('.'):
        word = word.strip('.')
        new_text.append(f'{word}ing.')
    else:
        new_text.append(f'{word}ing')
print(' '.join(new_text))
