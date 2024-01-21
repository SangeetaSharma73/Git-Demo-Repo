def s(n,i=0,j=0):
    if i==n:
        return
    elif j<n:
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
        return s(n,i,j+1)
    print()
        
    return s(n,i+1,j=0)
s(7)
print('NEsted Loop')
def solve(n):
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()