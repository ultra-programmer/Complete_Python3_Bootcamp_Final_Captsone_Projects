'''
Print Primes
Generates prime numbers up to an input limit.
'''
def check_prime(num):
    '''
    Checks if num is prime
    '''

    # We know 1 and 2 are prime, so if num is 1 or 2 return True
    if num == 2 or num == 1:
        return True

    # If the number is even, return False
    if num % 2 == 0:
        return False

    # Apply sieve of Eratosthenes
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

def gen_primes(limit):
    '''
    Generates primes numbers up to limit
    '''

    for i in range(limit):
        if check_prime(i):
            yield i

def main():
    '''
    Wrapper function
    '''
    while True:
        try:
            input_limit = int(input('Print all primes up until: '))
            if input_limit <= 0:
                raise RuntimeError
        except ValueError:
            print('I\'m sorry! You must enter an integer. Please try again!\n')
            continue
        except RuntimeError:
            print('I\'m sorry! You must enter an integer greater than 0. Please try again!\n')
            continue
        else:
            break

    for num in gen_primes(input_limit):
        print(num)

if __name__ == '__main__':
    main()
