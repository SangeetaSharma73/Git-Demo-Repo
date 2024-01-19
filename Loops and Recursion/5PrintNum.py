def f(n):
    if n==0:
        return 
    else:
        print(n)
        return f(n-1)
ans=f(5)