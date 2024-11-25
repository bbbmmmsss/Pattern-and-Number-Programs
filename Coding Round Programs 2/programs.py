1. Reverse a String
python
Copy code
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))
--------------------------------------------------------------------
2. Find the Largest Element in an Array
python
Copy code
def find_largest(arr):
    return max(arr)

print(find_largest([1, 2, 3, 4, 5]))
------------------------------------------------------------------
3. Check for Palindrome
python
Copy code
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False
-------------------------------------------------------------------
4. Factorial Calculation
python
Copy code
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
------------------------------------------------------------------
5. Fibonacci Series
python
Copy code
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(10))
------------------------------------------------------------------
6. Check for Prime Number
python
Copy code
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(29))  # True
print(is_prime(10))  # False
-------------------------------------------------------------------
7. String Anagrams
python
Copy code
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))   # False
-------------------------------------------------------------------
8. Array Sorting (Bubble Sort)
python
Copy code
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
-------------------------------------------------------------------
9. Binary Search
python
Copy code
def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search([1, 2, 3, 4, 5], 4))  # 3
-----------------------------------------------------------------------------
10. Duplicate Elements in an Array
python
Copy code
def find_duplicates(arr):
    from collections import Counter
    counter = Counter(arr)
    return [item for item, count in counter.items() if count > 1]

print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))
---------------------------------------------------------------------------------
11. Linked List Reversal
python
Copy code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev, current = None, head
    while current:
        next_node = current.next
        current.next = prev
        prev, current = current, next_node
    return prev
  ---------------------------------------------------------------------------
12. Matrix Operations (Addition)
python
Copy code
import numpy as np

def matrix_addition(a, b):
    return np.add(a, b)

print(matrix_addition([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
----------------------------------------------------------------------------------
13. Implement a Stack
python
Copy code
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if self.stack else None
 ---------------------------------------------------------------------------------------
14. Implement a Queue
python
Copy code
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None
---------------------------------------------------------------------------------------------
15. Inheritance and Polymorphism
python
Copy code
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
-------------------------------------------------------------------------------------------------------------
16. Exception Handling
python
Copy code
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
-------------------------------------------------------------------------------------------------
17. File I/O
python
Copy code
with open("sample.txt", "w") as file:
    file.write("Hello, world!")

with open("sample.txt", "r") as file:
    print(file.read())
----------------------------------------------------------------------------------------------
18. Multithreading
python
Copy code
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
------------------------------------------------------------------------------------------------
19. Lambda Expressions
python
Copy code
add = lambda x, y: x + y
print(add(5, 3))  # 8
---------------------------------------------------------------------------------------
20. Recursive Algorithms (Fibonacci)
python
Copy code
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print([fibonacci_recursive(i) for i in range(10)])
