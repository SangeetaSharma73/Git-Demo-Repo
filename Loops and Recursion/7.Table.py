def mul(n,i=1):
    if i==10:
        return n*i
    else:
        print(n*i)
        return mul(n,i+1)
ans=mul(3)
print(ans)