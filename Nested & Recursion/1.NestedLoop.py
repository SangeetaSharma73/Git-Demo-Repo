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
print_nested_recursively(4)
