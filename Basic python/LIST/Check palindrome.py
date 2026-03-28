lst = list(map(int, input("Enter numbers: ").split()))

# Check palindrome
is_palindrome = lst == lst[::-1]

print("Is palindrome:", is_palindrome)