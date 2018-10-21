"""
Pig Latin!
"""
while True:
    try:
        STRING = input('Please enter the word to be translated into pig latin: ')
        if len(STRING.split()) > 1:
            raise RuntimeError
        elif len(STRING.split()) < 1:
            raise RuntimeError
    except RuntimeError:
        print('Please enter a word to be reversed\n')
        continue
    else:
        break

if STRING[0].lower() in ['a', 'e', 'i', 'o', 'u']:
    print(f'Your word in pig latin is: {STRING}-ay')
else:
    print(f'Your word in pig latin is: {STRING[1::]}-{STRING[0]}ay')
