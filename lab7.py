#============================
# PROGRAM SPECIFICATIONS
# NARRATIVE DESCRIPTION:Lab7
#
#  @author (David Proia)
#  @version(dat1/25/12)
#==============================

import string
import locale
locale.setlocale( locale.LC_ALL, '' )

repeat = "yes"
YUAN = 0.1579

print ("This program is made to convert Dollars to Yuan")
print()

while (repeat == "yes"):

    
    dollars = float(input("Enter number of dollars you would like to convert: "))
    print(locale.currency(dollars), "converted to Yaun is: ", round(dollars/YUAN,2))
    print()

    repeat = str.lower(input("Would you like to try another amount? yes or no: "))
    print()
    while (repeat != "no" and repeat != "yes"):
        print("INVALID ENTRY")
        repeat = str.lower(input("Would you like to try another amount? yes or no: "))
        print()
