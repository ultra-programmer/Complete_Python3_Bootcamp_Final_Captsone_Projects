"""
Fibonacci sequence generator
"""
def fib(limit):
    '''
    Generate a fibonacci sequence up to limit
    '''
    num_1 = 1
    num_2 = 1
    for i in range(limit):
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2

#Test
while True:
    try:
        FIB_LIMIT = int(input('Print all fibonacci numbers up to: '))
    except ValueError:
        print('I\'m sorry! You must enter an integer! Please try again!\n')
        continue
    else:
        break

for num in fib(FIB_LIMIT):
    print(num)
