#ask user if they want to generate the password or not
#if yes,ask the length of the password
#generate password
#print
#if no,exit 
import string
import random
characters=list(string.ascii_letters + string.digits + "!@#$%^&*")

def generate_password():
    password_length=int(input("enter the length of the password"))
    random.shuffle(characters)
    #list of characters are shuffled so that it should not be like  abc321!@
    password=[]
    for x in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    #to have a strong password 
    password="".join(password)
    print(password)
    
option=int(input("do u want to generate password--  "))
if option=="yes":
  generate_password()
elif option=="no":
   print("program_exit")
   quit()
else:
   print("invalid")
   quit()

