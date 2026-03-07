import time


def log_time(func):
    """Decorator to log function calling time"""
    def wrapper(*args, **kwargs):
        print(f"\nFunction '{func.__name__}' called at {time.strftime('%X')}")
        result = func(*args, **kwargs)
        return result
    return wrapper


@log_time
def report(*args, **kwargs):
    """Builds a flexible report with positional and keyword data."""
    
  
    if args:
        print("\n--- Positional Data ---")
        for i, value in enumerate(args, start=1):
            print(f"{i}. {value}")
    
  
    if kwargs:
        print("\n--- Keyword Data ---")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    
 
    print("\nReport generated successfully!\n")


report("Alice", "Bob", "Charlie", score=95, grade="A", subject="Math")