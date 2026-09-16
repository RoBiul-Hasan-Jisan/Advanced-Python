# Property Decorators - Getters, Setters and Deleters

# Recall that our 'email' attribute is built from 'first' and 'last' at the time the object is
# created (inside '__init__'). This creates a problem: if we change 'emp_1.first' AFTER the object
# has been created, the 'email' attribute does NOT automatically update, since it was only
# calculated once, when '__init__' ran.


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # We turn 'email' into a METHOD instead of a plain attribute, calculating it fresh every time
    # it is accessed, so it will always be up to date with the current 'first'/'last'.
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_1.first = 'Jim'

# The problem now is that anywhere in our code that used to access 'emp_1.email' (as an attribute)
# would now need to be changed to 'emp_1.email()' (as a method call), since we turned it into a
# method. If this attribute was used in many places across a big codebase, that's a lot of changes.

# This is exactly the problem the '@property' decorator solves - it lets us define a method, but
# ACCESS it like a plain attribute (no brackets needed), giving us the best of both: a value that
# recalculates itself, but doesn't require every other line of code to be rewritten.


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # --- GETTER (@property) ---
    # Adding '@property' above a method lets us access it WITHOUT brackets, i.e. as 'emp_1.email'
    # instead of 'emp_1.email()'.
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # --- SETTER (@fullname.setter) ---
    # What if we want to be able to set 'emp_1.fullname = 'Full Name'' directly, and have it
    # automatically split into 'first' and 'last' behind the scenes? For this we need a SETTER,
    # defined with '@<method_name>.setter' right above a method of the SAME name as the property.
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # --- DELETER (@fullname.deleter) ---
    # We can also define what happens when 'del emp_1.fullname' is called, using
    # '@<method_name>.deleter'. Here we'll just clear out the 'first' and 'last' attributes and
    # print a message, purely for demonstration.
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.first = 'Jim'

# Notice we access 'fullname' and 'email' WITHOUT brackets now, even though they are methods
# underneath, thanks to the '@property' decorator.
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# Using the SETTER: this looks like a plain attribute assignment, but it actually runs the
# 'fullname(self, name)' method we defined above with '@fullname.setter', which splits the name
# and updates 'first'/'last' for us.
emp_1.fullname = 'Corey Schafer'
print(emp_1.first)
print(emp_1.last)
print(emp_1.email)

# Using the DELETER: this runs the 'fullname(self)' method defined with '@fullname.deleter'.
del emp_1.fullname
print(emp_1.first)
print(emp_1.last)
