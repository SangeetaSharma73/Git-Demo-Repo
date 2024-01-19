def mod(n):
    if n<=0:
        return 0
    else:
        mod(n-1)
        print(n%10)

mod(5)
