def f(n,i=1,j=1):
    if i>n:
        return 
    if j<=i:
        print(j)
        return f(n,i,j+1)
    return f(n,i+1,j=1)
f(5)
#NEsted Loop
def anotherNested(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j)
anotherNested(4)