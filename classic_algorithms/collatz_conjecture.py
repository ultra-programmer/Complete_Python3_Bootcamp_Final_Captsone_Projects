"""
The Collatz Conjecture is an algorithm that turns any number into 1 using the following steps:
  If the number is even divide it by 2
  If the number is ood multiply it by 3 and add 1
"""
def collatz_conjecture(n):
    '''
    Collatz Conjecture
    '''
    count = 0

    while n != 1:
        if n % 2 == 0:
            n /= 2
            count += 1
        else:
            n = n * 3 + 1
            count += 1

    return count

def main():
    '''
    Wrapper Function
    '''
    while True:
        try:
            NUMBER = int(input('Collatz Conjecture on: '))
            if NUMBER < 2:
                raise RuntimeError
        except RuntimeError:
            print('Please give an integer greater than 1!\n')
            continue
        except ValueError:
            print('Please give an integer!\n')
            continue
        else:
            break
    print(f'It takes {collatz_conjecture(NUMBER)} steps to turn your number into 1 using the Collatz Conjecture!')
        
if __name__ == '__main__':
    main()
