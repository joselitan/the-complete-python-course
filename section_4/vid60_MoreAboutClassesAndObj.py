class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Rolf Smith', [70, 80, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])


print(student_one.average())
print(student_two.average())