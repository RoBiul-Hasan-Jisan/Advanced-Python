# Take tuple input from user
numbers = tuple(map(int, input("Enter numbers: ").split()))

# Element to count
x = int(input("Enter element to count: "))

# Count
print(numbers.count(x))