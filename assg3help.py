#============================
# PROGRAM SPECIFICATIONS
# NARRATIVE DESCRIPTION: Assignment 3
#
# @author (David Proia)
# @version(2-15-12)
#==============================
import string

def load_username(username):
  with open('password.txt') as f:
    credentials = [x.strip().split(' ') for x in f.readlines()]

  for username,password in credentials:

def load_password(password):
  with open('password.txt') as f:
    credentials = [x.strip().split(' ') for x in f.readlines()]

  for username,password in credentials:

def print_menu():
  print('1. Press 1 to enter a username/password combination')
  print('2. Press 2 to add another username/password combination.")
  print('3. Type 7 to quit out')

while print_menu == "0":
    if print = "1":
        user2=input("Username: ")
        pass1=input("Enter Password: ")
        if user2==username and pass1==password:
            print ("System Acessed...")
        else:
            print ("Error: Incorrect username or password.")  
     



