def f(n,i=1):
    if i>n:
        return 
    fn(n,i)
    print()
    return f(n,i+1)
def fn(n,i,j=1):
    if j>i:
        return 
    print(i,end=' ')
    return fn(n,i,j+1)
f(5)   
print('#Nested LOop')
def solve(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1,end=' ')
        print()
