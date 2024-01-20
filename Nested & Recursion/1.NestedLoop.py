def print_nested_recursively(n, i=0):
    if i == n:
        return
    
    def print_row(j=0):
        if j == n:
            return
        print(j + 1, end=' ')
        print_row(j + 1)

    print_row()
    print()
    print_nested_recursively(n, i + 1)

# Example: Print the nested pattern with n = 4
print('USing Recursion')
print_nested_recursively(4)


print(' Using Loop')
def yourFirstNested(n):
    for i in range(n):
        for j in range(n):
            print(j+1,end=' ')
        print()
yourFirstNested(5)

#Using one function
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