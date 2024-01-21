#Recursive
def pattern(N):
    if N==0:
        return
    else:
        pattern(N-1)
        print('*'*N)
pattern(4)
#Nested
print('Loop')
def patternPrinting(N):
    for i in range(1,N+1):
        print('*'*i)
