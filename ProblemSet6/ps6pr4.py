#
# ps6pr4.py (Problem Set 6, Problem 4)
#
# TT Securities    
#
# Computer Science 111
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Finding the average price')
    print('(4) Find the min price and its day')
    print('(5) Find the max single-day change and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.
def avg_price(prices):
    """takes the average of a list of prices"""
    
    final = 0
    for i in range(len(prices)):
        final = final + prices[i]
    
    average = final/len(prices)
    return average

def min_day(prices):
    """compares a list of prices and returns
    the day of the smallest price"""
    
    output = []
    day = 0
    final = 0
    for i in range(len(prices)):
        if prices[0] > prices[i]:
            output = i - 1
    
    return output

def max_change_day(prices):
    """returns the largest change in price 
    over a single day"""
    
    output =[]
    difference = 0
    for i in range(len(prices)):
        x = i+1
        if x < len(prices):
            if prices[x] - prices[i] > difference:
                difference = prices[x] - prices[i]
                output = x
    return output

def any_above(prices, threshold):
    """Tests to see if any prices are larger than the threshold"""
    
    for i in range(len(prices)):
        if prices[i] > threshold:
            output = True 
            return output
            
    return output == False

def find_tts(prices):
    """Finds the best day to buy and sell stocks 
    resulting in the largest profit"""
    
    difference = 0
    profit = 0
    output = []
    day_one = 0
    day_two = 0
    for i in range(len(prices)):
        for j in range(len(prices)):
            if prices[j] > prices[i]:
                if j > i:
                    difference = prices[j] - prices[i]
                    if difference > profit:
                        profit = difference
                        day_one = i
                        day_two = j
            
    output = [day_one, day_two, profit]
    return output

def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            average = avg_price(prices)
            print('The average price is', average)
        elif choice == 4:
            output = min_day(prices)
            day = output
            print('The min price is', prices[i], 'on day', day)
        elif choice == 5:
            output = max_change_day(prices)
            day = output
            first_price = prices[i]
            second_price = prices[x]
            print('The max single-day change occurs on day', day, 'when the price goes from', first_price, 'to', second_price )        
        elif choice == 7:
             output = find_tts(prices)
             buy_day = output[0]
             sell_day = output[1]
             profit = output[2]
             print('Buy on day', buy_day, 'at price', prices[buy_day])
             print('Sell on day', sell_day, 'at price', prices[sell_day])
             print('Total profit:', profit)
            
        elif choice == 6:
            threshold = eval(input('Enter the threshold: '))
            output = any_above(prices, threshold)
            if output == True:
                print('There is at least one price above', threshold)
            else:
                print('There are no prices above', threshold)
        
        
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
