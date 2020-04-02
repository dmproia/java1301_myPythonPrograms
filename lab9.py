#============================
# PROGRAM SPECIFICATIONS
# NARRATIVE DESCRIPTION:Lab9
#
#  @author (David Proia)
#  @version(1/30/12)
#==============================
# Functions
def sumNumber(add1, add2):
    return add1 + add2

def subNumber (sub1, sub2):
    return sub1 - sub2

def multNumber(mult1, mult2):
    return mult1 * mult2

def divNumber(div1, div2):
    return (div1 / div2)

print ("This program is a simple calculator")
print ()

menu = ("Type in numbers 1-4 depending on what you want to do:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
print (menu)

repeat = "Y"

# if statements with functions inside it
while (repeat == "Y"):
    choice = (input ( "Type in your choice then press enter: "))
    
   

    while (choice != "1" and choice != "2" and choice !="3" and choice !="4"):
        print ("INVALID ENTRY")
        print (menu)
        choice = input ("Enter a choice: ")

    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: ")) 

    if choice == "1":
        result = (sumNumber(num1, num2))
        operation = "+"
        
    elif choice == "2":
        result = (subNumber (num1, num2))
        operation = "-"
        
    elif choice == "3":
        result = (multNumber(num1, num2))
        operation = "*"
        
    elif choice == "4":
        result = (divNumber(num1, num2))
        operation = "/"
        
    print (num1, operation, num2, "=", result, "\n")
    repeat = input("Would you like to go again: Y/N ??  ")


