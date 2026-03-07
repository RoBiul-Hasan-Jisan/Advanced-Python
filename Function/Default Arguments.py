def student(name, course="cse", university="EDU"):
    print(name, course, university)

name = input("Enter name: ")
course = input("Enter course (press Enter for default): ")
university = input("Enter university (press Enter for default): ")

if course == "":
    student(name)
elif university == "":
    student(name, course)
else:
    student(name, course, university)