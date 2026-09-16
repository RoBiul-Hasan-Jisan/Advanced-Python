# Class Methods and Static Methods

# So far our 'Employee' methods (like 'fullname' and 'apply_raise') are REGULAR METHODS. They
# automatically take the Class Instance as the first argument, which we call 'self' by convention.

# There are 2 other types of methods you should know about: Class Methods and Static Methods.

import datetime


class Employee:

    number_of_employees = 0
    raised_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.number_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # --- CLASS METHOD ---
    # We turn a regular method into a Class Method by using the '@classmethod' decorator.
    # A Class Method automatically takes the CLASS itself as the first argument instead of the
    # Class Instance. By convention we call this first parameter 'cls' (short for class), the same
    # way we call the Class Instance parameter 'self'.
    @classmethod
    def set_raised_amount(cls, amount):
        # Because we access 'raised_amount' through 'cls' (the class) instead of 'self', this
        # changes the raise amount for the CLASS, which means it changes it for every Class
        # Instance too (unless a specific instance has overridden it, refer to Tutorial 2).
        cls.raised_amount = amount

    # --- CLASS METHOD AS AN ALTERNATIVE CONSTRUCTOR ---
    # A very common use of Class Methods is to provide alternative ways of creating a Class
    # Instance ('alternative constructors'). Lets say most of the time, employee information is
    # given to us as a single hyphen-separated string, e.g. 'John-Doe-70000'. Instead of manually
    # splitting this string every time before calling 'Employee(...)', we can put that logic
    # inside a Class Method.
    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        # 'cls(...)' here is the same as calling 'Employee(...)'. Using 'cls' instead of the
        # class name directly means this still works correctly even if this class is later
        # subclassed (see Tutorial 4 on Inheritance).
        return cls(first, last, int(pay))

    # --- STATIC METHOD ---
    # Regular methods automatically pass 'self' (the instance), Class Methods automatically pass
    # 'cls' (the class). STATIC METHODS pass NEITHER. We use them when some logic is logically
    # related to the class, but doesn't actually need to access the instance or the class itself.

    # A good way to check if something should be a Static Method: if you don't use 'self' or
    # 'cls' anywhere inside the method, it should probably be a Static Method.
    @staticmethod
    def is_workday(day):
        # 'day' here is expected to be a 'datetime.date' object. 'weekday()' returns 0 for
        # Monday through 6 for Sunday, so 5 (Saturday) and 6 (Sunday) are not workdays.
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Using the Class Method to change the raise amount for the whole class (and therefore every
# instance that hasn't overridden it individually).
Employee.set_raised_amount(1.05)
print(Employee.raised_amount)
print(emp_1.raised_amount)
print(emp_2.raised_amount)

# Using the Class Method as an alternative constructor. Notice we never had to manually split the
# string ourselves in the main code.
emp_str_1 = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

# Using the Static Method. Since it doesn't need 'self' or 'cls', we can call it directly off the
# class (or an instance, but calling it off the class makes the intent clearer).
my_date = datetime.date(2026, 7, 10)
print(Employee.is_workday(my_date))
