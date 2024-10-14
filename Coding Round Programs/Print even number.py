# Printing even numbers from 1 to 10 using a for loop in Python
for number in range(1, 11):
    if number % 2 == 0:
        print(number)

#-------------------------------------------------------------------
#Ex:2 Another Method
def even_numbers(n):
    return [x for x in range(n) if x % 2 == 0]
# Test the function
print(even_numbers(10))
