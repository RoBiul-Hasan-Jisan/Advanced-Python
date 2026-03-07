def student_info(*args, **kwargs):
    print("Subjects:", args)
    print("Details:", kwargs)

student_info("Math", "Physics", "Chem", name="Jisan", university="EDU")