def is_prime_recursive(n, divisor=None):
    if divisor is None:
        divisor = n - 1  # Start with the largest possible divisor

    if n <= 1:
        return False  # 1 and any negative number are not prime
    elif divisor == 1:
        return True   # The number is prime if no divisor is found
    elif n % divisor == 0:
        return False  # The number is not prime if it's divisible by the current divisor
    else:
        return is_prime_recursive(n, divisor - 1)  # Check the next smaller divisor

# Example usage
number = 17
result = is_prime_recursive(number)
print(f"{number} is prime: {result}")
