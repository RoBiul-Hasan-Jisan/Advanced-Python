def greet(msg):
    def name_func(name):
        return f"{msg}, {name}!"
    return name_func

say_hello = greet("Hello")
say_bye = greet("Goodbye")

print(say_hello("Alice"))  
print(say_bye("Bob"))      