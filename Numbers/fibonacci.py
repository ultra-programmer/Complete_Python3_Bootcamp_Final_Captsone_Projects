"""
Fibonacci sequence generator
"""
def fib(n):
    '''
    Generate a fibonacci sequence up to n
    '''
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

#Test
for i in fib(10):
    print(i)
