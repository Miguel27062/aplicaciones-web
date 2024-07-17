def print_z_pattern(n):
    for i in range(n):
        print('*', end='')
    print()
    for i in range(1, n-1):
        for j in range(n-i-1):
            print(' ', end='')
        print('*')

    for i in range(n):
        print('*', end='')
    print()
n = 7
print_z_pattern(n)
