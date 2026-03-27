# Remove duplicates from a tuple
t = (1, 2, 3, 2, 4, 1, 5)

t_unique = tuple(dict.fromkeys(t))  # dict keys remove duplicates but preserve order

print("Tuple without duplicates (order preserved):", t_unique)