# write  a recursivefunction to calculate the sum of first  n natural numbers


def calc_sum(n):
    if(n==0):
        return
    print(n)
    calc_sum(n-1)

    calc_sum(5)

    #-----------------------------2nd process-----------------------
def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n
sum = calc_sum(10)
print(sum)


# write a recursive function to print all element in a list.
#hint: use list & index as parameters

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

    fruits= ["mango","litch","apple","banana"]
    print_list(fruits)