t = "this this is is a test test"
c = t.lower().replace(" ","")
ct = {x: c.count(x) for x in c}
print(ct)