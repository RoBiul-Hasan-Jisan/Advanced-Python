n_list = list(map(int, input("Enter numbers: ").split()))
squares = list(x**2 for x in n_list)
print(squares)
print(type(squares))