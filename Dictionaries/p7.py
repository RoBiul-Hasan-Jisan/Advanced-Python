d = {'a': 5, 'b': 8, 'c': 3, 'd': 10}


dd = {k : v for k,v in d.items() if v % 2 != 0}
       


print(dd)