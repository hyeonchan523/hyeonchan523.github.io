import check_module
import output_message
print("""This program will tell you if a year is a leap year or not
Type in a year equal to or greater than 0.
It terminates if the year is 0.
""")

while True:
    print("==========================================")
    year = int(input('Type in a positive integer : '))
    leap_year = None
    # check positive number
    if not check_module.validity_check(year):
        continue
    
    # check leak year
    leap_year = check_module.leap_year_check(year)
        
    # Print information
    output_message.print_result(year,leap_year)
    if year ==0:
        break
    print("==========================================\n\n\n")