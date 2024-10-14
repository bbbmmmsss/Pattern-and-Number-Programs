# Write a Python program to find the second largest number in a list.
def find_second_largest(numbers):

    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements.")

    largest = max(numbers)
    second_largest = min(numbers)

    for num in numbers:
        if num > second_largest and num < largest:
            second_largest = num

    return second_largest
# Example usage
nums = [10, 5, 8, 20, 3]
second_largest_num = find_second_largest(nums)
print(f"The second largest number is {second_largest_num}")

# ex:2

def find_second_largest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

# Test the function
nums = [70, 5, 8, 500, 3]
second_largest_num = find_second_largest(nums)
print(f"The second largest number is {second_largest_num}")
