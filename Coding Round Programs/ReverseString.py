# Write a Python program to reverse a string.
def reverse_string(string):
    return string[::-1]

# Test the function
text = "Hello, World!"
reversed_text = reverse_string(text)
print(reversed_text)

#-----------------------------------------------------------

#EX:2 Second Method
def reverse_string(s):
    return s[::-1]
# Test the function
print(reverse_string("hello"))