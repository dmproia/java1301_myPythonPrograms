


def matchlogin(login,passwd):
    file = open( "password.txt", "rt" )
    for aLine in file:
        value= aLine.strip().split(" ")
        if value[0] == (login) and value[1] == (passwd) :
            return login,passwd
        else:
            print ()

while True:
    login1=input("Username: ")
    word=input("Enter Password: ")
    if matchlogin(login1,word):
        print ("System Acessed...")
    else:
        print ("Error: Incorrect username or password.")

file.close()
