def validity_check(year):
    if year < 0 or int(year) != year:
        print(f"{year} is not a valid input")
        print('Try again.')
        return False
    else :
        print(f"{year} is a valid input")
        return True

def leap_year_check(year):
    if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
            leap_year = True
    else :
            leap_year = False
    return leap_year