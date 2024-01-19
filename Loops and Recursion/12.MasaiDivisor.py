def f(left,right,k):
    if left>right:
        return 0
    else:
        if left%k==0:
            return 1+f(left+1,right,k)
        return f(left+1,right,k)
ans=f(1,10,3)
print(ans)
#2nd
def f(left,right,k):
    if left>right:
        return 0
    elif left%k==0:
        return 1+f(left+1,right,k)
    else:
        return f(left+1,right,k)
ans=f(1,10,3)
print(ans)