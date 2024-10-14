# Python Program to Print Hollow Square Star Pattern

# side = int(input("Please Enter any Side of a Square  : "))
n=3
print("Hollow Square Star Pattern")
for i in range(n):
    for j in range(n):
        if(i == 0 or i == n - 1 or j == 0 or j == n - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()