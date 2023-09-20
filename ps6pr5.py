#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# 2-D Lists
#
# Computer Science 111
# 

import random

def create_grid(num_rows, num_cols):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = []
    
    for r in range(num_rows):
        row = [0] * num_cols     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line.
        input: grid is a 2-D list
    """
    num_rows = len(grid)
    for r in range(num_rows):
        if r == 0:
            print('[', end='')
        else:
            print(' ', end='')
        if r < num_rows - 1:
            print(str(grid[r]) + ',')
        else:
            print(str(grid[r]) + ']')

def random_grid(num_rows, num_cols):
    """ creates and returns a 2-D list with the specified dimensions
        in which each cell is assigned a random integer from 0-9.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = create_grid(num_rows, num_cols)

    for r in range(num_rows):
        for c in range(num_cols):
            grid[r][c] = random.choice(range(10))
            
    return grid

def row_index_grid(num_rows, num_cols):
    """ creates and returns a 2-D list with the specified dimensions
        in which each cell is assigned the integer of the row number.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = create_grid(num_rows, num_cols)

    for r in range(num_rows):
        for c in range(num_cols):
            grid[r][c] = r
            
    return grid

def num_between(grid, n1, n2):
    """Takes a grid and returns the amount 
    of values in the grid between n1 and n2"""
    
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] >= n1:
                if grid[r][c] <= n2:
                    count = count + 1
    
    return count
            
def copy(grid):
    """Creates and returns a deep copy of 
    the grid with the same dimensions and 
    cell values"""

    new_grid = []
    for r in range(len(grid)):
        next_grid = []
        for c in range(len(grid[0])):
            next_grid = next_grid + [grid[r][c]]
        
        new_grid = new_grid + [next_grid]
            
    return new_grid
            
def double_with_cap(grid, cap):
    """Takes a 2-D list and returns the 
    double of each value unless it is 
    more then the cap, then it returns 
    the cap instead"""
    
    for r in range(len(grid)):
        for c in range(len(grid[0])): 
            double_value = grid[r][c]*2
            if double_value > cap:
                grid[r][c] = cap
            else:
                grid[r][c] = double_value
    
def sum_evens_in_col(grid, colnum):
    """Returns the sum of the even values 
    in the colnum of the grid which is 
    the index colnum"""
    
    total = 0
    for r in range(len(grid)):
        if grid[r][colnum] % 2 == 0:
            total = total + grid[r][colnum]
    
    return total
            
            
            
            
            









