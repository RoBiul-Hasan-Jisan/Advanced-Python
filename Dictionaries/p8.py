d1 = {"a": 2, "b": 5, "c": 1}
d2 = {"a": 4, "b": 3, "d": 7}


result = {k: max(d1.get(k, 0), d2.get(k, 0)) for k in set(d1) | set(d2)}

print(result)