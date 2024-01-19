def f(n,s):
    if n==0:
        return s
    elif n%2==1:
        s+=n
    return f(n-1,s)
ans=f(10,0)
print(ans)
#another way
def f(n):
    if n<=0:
        return 0
    elif n%2==1:
        return n+f(n-1)
    return f(n-1)
ans=f(6)
print(ans)