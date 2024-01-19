def f(max,min):
    if max==min:
        return min
    else:
        f(max-1,min)
        print(max-1)
ans=f(19,13)