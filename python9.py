"""students = ["Anand", "Geetha", "Kumar"]
marks = [85, 90, 78]

student_marks = {}

for index, student in  enumerate(students):
    student_marks[student] = marks[index]
print(student_marks)"""

#creation of dictionary from two lists

students = ["Anand", "Geetha", "Kumar"]
marks = [85, 90, 78]
student_marks = {}

for i in range(0,len(students),2):
    student_marks[students[i]] = marks[i]
print(student_marks)

