def grade_classifier(score):
    if score >= 85:
        print(f"Your score is {score}, So you got an 'A'.")
    elif score >= 70: 
        print(f"Your score is {score}, So you got a 'B'.")
    elif score >= 55:
        print(f"Your score is {score}, So you got a 'C'")
    elif score >= 40:
        print(f"Your score is {score}, So you got a 'D'")
    elif score >= 25:
        print(f"Your score is {score}, So you got an 'E'")
    else:
        (f"Your score is {score}, So you got a 'F'")

score = int(input("Enter your score: ")) 
grade_classifier(score)