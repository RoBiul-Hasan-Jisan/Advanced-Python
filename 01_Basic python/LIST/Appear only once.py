n_list = list(map(int, input("Enter numbers: ").split()))


s = list(x for x in n_list if n_list.count(x)==1)

print(s)
print(type(s))