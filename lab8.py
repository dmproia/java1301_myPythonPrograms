#============================
# PROGRAM SPECIFICATIONS
# NARRATIVE DESCRIPTION:Lab8
#
#  @author (David Proia)
#  @version(1/27/12)
#==============================

repeat = "Y"
print ("This program is designed to tell allow you to tell if you have a right triangle or not" )
print ()

while (repeat == "Y"):

    X = float(input("What is the length of side A of triangle? "))
    Y = float(input("What is the length of side B of triangle? "))
    Z = float(input("What is the length of side C of triangle? "))
    if (X >= Y) and (X >= Z):
        A = Y
        B = Z
        C = X
    elif (Y >= X) and (Y >= Z):
        A = Z
        B = X
        C = Y
    elif (Z >= X) and (Z >= Y):
        A = Y
        B = X
        C = Z



    if (A**2) + (B**2) == (C**2):
        print ("This is a right triangle!")

    else:
        print("This is not a right triangle")

    repeat = input("Press Y to make more conversion or Q to quit: ")
