pswd = open( "password.txt", "rt" )
for aLine in pswd:
    value= aLine.split( " " )
    print (value[0], value[1])
user = str()
while user != "1234":
    user=input("Username: ")
    if user == value[0]:
        print ("System Acessed...")
    else:
        print ("Error: Incorrect username or password.")

    pswd.close()
