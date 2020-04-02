# open up our file
file_object = open("prices.txt", "a")

keepgoing = True

while keepgoing == True:

    # ask the user for a price
    price = float(input("give me a price: "))

    if price > 0:

        # store the price
        file_object.write(str(price) + "\n")

    else:

        # end the loop
        keepgoing = False

# close the file
file_object.close()
