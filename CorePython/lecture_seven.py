#-------------------------Read file


# open("demo.txt")
f=open("demo.txt","r")
data = f.read()
print(data)
print(type(data))

#---------------------------

f= open("demo.txt","r")
data = f.read(5)
print(data)
f.close()

#---------------------------------------

f=open("demo.txt","r")
line1 = f.readline()
print(line1)
f.close()



#----------------------------------------


f=open("demo.txt","r")
data = f.read()
print(data)

line1 = f.readline()
print(line1)



line2 = f.readline()
print(line2)

f.close()



#-------------------------------write file -------------------------------
f= open("demo.txt","w")

f.write("i want to learn javascript tommorw.123")

f.close()


f= open("demo.txt","w")

f.write("\n i want to learn javascript tommorw.123")

f.close()


f = open("simple.txt","w")
f.close()

#-----------------------------------

f= open("demo.txt","w")
# f.write("123")
print(f.read())
f.write("abc")
f.close()


#----------------with syntex

with open("demo.txt","r") as f:
    data =f.read()
    print(data)

    with  open("demo.txt","w") as f:
        f.write("new data")


#--------------------------Deleting File----------------------

import os
os.remove("sample.txt")
