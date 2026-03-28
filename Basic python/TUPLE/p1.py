# Create a tuple with 5 elements and print it
n = tuple(map(int,input("Enter number :").split()))

if len(n) != 5:
    print("Error")
else :
    print(n)