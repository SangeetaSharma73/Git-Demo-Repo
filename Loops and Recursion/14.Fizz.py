def Fizz(n):
    if n<=0:
        return n
    Fizz(n-1)
    if n%3==0 and n%5==0:
        print('FizzBuzz')
    elif n%3==0:
        print('Fizz')
    elif n%5==0:
        print('Buzz')
    else:
        print(n)
Fizz(3)
