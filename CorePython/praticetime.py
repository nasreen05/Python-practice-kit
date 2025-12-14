A=int(input("A:"))
G=int(input("M/F:  "))
if((A==1 or A==2)and G=="M"):
    print("free is 100")
elif(A==3 or A==7 or G=="F"):
    print("free is 200")
elif(A==6 and G=="M"):
    print("fee is 300")
else:
    print("no fee")


#---------------------------> write program to input 2 number & print their sum <--------------------------------

first=int(input("enter first:"))
second=int(input("enter second:"))

print("sum=", first+second)

#-----------------> WAP to input side of a square & print a aarea <-------------------------
side=float(input("enter square side:"))
print("area=", side * side)

#--------------->WAP to input 2 floating point numbers & print their average<--------------
A=float(input("enter first:"))
B=float(input("enter second:"))
print("avg =", (A+B)/2)

A=float(input("enter first:"))
B=float(input("enter second:"))
print (A>=B)