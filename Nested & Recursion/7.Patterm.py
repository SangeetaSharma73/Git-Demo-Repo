#Recursion
def Fun(N,i=0,j=0):
    if i==N:
        return 
    elif j<N:
        print(i*N+j+1,end=' ')
        return Fun(N,i,j+1)
    print()
    return Fun(N,i+1,j=0)
    
Fun(3)   

#Nested loop
def patternOfN(N):
    for i in range(N):
        for j in range(N):
            print(i*N+j+1,end=' ')
        print()

#Nested Loop
def patternOfN(N):
    c=1
    for i in range(N):
        for j in range(1,N+1):
            print(c,end=' ')
            c+=1
        print()
