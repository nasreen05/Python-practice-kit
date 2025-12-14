# WAP to ask the user names of their 3 fav. movie & store them in a list

movies=[]
mov1=input("enter the first movie:")
mov2=input("enter the second movie:")
mov3=input ("enter third movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

# WAP to check if list contains a palindrom of element .(hint: use copy()mrthod)

list1=[1,2,3]
list2=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("palindrom")
else:
    print("Not palindrom")


    #WAP to count the number of student wwith the "A" grade in the following tuple["C","D","A","A","B","B","A"]


    grade  = ("C","D","A","A","B","B","A")
    print(grade.count("A"))

    # store  the above value in a list & sort them from"A" to "D".
grade  = ["C","D","A","A","B","B","A"]
grade.sort()

print(grade)


