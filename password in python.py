from operator import truediv
import string 
import random
s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)

caracter_number=input("how many caracter do you need: ")

while True:
     try:
        caracter_number= int(caracter_number)
        if caracter_number < 6:
         print ("you need at lest 6")
         caracter_number=input("how many caracter do you need: ")
        else :
              break
     except:
         print("enter the number only")
         caracter_number=input("how many caracter do you need: ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1=round(caracter_number*(30/100))
part2=round(caracter_number*(20/100))

password= []
for i in range(part1):
      password.append(s1[i])
      password.append(s2[i])
for i in range(part2):
      password.append(s3[i])
      password.append(s4[i])

random.shuffle(password)   
password="".join(password[0:])  

print(password)



        


