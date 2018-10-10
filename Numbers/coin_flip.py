"""
Flip a Coin! The classic decision maker!
"""

from random import randint

#Global variables
NUM_HEADS = 0
NUM_TAILS = 0

def flip_coin(num_times):
    '''
    Flips a coin num_times times
    '''
    global NUM_HEADS
    global NUM_TAILS
    for i in range(num_times):
        coin = randint(1, 2)
        if coin == 1:
            NUM_HEADS += 1
            yield 'HEADS'
        else:
            NUM_TAILS += 1
            yield 'TAILS'
#Test
while True:
    try:
        NUM_FLIPS = int(input('How many coins would you like to flip? '))
        if NUM_FLIPS <= 0:
            raise RuntimeError
    except ValueError:
        print('I\'m sorry! You must give an integer! Please try again!\n')
        continue
    except RuntimeError:
        print('I\'m sorry! The input must be greater than 0! Please try again!\n')
        continue
    else:
        break

for flip in flip_coin(NUM_FLIPS):
    print(flip)

print(f'You flipped {NUM_HEADS + NUM_TAILS} coin(s).')
print(f'You got {NUM_HEADS} head(s) and {NUM_TAILS} tail(s).')
