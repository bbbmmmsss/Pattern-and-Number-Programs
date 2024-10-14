# Write a Python program to remove duplicates from a list.
def remove_duplicates(lst):

    return list(set(lst))

# Example usage
original_list = [1, 2, 3, 2, 4, 3, 5]
unique_list = remove_duplicates(original_list)
print(f"Original List: {original_list}")
print(f"Unique List: {unique_list}")