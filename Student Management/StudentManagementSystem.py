from utils import average, grade

class InvalidError(Exception):
    pass

class Student:
    def __init__(self, student_id, name, age, marks):
        self.__student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def get_student_id(self):
        return self.__student_id

    def stu_average(self):
        return average(self.marks)

    def stu_grade(self):
        return grade(self.marks)

    def display(self):
        print(f"Student ID: {self.__student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.stu_average():.2f}")
        print(f"Grade: {self.stu_grade()}")

class CollegeStudent(Student):
    def __init__(self, student_id, name, age, marks, department, year):
        super().__init__(student_id, name, age, marks)
        self.department = department
        self.year = year

def add_student():
    try:
        sid = int(input("Enter your student_id: "))
        name = input("Enter Your Name: ")
        age = int(input("Enter your age: "))

        if age < 5 or age > 30:
            raise InvalidError("Invalid Age Error")

        dept = input("Enter your Department: ")
        year = int(input("Enter your Batch Year: "))
        marks = list(map(int, input("Enter your marks: ").split(",")))

        s1 = CollegeStudent(sid, name, age, marks, dept, year)
        with open("Details.txt", "a") as f:
            marks_str = "|".join(map(str, marks))
            f.write(f"{sid},{name},{age},{dept},{year},{marks_str}\n")

        print("\nStudent Added Successfully\n")
        s1.display()

    except ValueError:
        print("Please enter valid numeric values")

    except InvalidError as e:
        print(e)

add_student()