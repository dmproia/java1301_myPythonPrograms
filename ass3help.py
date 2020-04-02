#============================
# PROGRAM SPECIFICATIONS
# NARRATIVE DESCRIPTION: Assignment 3
#
# @author (David Proia)
# @version(2-15-12)
#==============================
import string

file = open ("password.txt", 'r')
firstNames = list()
lastNames = list()
for line in file:
    values = line.split()
    firstNames.append(values[0])
    lastNames.append(values[1])
    print ("First Name:", values[0], "\nPassword  :", values[1])
file.close()

repeat = "yes"
while (repeat == "yes"):
    username = input(str.lower("Enter your username: "))
    print()
    password = input("Enter your password: \nPasswords are case sensitive: ")
    print()
    repeat = str.lower(input("Type 'yes' to continue or 'no' to stop? yes/no: "))
    while (repeat != "no" and repeat != "yes"):
            print("INVALID ENTRY")
            repeat = str.lower(input("To keep going type=> yes\nTo stop type=> no : "))
            print ()
