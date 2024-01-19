def solve(k):
    a=1
    ans='false'
    b=int(k**0.5)
    while a<b:
        if a**2+b**2==k:
            ans='true'
            break
        elif a**2+b**2<k:
            a+=1
        else:
            b-=1
    print(ans)
            