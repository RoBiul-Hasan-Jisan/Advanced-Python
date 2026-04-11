
nums = list(map(int,input("enter nums :").split()))

cube = list(filter(lambda x : x%2 == 0,nums))

print(cube)