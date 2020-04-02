# ask the user for their username
# and password
username = input("What's your username: ")
password = input("What's your password: ")

# store the username and password
file_object = open("security.txt", "w")

# send the information into the file
file_object.write(username + "\n")
file_object.write(password + "\n")

# print a confirmation
print ("Your account has been set up")

# close the file
file_object.close()
