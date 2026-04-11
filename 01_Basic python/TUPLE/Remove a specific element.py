t = (1, 2, 3, 4, 5)
element_to_remove = 3

# Create a new tuple without the element
new_t = tuple(x for x in t if x != element_to_remove)

print("Original tuple:", t)
print("Tuple after removing", element_to_remove, ":", new_t)