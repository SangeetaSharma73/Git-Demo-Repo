def print_nested_recursively(n, i=0, j=0):
    if i == n:
        return

    if j == n:
        print()
        print_nested_recursively(n, i + 1, 0)
        return

    print(j + 1, end=' ')
    print_nested_recursively(n, i, j + 1)

# Example: Print the nested pattern with n = 4
print_nested_recursively(4)

#using nested loop
def yourFirstPattern(n):
    for i in range(n):
        for j in range(n):
            print('*',end=' ')
        print()
yourFirstPattern(5)