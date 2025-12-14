# create a new file "practice.txt" using python .add the followiing data in it

with open ("practice.txt","w")as f:
    f.write("hi everyone\nwe are learning file I/O\n")
    f.write("using java.\nI like programimg in java")

#------------------------------2nd question------------
with open ("practice.txt","w")as f:
    data =f.read()

    new_data=data.replace("java","python")
    print(new_data)

    with open("practice.txt","r")as f:
        data =f.read()
    



#----------------------------------3rd question--------------------------------
def check_for_word():

   word ="xlearning"

   with open ("practice.txt","w")as f:
    data =f.read()
    if(data.find( word )!=-1):
      print("found")
    else:
       print("not found")
   


# WAF to find which line of the file does  the word"learning " occcur first"
#print-1 if would not found

def check_for_word():

   word ="xlearning"

   with open ("practice.txt","w")as f:
    data =f.read()
    if(data.find( word )!=-1):
      print("found")
    else:
       print("not found")
   

def check_for_word():

   word ="learning"
data =True
line_no =1
with open ("practice.txt","r")as f:
    while data:
     data =f.readline()
if(word in data ):
               print(link_no)
return
link_no +=1

return -1

print(check_for_line())

#--------------from a file containnig numbers separated by comma. print the count of even numbers-------------------

with open ("practice.txt","r")as f:
    data = f.read()
    print(data)

    num =""
    for i in range(len(data)):
    if(data[i] == ","):
      print(num)
      num =""
    else:
       num +=data[i]   

#--------------------------

with open ("practice.txt","r")as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    print(nums)

    #--------------------------------
    count =0
    with open ("practice.txt","r")as f:
    data = f.read()
    
    nums = data.split(",")
for val in nums:
    if(int (val) % 2==0):
        count +=1
    
    print(count)