# function to print solid rhombus
def solidRhombus(n):
    for i in range(1, n+1):
        for j in range(1, n-i+1):
            print(" ", end="")
        for j in range(1, n+1):
            print("*", end="")
        print()

n = 5
print("Solid Rhombus:")
solidRhombus(n)