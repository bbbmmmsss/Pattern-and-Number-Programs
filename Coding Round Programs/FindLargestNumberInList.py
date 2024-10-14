# Write a Python program to find the largest element in a list.
def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Test the function
nums = [10, 5, 8, 20, 3]
largest_num = find_largest(nums)
print(f"The largest number is {largest_num}")

#------------------------------------------------------------

#Ex:2 Second Method
def find_largest(numbers):
    return max(numbers)
# Test the function
print(find_largest([1, 2, 3, 4, 5]))