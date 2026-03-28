# Slice a tuple to get the middle elements

n = tuple(map(int, input("Enter 5 numbers: ").split()))
middle = n[1:-1]
print("Middle elements:", middle)