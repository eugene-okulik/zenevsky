original_text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)

new_text = []
for word in original_text.split():
    if word.endswith(','):
        new_text.append(f'{word.strip(',')}ing,')
    elif word.endswith('.'):
        new_text.append(f'{word.strip('.')}ing.')
    else:
        new_text.append(f'{word}ing')
print(' '.join(new_text))
