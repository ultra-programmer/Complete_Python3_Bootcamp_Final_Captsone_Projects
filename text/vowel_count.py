"""
Ever wonder how many vowels are in a sentence?
Not me, but maybe you are...
"""
VOWEL_COUNT = 0
VOWELS = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

while True:
    try:
        STRING = input('Give the sentence you want me to count the vowels of: ')
        if len(STRING) < 1:
            raise RuntimeError
    except RuntimeError:
        print('I\'m sorry! You must give a sentence. Please try again!\n')
        continue
    else:
        break

for char in STRING:
    for letter in VOWELS:
        if char.lower() == letter:
            VOWELS[letter] += 1

    if char.lower() in VOWELS:
        VOWEL_COUNT += 1

print(f'The total number of vowels in your sentence are {VOWEL_COUNT}.')
print('Here are the amount of each vowel in your sentence: ')
for letter in VOWELS:
    print(f'\t{letter.upper()}: {VOWELS[letter]}')
