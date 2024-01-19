def Som(x,k,y,i=1):
    if i>k:
        return 0
    elif (x*i)%y==0:
        return (x*i)+Som(x,k,y,i+1)
    else:
        return Som(x,k,y,i+1)
ans=Som(3,10,5)
print(ans)