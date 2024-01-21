def print_pattern_recursive(n,row=0,col=0):
    if row < n:
        if col < n:
            if row == 0 or col == 0:
                print('*', end=' ')
            print_pattern_recursive(n, row, col + 1)
        else:
            print()
            print_pattern_recursive(n, row + 1, 0)
    
print_pattern_recursive(4)

print('Nested')
# def solve(n):
#     for i in range(n):
#         for j in range(n):
#             if i==0 or j==0:
#                 print('*',end=' ')
#         print()