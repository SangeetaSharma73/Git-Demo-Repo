def f(n):
    if n<=0:
        return 0
    else:
        f(n-1)
        if n%2==1:
            print(n)
ans=f(12)