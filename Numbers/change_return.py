'''
A Change Return Calculator.
Never get shortchanged again! (pun intended)
'''
while True:
    try:
        COST = round(float(input('What is the cost of the item (in USD): ')), 2)
        CASH_GIVEN = round(float(input('What is the amount of money given (in USD): ')), 2)
        COST = int(COST * 100)
        CASH_GIVEN = int(CASH_GIVEN * 100)
        if COST > CASH_GIVEN:
            raise ArithmeticError
        if COST <= 0 or CASH_GIVEN <= 0:
            raise RuntimeError
    except ValueError:
        # Make sure input values are numbers
        print('I\'m sorry! You must enter a rational number. Please try again!\n')
        continue
    except ArithmeticError:
        # Make sure that there is enough money to pay for the item
        print('I\'m sorry! You do not have enough money to purchase that!\n')
        continue
    except RuntimeError:
        # Make sure that both input values aren't 0
        print('I\'m sorry! You must enter a number greater than 0. Please try again!\n')
        continue
    else:
        # If everything is good, move on
        break

#Find the amount of change due
MONEY_DUE = CASH_GIVEN - COST

#Find the number of dollars owed
DOLLARS = MONEY_DUE // 100
DOLLAR_TEMP_TOTAL = MONEY_DUE - DOLLARS * 100

#Find the number of quarters owed
QUARTERS = DOLLAR_TEMP_TOTAL // 25
QUARTER_TEMP_TOTAL = DOLLAR_TEMP_TOTAL - QUARTERS * 25

# Find the number of dimes owed
DIMES = QUARTER_TEMP_TOTAL // 10
DIME_TEMP_TOTAL = QUARTER_TEMP_TOTAL - DIMES * 10

# Find the number of nickels owed
NICKELS = DIME_TEMP_TOTAL // 5
NICKEL_TEMP_TOTAL = DIME_TEMP_TOTAL - NICKELS * 5

# Find the number of pennies owed
PENNIES = NICKEL_TEMP_TOTAL // 1
PENNY_TEMP_TOTAL = NICKEL_TEMP_TOTAL - PENNIES * 1

# Print everything out
print(f'Change due: {MONEY_DUE / 100} dollars.')
print(f'You are owed {DOLLARS} dollars, {QUARTERS} quarters, {DIMES} dimes, {NICKELS} nickels, and {PENNIES} pennies.')
