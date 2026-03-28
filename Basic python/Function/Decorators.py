def decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is called with arguments:", args, kwargs)
        result = func(*args, **kwargs)
        print("Function executed successfully!")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(5, 7))