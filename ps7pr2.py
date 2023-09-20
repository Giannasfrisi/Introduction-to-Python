# 
# ps7pr2.py - Problem Set 7, Problem 2
#
# Our Rectangle class revisited
#

import math

class Rectangle:
    def __init__(self, init_width, init_height, unit):
        """ constructor for a Rectangle object with the specified dimensions 
            init_width and init_height, and initial x and y coordinates of 0
        """
        self.x = 0
        self.y = 0
        self.width = init_width
        self.height = init_height
        self.unit = unit
        
    
    def grow(self, dwidth, dheight):
        """ modifies the dimensions of the called Rectangle object
            (the one given by self) by adding dwidth to the current width
            and dheight to the current height.
            Note that nothing needs to be returned. The changes are
            made to the internals of the called object, and thus they 
            will still be there after the method returns!
        """
        self.width += dwidth
        self.height += dheight

    def area(self):
        """ computes and returns the area of the called Rectangle object
        """
        return self.width * self.height

    def perimeter(self):
        """ computes and returns the perimeter of the called Rectangle object
        """
        return 2*self.width + 2*self.height

    def scale(self, factor):
        """ modifies the dimensions of the called Rectangle object
            by multiplying them by the specified factor.
        """
        self.width *= factor
        self.height *= factor

    def __eq__(self, other):
        """ determines if the called Rectangle object (self) is 
            equivalent to the Rectangle object given by other
            note: the \ symbol at the end of the first line below 
            allows us to continue that line onto the next line of the file.
        """
        if self.width == other.width and \
           self.height == other.height and \
           self.unit == other.unit:    
            return True
        else:
            return False

    def __repr__(self):
        """ creates and returns a string representation of the 
            called Rectangle object
        """
        return str(self.width) + ' x ' + str(self.height) + " " + (self.unit)
    
    def diagonal(self):
        """Returns the rectangle's diagonal (square root of the sum of he squares)"""
        
        sum_squares = self.width**2 + self.height**2
        return math.sqrt(sum_squares)
    
    def larger_than(self, other):
        """Determines if one rectangles area is larger than another rectangle's area"""
        
        if str(self.unit) != str(other.unit):
            return False
        
        if int(self.area()) > int(other.area()):
            return True 
        
        else:
            return False
        
    
    
    