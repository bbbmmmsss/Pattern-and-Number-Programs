**Top OOP Questions Asked in Python Interviews**
# 1. What are the four main principles of OOP, and how are they implemented in Python?
    A)Inheritance
    B)Polymorphism
    c)Encaspulation
    D)Abstraction
    
A) Inheritance:

-Inheritance allows a class (subclass or derived class) to inherit attributes and methods from another class (superclass or base class), promoting code reuse and creating a hierarchy of classes with shared characteristics


B) Polymorphism:
- Polymorphism refers to the ability of objects to take on multiple forms or behaviors depending on their context or the type of data they operate on.
- It allows for the same method name to behave differently in different contexts or for different types of objects, promoting flexibility and extensibility.
- polymorphism is achieved through method overriding and method overloading,

C) Encaspulation:
- Encapsulation refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit or class.
- It helps in hiding the internal state of an object and only **exposing the necessary methods** to interact with the object’s state.

D) Abstraction: 
- Abstraction refers to the process of hiding the complex implementation details and showing only the essential features of the object.


# 2.Differentiate between instance variables and class variables in Python.

A) Instance Variable:
1. instance variables belong to instances of a class, representing the state of individual objects
2. Instance variables are defined within methods using the self keyword and are unique to each instance
3. Instance variables are specific to each object

B) Class Variable:
1. class variables belong to the class itself, representing attributes shared by all instances of the class
2. whereas class variables are defined outside methods and are accessed using the class name
3. while class variables are common to all objects of the class.

# 3.How do you create a constructor in Python? Explain with an example.
 - In Python, a constructor is a special method called __init__() that is automatically invoked when a new object of a class is created.
   - It is used to initialize the object's state or set up initial values for its attributes.
     - Example: 
      class Car:
        def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year

      car1 = Car("Toyota", "Corolla", 2020)
      print(car1.make)  # Output: Toyota
      print(car1.model)  # Output: Corolla
      print(car1.year)  # Output: 2020

# 4.  Explain the difference between instance methods, class methods, and static methods in Python.
    A) Instance Methods:

    Instance methods are methods that operate on instances of a class and have access to the instance attributes through the self parameter.
    They are defined without any additional decorators and are the most common type of method in Python classes.
    
    B)Class Methods:

    Class methods are methods that operate on the class itself rather than its instances and have access to the class variables through the cls parameter.
    They are defined using the @classmethod decorator and are typically used to create alternative constructors or perform operations that involve the class itself.
 
    C) Static Methods:

    Static methods are methods that do not operate on either instances or classes and are independent of the class state.
    They are defined using the @staticmethod decorator and do not require the self or cls parameters, making them similar to regular functions but within the class namespace

# 5. What is the purpose of the super() function in Python?

- The super() function in Python is used to call methods and access attributes from the superclass (parent class) within a subclass (child class). 
- It allows subclasses to inherit and leverage behavior from their superclass,
- facilitating code reuse and maintaining a clean and organized class hierarchy.
- By using super(), developers can invoke superclass methods and constructors
