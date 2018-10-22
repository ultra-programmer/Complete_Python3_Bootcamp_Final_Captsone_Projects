"""
Check if a phrase is a palindrome
"""
def check_palindrome(input_string):
    '''
    Palindrome checker
    '''
    reversed_words = []
    if len(input_string.split()) == 1:
        return input_string[::-1].lower() == input_string.lower()
    else:
        for word in input_string.split():
            reversed_words.append(word[::-1])

        return ''.join(reversed_words[::-1]).lower() == ''.join(input_string.split()).lower()

while True:
    try:
        STRING = input('Phrase to be checked for palindrome: ')
        if len(STRING) < 1:
            raise RuntimeError
    except RuntimeError:
        print('Please enter a phrase to be checked for palindrome!\n')
        continue
    else:
        break

def main():
    '''
    Wrapper function
    '''
    if check_palindrome(STRING):
        print(f'{STRING.capitalize()} is a palindrome.')
    else:
        print(f'{STRING.capitalize()} is not a palindrome.')

if __name__ == '__main__':
    main()
