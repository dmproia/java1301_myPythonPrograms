

with open('password.txt') as f:
  credentials = [x.strip().split(' ') for x in f.readlines()]

for username,password in credentials:


#User/Password Input
    user2=input("Username: ")
    pass1=input("Enter Password: ")
    if user2==username and pass1==password:
        print ("System Acessed...")
    else:
        print ("Error: Incorrect username or password.")
    
