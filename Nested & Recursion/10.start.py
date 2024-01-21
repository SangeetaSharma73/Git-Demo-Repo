def f(n,i=1):
    if i>n:
        return
    row(n)
    print()
    f(n,i+1)
def row(n):
    if n==0:
        return 
    print('*',end=' ')
    return row(n-1)
f(4)
#nested loop
def yourFirstPattern(n):
    for i in range(n):
        for j in range(n):
            print('*',end=' ')
        print()
            