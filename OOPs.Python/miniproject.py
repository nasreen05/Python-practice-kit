import random

target = random.randint(1,100)

while True:
    userChoice = input("guess the target or Quit(Q):")
    if(userChoice== "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("success : Correct Guess!!")
        break
    elif(userChoice  < target):
        print("your number  was too small. take a bigger guess..")
    else:
        print("your number was  too big.Take a smaller guess.. ")

        print("---------Game Over--------------")





#----------------------2nd Project-----------------------
#import random
#import string


#pass_len =12
#charValues = string.ascii_letters + string.digits

#password=""
#for i in range

#print(random.choice(charValues))
#print(charValues

# print(random.choice(charValues))




#print(string.ascii_letters)
#print(string.digits)
#print(string.punctuation)

#print(random.choice("hello"))

#val  =  random.choice(['a','b','c','d'])
#print(val)



#----------------------- 3rd Project -----------------------

import random
import string

pass_len =12
charValues = string.ascii_letters + string.digits + string.punctuation

#list comprehension [function for i in range(n)]


password ="".join([random.choice(charValues)for i in range(pass_len)])


#password=""
#for i in range (pass_len):
#password += random.choice(charValues)

#password = ""
#for i in range(pass_len):
 #   print(random.choice(charValues))

print("your random password is:", password)