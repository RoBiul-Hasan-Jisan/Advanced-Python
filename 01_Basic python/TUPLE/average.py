# Input numbers from user
t = tuple(map(int, input("Enter numbers separated by space: ").split()))

# Calculate average
print("Average of elements:", sum(t) / len(t))