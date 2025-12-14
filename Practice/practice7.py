#________________________ print numbers from 1 to 100___________________________

i=100
while i >=1:
    print(i)
    i-=1


#________________________print numbers from 100 to 1______________________________
i=100
while i >=1 :
    print(i)
    i -=1

#_____________________print the multiplication table of a number n___________________

i=1
while i<=10:
    print(3*i)
    i +=1

#__________2nd process_________

n = int (input ("enter number:"))
i=1
while i <=10:
    print(n *i)
    i +=1

#_________________print the element of the following list using  a loop_____________________

nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx +=1


nums = [1,4,9,16,25,36,49,64,81,100]

x=36
i = 0
while i < len(nums):
    if(nums[i]==x):
     print("FOUND at idx ",i)
    i +=1







