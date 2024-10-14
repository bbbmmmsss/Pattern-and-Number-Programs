# Ex 1. Write a Python program to check if a string is a palindrome.

def is_palindrome(string):
    # Remove whitespace and convert to lowercase
    cleaned_string = ''.join(char for char in string.lower() if char.isalnum())

    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage
input_string = "A man a plan a canal Panama"
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
#----------------------------------------------------------------

# Ex 2.

def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

# Test the function
word = "madam"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
#---------------------------------------------------------------
# Ex:3 Third Method

def is_palindrome(s):
    return s == s[::-1]
# Test the function
print(is_palindrome("racecar"))
