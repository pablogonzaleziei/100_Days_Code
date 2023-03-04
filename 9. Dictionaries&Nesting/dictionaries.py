student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades ={}
for names in student_scores:
    if student_scores[names]>90:
        student_grades[names] = "Outstanding"
    elif student_scores[names]>80:
        student_grades[names] = "Exceeds Expectations"
    elif student_scores[names]>70:
        student_grades[names] = "Acceptable"
    else:
        student_grades[names] = "Fail"
print(student_grades)
        






# print('welcome to the auction')
