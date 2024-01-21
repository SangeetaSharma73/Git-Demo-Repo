#Recursion
def even_sum_recursive(num, i=1):
    if i > num:
        return
    else:
        s = sum_even_numbers(i)
        print(s)
        even_sum_recursive(num, i + 1)

def sum_even_numbers(n, current_sum=0, j=1):
    if j > n:
        return current_sum
    else:
        if j % 2 == 0:
            current_sum += j
        return sum_even_numbers(n, current_sum, j + 1)
#Nested Loop
def evenSumAgain(num):
    for i in range(1,num+1):
        s=0
        for j in range(1,i+1):
            if j%2==0:
                s+=j
        print(s)