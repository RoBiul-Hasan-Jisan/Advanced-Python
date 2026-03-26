# Find Minimum Marks
def mina(st):
    return min(st,key = st.get)


st = {"Alice": 85,"Bob":92,"jisan":32}

print(mina(st))