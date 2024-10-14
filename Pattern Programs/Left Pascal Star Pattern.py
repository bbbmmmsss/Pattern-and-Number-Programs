# left pascal triangle
n = 5

# upper triangle
for i in range(n):
    # print spaces
    for j in range(n - i - 1):
        print(' ', end='')
    # print stars
    for k in range(i + 1):
        print('*', end='')
    print()

# lower triangle
for i in range(n - 1):
    # print spaces
    for j in range(i + 1):
        print(' ', end='')
    # print stars
    for k in range(n - i - 1):
        print('*', end='')
    print()