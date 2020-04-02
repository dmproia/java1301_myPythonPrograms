# ask the user for their username
# and password
username = input("What's your username: ")
password = input("What's your password: ")
repeat = "yes"
while (repeat == "yes"):
    # store the username and password
    file_object = open("password.txt", "w")

    # send the information into the file
    file_object.write(username + " " + password)

    # print a confirmation
    print ("Your account has been set up")

    # close the file
    file_object.close()

    # open up a connection to my file
    file_object = open("password.txt", "r")

    # grab the username
    username_from_file = file_object.readline()
    username_from_file = username_from_file.rstrip()

    # grab the password
    password_from_file = file_object.readline()
    password_from_file = password_from_file.rstrip()

    # close the file
    file_object.close()

    # now that we have the username and password
    # ask the current user for their info
    # if it matches what's in the file we cna let them in
    # otherwise they can't log in
    username = input("username: ")
    password = input("password: ")

    # check to see if they match
    if username == username_from_file and password == password_from_file:
        print ("you're in!")
    else:
        print ("sorry, wrong info")
    # next ask the user if they wish to go again
    # yes keeps running program
    # no ends program
    repeat = str.lower(input("Type 'yes' to continue or 'no' to stop? yes/no: "))
    while (repeat != "no" and repeat != "yes"):
        print("INVALID ENTRY")
        repeat = str.lower(input("To keep going type=> yes\nTo stop type=> no : "))
        print ()
