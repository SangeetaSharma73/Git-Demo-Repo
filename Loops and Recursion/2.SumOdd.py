def f(n,s):
    if n==0:
        return s
    elif n%2==1:
        s+=n
    return f(n-1,s)
ans=f(10,0)
print(ans)