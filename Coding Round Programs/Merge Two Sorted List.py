#Ex: Merge Two Sorted Lists

def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)
# Test the function
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))