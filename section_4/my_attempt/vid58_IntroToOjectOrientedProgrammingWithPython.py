my_student = {
    'name': 'Rolf Smith',
    'grade': [70, 80, 90, 99]
}
my_student = my_student["grade"]
# print(my_student)
# sumOfGrades = sum(my_student)
# print(sumOfGrades)
# count = len(my_student)
# print(count)
# gradeAverage = sumOfGrades / count
# print(gradeAverage)
def avg_grade(grades):
    return sum(grades) / len(grades)

print(avg_grade(my_student))

