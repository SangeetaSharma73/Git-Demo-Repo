def divisible(n,k):
    if n<=0:
        return 0
    else:
        if n%k==0:
            return n+divisible(n-1,k)
        return divisible(n-1,k)
ans=divisible(7,2)
print(ans)
#chatgpt
def divisible_sum(n, k):
    if n <= 0:
        return 0
    elif n % k == 0:
        return n + divisible_sum(n - 1, k)
    else:
        return divisible_sum(n - 1, k)

# Example usage
ans = divisible_sum(7, 2)
print(ans)
