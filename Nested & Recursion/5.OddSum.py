#Recursion
def oddSum(n,i=1):
    if i>n:
        return 
    else:
        s=Recursive(i)
        print(s)
        return oddSum(n,i+1)
def Recursive(i,j=1,curr_sum=0):
    if j>i:
        return curr_sum
    else:
        if j%2==1:
            curr_sum+=j
        return Recursive(i,j+1,curr_sum)
oddSum(4)
#Nested Loop
def oddSumAgain(num):
    s=0
    for i in range(1,num+1):
        s=0
        for j in range(1,i+1):
            if j%2==1:
                s+=j
        print(s)