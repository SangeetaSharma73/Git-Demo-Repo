#NEsted
def solve(n):
    for i in range(n):
        for j in range(n,0,-1):
            print(j,end=' ')
        print()
def print_numbers_recursive(n, row=1):
    if row > n:
        return
    
    print_numbers_in_reverse(n)
    print()

    print_numbers_recursive(n, row + 1)

def print_numbers_in_reverse(k):
    if k == 0:
        return
    
    print(k, end=' ')
    print_numbers_in_reverse(k - 1)

# Example usage:
n = 5
print_numbers_recursive(n)