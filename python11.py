#creation of dictionary using dictionary comprehension which prints name and how much letters are there in it
"""l=["Dhhanus", "Lord", "God", "kingdome"]
dict={i:len(i) for i in l}
print(dict)"""


marks_crad={
    "Anand":85,
    "Geetha":90,
    "Kumar":78 , 
    "raju":60
    }
#to print the names of students who passed the exam
dictionction={name:marks for (name,marks) in marks_crad.items() if marks>=80}
print(dictionction)