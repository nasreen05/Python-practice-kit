#------------------- WAF to print the length of a list-------------

cities= ["delhi","kolkata","mumbai","noida","chennai"]
heroes =["thor","ironman","captain","srk","amir khan"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end=" ")

        print_list(heroes)

   #   print_len(cities)
    #   print_len(heroes)

    #--------------------------WAF to find the factorial of n---------------------

    n=5
    fact =1
    for i in range(1,n+1):
        fact *= i
        print(fact)