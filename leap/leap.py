def leap_year(year):
    '''Calculate if a given year is a leap year.

    Parameters
    year: int    

    A leap year occurs on every year that is evenly divisible by 4
      except every year that is evenly divisible by 100
        unless the year is also evenly divisible by 400 
    '''

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
