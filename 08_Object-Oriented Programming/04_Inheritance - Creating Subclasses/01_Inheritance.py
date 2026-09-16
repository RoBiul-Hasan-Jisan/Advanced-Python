# Inheritance - Creating Subclasses

# Inheritance allows us to inherit attributes and methods from a PARENT class. This is useful
# because we can create SUBCLASSES and get all of the functionality of the parent class, and then
# override or add whatever we need on top of that, without rewriting code from scratch.

# Lets say our company now has different types of Employees: 'Developer' and 'Manager'. Both are
# still Employees (same 'first', 'last', 'pay', 'email', 'fullname()'), but each also needs some
# extra, more specific attributes/behaviour.


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


# To make 'Developer' a Subclass of 'Employee', we simply put 'Employee' in the brackets where we
# would normally leave empty brackets or no brackets at all.
class Developer(Employee):
    # Developers get a bigger raise than regular employees, so we override the 'raised_amount'
    # Class Variable here. Everything else ('__init__', 'fullname', 'apply_raise') is inherited
    # from 'Employee' automatically - we didn't have to type any of that again.
    raised_amount = 1.10

    # We want Developers to also have a 'programming_language' attribute, which a normal Employee
    # doesn't have. To do this, we need our own '__init__' method for 'Developer'.
    def __init__(self, first, last, pay, prog_lang):
        # Instead of retyping 'self.first = first' etc, we can let the parent class ('Employee')
        # handle those by calling 'super().__init__(...)'. This passes the arguments up to the
        # parent's '__init__' method. ('super()' refers to the parent class, 'Employee' here).
        super().__init__(first, last, pay)
        # Then we just add the extra attribute that's unique to 'Developer'.
        self.prog_lang = prog_lang


# Managers are also Employees, but each Manager also manages a list of other Employees.
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # We use 'None' as the default instead of an empty list '[]' directly. This is because
        # mutable default arguments (like lists) are shared across every instance that doesn't
        # provide one, which usually leads to bugs. Using 'None' and creating a new list inside
        # the method avoids that problem.
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

# 'Developer' inherited 'email' and 'fullname()' from 'Employee' without us writing them again.
print(dev_1.email)
print(dev_1.prog_lang)

# 'Developer' has its own 'raised_amount' (1.10), overriding the one from 'Employee' (1.04).
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.add_employee(dev_2)
mgr_1.print_employees()
mgr_1.remove_employee(dev_1)
mgr_1.print_employees()

# Python has 2 built-in functions to help you learn about inheritance relationships:

# 'isinstance()' tells you whether an object is an instance of a class (including any of its
# parent classes).
print(isinstance(mgr_1, Manager))    # True, mgr_1 is directly a Manager
print(isinstance(mgr_1, Employee))   # True, Manager inherits from Employee
print(isinstance(mgr_1, Developer))  # False, Manager and Developer are unrelated siblings

# 'issubclass()' tells you whether a class is a subclass of another class.
print(issubclass(Developer, Employee))  # True
print(issubclass(Manager, Employee))    # True
print(issubclass(Developer, Manager))   # False
