student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = ''

for student in student_scores:
    print(student)
    if student_scores[student]>= 91:
        print("Outstanding")
    elif student_scores[student]>=81:
        print("Exceeds Expectations")
    elif student_scores[student]>=71:
        print("Acceptable")
    elif student_scores[student]<=70:
        print("Fail")
    else:
        print("Cannot Read this Score")
    