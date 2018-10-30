"""
Convert decimal numbers to binary, and binary numbers to decimal
"""
def binary_and_decimal(num, binary=True):
    '''
    Convert num into either binary or decimal
    '''
    if binary:
        # Return the number converted into binary
        return bin(num)[2:]
    else:
        # Return the number converted into a decimal from a number in binary
        return int(str(num), 2)

def main():
    '''
    Wrapper function
    '''
    while True:
        try:
            number = int(input('What integer would you like to convert to binary or decimal? '))
            if number < 0:
                raise ValueError

            what_to_convert = input('Would you like to convert that integer into binary or decimal? ')
            if not what_to_convert in ['binary', 'decimal']:
                raise RuntimeError
        except RuntimeError:
            print('I\'m sorry! You must provide either binary or decimal. Please try again!\n')
            continue
        except ValueError:
            print('I\'m sorry! You must give a positive integer. Please try again!\n')
            continue
        else:
            break

    if what_to_convert == 'binary':
        print(f'Your number in {what_to_convert} is {binary_and_decimal(number)}.')
    else:
        print(f'Your number in {what_to_convert} is {binary_and_decimal(number, False)}.')

if __name__ == '__main__':
    while True:
        main()
        again = input('Would you like to convert another number? (y/n)\n')
        if again == 'y':
            continue
        else:
            break
