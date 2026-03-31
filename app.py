def report(*args, **kwargs):
    print("---- REPORT ----")
    
    # Positional arguments
    if args:
        print("Positional Data:")
        for i, value in enumerate(args, start=1):
            print(f"{i}. {value}")
    
    # Keyword arguments
    if kwargs:
        print("\nKey-Value Data:")
        for key, value in kwargs.items():
            print(f"{key} : {value}")
    
    print("----------------")

# Example usage
report("Student Info", name="jisan", id=101, cgpa=3.4)
