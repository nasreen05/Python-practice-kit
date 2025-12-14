for i in range(5):
    pass
if i >5:
  pass 
print("some useful work")

#--------------Practice set--------------------

#wap to find the sum of first n numbers(usiing while)

n=5
for i in range(n-1):
   print(i)

#------------------------------

n=7
sum=0
for i in range(1, n+1):
   sum +=i
   print("total sum =",sum)

   #------------------------------------------ 

   n=7
   sum =0
   i=1
   while i <=n:
      sum +=i
      i +=1

      print("total sum=",sum)


#wap to find factorial of first n numbers(using for)

n=3
fact =1
i=1
while i<= n:
   fact *=1
   i +=1

   print("factorial =",fact)

   #--------------------------2nd process--------------------

   n=5
   fact =1
for i in range(1, n+1):
      fact *=i

      print("factorial=", fact)

      #--------------------------3rd----------------------

def fact(n):
   if(n==1 or n==0):
      return 1
   return fact(n-1)* n
print(fact(6))



