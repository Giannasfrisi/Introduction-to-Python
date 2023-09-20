# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

# function 1
def root(x):
    return x**0.5
    
    
# function 2

def gap(num1, num2):
    if num1 > num2:
        return num1 - num2

    elif num1 < num2:
        return num2 - num1

    else:
        return 0

# function 3
   
#def larger_gap(a1, a2, b1, b2):

  #def gap(a1, a2):
   #   if a1 > a2:
   #       return a1 - a2
    #      a = a1 - a2
          
    #  elif a2 > a1:
    #      return a2 - a1
    #      a = a2 - a1
          
    #  else:
    #      return 0
 
#  def gap(b1, b2):
 #   if b1 > b2:
    #    return b1 - b2
     #   b = b1 - b2    
    
 #   elif b2 > b1:
     #   return b2 - b1
   #     b = b2 - b1
    
 #   else:
  #      return 0
    
# def gap(a, b):
  #  if a > b:
  #      return a
    
  #  else: 
   #     return b
     
    
# function 4

def median (a, b, c):
    if a <= b <= c:
        return b
    
    elif a >= b >= c:
        return b
    
    elif b <= a <= c:
        return a
    
    elif b >= a >= c:
        return a
    
    else:
        return c

    
# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))

    # optional but encouraged: add test calls for your functions below

