import random
student_score = [100, 120, 156, 265, 129, 205, 97, 78, 254, 158, 301, 260, 222, 154, 116, 117, 185, 214, 300]
finalScore = 0

for score in student_score: 
    if score > finalScore:
        finalScore = score
        
print(finalScore)



