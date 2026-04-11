d1 = {"a":1,"b":3,"c":4}
d2 = {"a":4,"b":2,"c":2}

re = {k : d1.get(k,0)+d2.get(k,0) for k in d2}

print(re)