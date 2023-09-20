#
# ps8pr1.py  (Problem Set 8, Problem 1)
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month = init_month
        self.day = init_day
        self.year = init_year

    # The function for the Date class that returns a string
    # representation of a Date object.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this *can* be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year, and False otherwise.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, and year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date
    
    def advance_one(self):
        """Changes the called object so that it states 
        one calendar day after the date given"""
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year() == True:
            days_in_month[2] = 29
        
        self.day += 1
        if self.day > days_in_month[self.month]:
            self.day = 1
            self.month += 1
            
            if self.month == 13:
                self.month = 1
                self.year += 1
        
    def advance_n(self, n):
        """Advances the given date 'n' calendar days 
        and prints the dates"""
        
        count = 1
        print(self)
        while count <= n:
            self.advance_one()
            print(self)
            count += 1
    
    def __eq__(self, other):
        """Returns True if self and other represent 
        the same calendar date"""
        if self.month == other.month:
            if self.day == other.day:
                if self.year == other.year:
                    return True
        return False
    
    def is_before(self, other):
        """Returns true if self occurs before other, 
        false is they occur on the same day or 
        self is after other"""
        
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False
        else: #same year
            if self.month < other.month:
                return True
            elif self.month > other.month:
                return False
            else: # same month
                if self.day < other.day:
                    return True
                else: 
                    return False
        
    def is_after(self, other):
        """Returns true if self occurs after other, 
        false is they occur on the same day or 
        self is before other"""
        if self.year > other.year:
            return True
        elif self.year < other.year:
            return False
        else: #same year
            if self.month > other.month:
                return True
            elif self.month < other.month:
                return False
            else: # same month
                if self.day > other.day:
                    return True
                else: 
                    return False
        
    def days_between(self, other):
        """Returns the number of days in between 
        self and other"""
        
        count = 0
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return count 
        
        new_self = self.copy()
        new_other = other.copy()
        
        if new_self.is_before(new_other): # positive number
            while new_self != new_other:
                new_self.advance_one()
                count += 1
            count = count*-1
        else: # negative number
            while new_self != new_other:
                new_other.advance_one()
                count += 1

        return count
    
    def day_name(self):
        """Returns a string that indicates the 
        name of the day of the week"""
        day_names = ['Monday', 'Tuesday', 'Wednesday', 
             'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        test_date = Date(11, 8, 2021)
        if self == (test_date):
            return day_names[0]
        
        else:
            number = self.days_between(test_date)
            index = number % 7 
            return day_names[index]
            







