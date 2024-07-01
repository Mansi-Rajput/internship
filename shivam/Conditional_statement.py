#The function  grade_ckassifier takes a numerical grade as input and returns a letter grade 
def grade_classifier(grade):

  if grade >= 90:
    return "A"
  elif grade >= 80:
    return "B"
  elif grade >= 70:
    return "C"
  elif grade >= 60:
    return "D"
  else:
    return "F"

grades = [72,85,63,91,98]

for grade in grades:
    letter_grade = grade_classifier(grade)
    print(grade,letter_grade)
