# Special (Magic or Dunder) Methods

# 'Dunder' is short for 'Double Underscore'. You've already used one Dunder method without
# realising it: '__init__', which runs automatically whenever a new Class Instance is created.

# Special/Dunder methods allow us to change/define the built-in behaviour of our objects, such as
# how they are printed, how they can be added together, or how their length is measured. They let
# our custom objects behave more like Python's own built-in types (like strings, ints and lists).


class Employee:

    raised_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raised_amount)

    # --- __repr__ ---
    # This is meant to be an UNAMBIGUOUS representation of the object, mainly used for
    # debugging/logging, and ideally something you could copy-paste to recreate the same object.
    # This is the representation used when you just type the object's name in the Python shell,
    # or when you print an object inside something like a list.
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # --- __str__ ---
    # This is meant to be a READABLE representation of the object, for the 'end-user' to see. When
    # you call 'print()' on an object, Python looks for '__str__' first. If '__str__' is not
    # defined, it will fall back to using '__repr__' instead.
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # --- __add__ ---
    # This lets us define what happens when we use the '+' operator between 2 Employee objects.
    # Here, lets say adding 2 employees together gives the combined pay of both employees.
    def __add__(self, other):
        return self.pay + other.pay

    # --- __len__ ---
    # This lets us use the built-in 'len()' function on our object. Here we'll (a bit playfully)
    # define the 'length' of an Employee as the number of characters in their full name.
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Without '__repr__' or '__str__' defined, printing an object would show something unhelpful like
# '<__main__.Employee object at 0x000001>'. Now it shows something meaningful instead.
print(emp_1)         # Uses '__str__' since it's defined
print(repr(emp_1))   # Explicitly calling '__repr__'
print(str(emp_1))    # Explicitly calling '__str__'

# These 2 lines below do the exact same thing as the 2 lines above, just written differently -
# Python automatically calls the corresponding Dunder method behind the scenes.
print(emp_1.__repr__())
print(emp_1.__str__())

# Using our custom '__add__' method with the '+' operator.
print(emp_1 + emp_2)

# Using our custom '__len__' method with the built-in 'len()' function.
print(len(emp_1))

# Python has many more special methods for things like '==' ('__eq__'), '<' ('__lt__'),
# subtracting ('__sub__') and many others. You can find the full list by searching for
# 'python special method names' or 'python data model' in the official documentation.
