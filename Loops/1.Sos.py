def Sos(n,x):
    if n==1:
        return 1
    return x**(n-1)+Sos(n-1,x)
ans=Sos(3,2)
print(ans)
def Sos(n,x):
    if n==0:
        return 1
    return x**(n)+Sos(n-1,x)
ans=Sos(2,2)
print(ans)