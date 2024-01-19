#mycode
def divisible(n,k):
    if n==1:
        return 1
    else:
        divisible(n-1,k)
        if n%k==0:
            print(n)
divisible(7,2)
#chatgpt
def divisible(n, k):
    if n == 1:
        return  # Base case: stop recursion when n reaches 1
    else:
        divisible(n - 1, k)  # Recur with n-1

        if n % k == 0:
            print(n)

# Example usage
divisible(7, 2)