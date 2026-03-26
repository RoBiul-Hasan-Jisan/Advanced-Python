
# Merge Two Dictionaries

d1 = {}
d2 = {}

n1 = int(input("enter number of items d1:"))

for i in range(n1):
    key = input("enter key :")
    value = int(input("enter value :"))
    d1[key] = value

n2 = int(input("enter number of items d1:"))

for i in range(n2):
    key = input("enter key :")
    value = int(input("enter value :"))
    d2[key] = value


re = {}

for key in d1:
    re[key] = d1[key]

for key in d2:
    if key in re:
        re[key] += d2[key]
    else:
        re[key] = d2[key]

print("Merged dictionary:", re)


# easy  way 

d1 = {"a":1,"b":3}
d2 = {"a":4,"b":2,"c":2}

re = {k : d1.get(k,0)+d2.get(k,0) for k in set(d1)|set(d2)}

print(re)