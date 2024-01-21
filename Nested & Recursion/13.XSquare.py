def print_pattern_recursive(n,row=0,col=0):
    if row < n:
        if col < n:
            if row == 0 or col == 0 or row == n - 1 or col == n - 1 or row == col or row + col == n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
            print_pattern_recursive(n, row, col + 1)
        else:
            print()
            print_pattern_recursive(n, row + 1, 0)
    
print_pattern_recursive(6)


def solve(n):
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1 or i==j or i+j==n-1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()