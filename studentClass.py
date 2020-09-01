class Student:
    def __init__(self, name, school_id, gpa):
        self.student_name = name
        self.student_id = school_id
        self.student_gpa = gpa

    def __str__(self):
        return f"Student name: {self.student_name}, ID: {self.student_id}, GPA: {self.student_gpa}"


def main():
    alex = Student("Alex", "a12345", 3.6)
    sam = Student("Sam", "b4321", 2.4)
    devin = Student("Devin", "c2314", 4.0)

    print(alex)
    print(sam)
    print(devin)


main()

"""Seems to me that data class looks a lot cleaner and removes the
extra codes that takes up space like __init__ etc. """
