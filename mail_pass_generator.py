import string
import random
first=input("Enter first name: ")
last=input("Enter last name: ")
num=int(input("Enter the length of password: "))
all_char=string.ascii_letters+string.digits+string.punctuation
num1=random.randint(1,1000)
num2=str(num1)
email=first+'.'+last+num2+'@gmail.com'
password=''
for i in range(num):
    rand_char=random.choice(all_char)
    password=password+rand_char
    
print("Your suggested gmail is: ",email)
print("Your suggested password is: ",password)    