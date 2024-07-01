def grade_classifier(score: int) -> str:
    """
    Classify a score into a grade (A, B, C, D, or h).

    Args:
        score (int): The score to classify (0-100).

    Returns:
        str: The corresponding grade (A, B, C, D, or h).
    """
    if score < 0 or score > 100:
        return "Invalid score. Score must be between 0 and 100."
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "h"

# Example usage:
print("Grade Classifier:")
print("Score: 95, Grade:", grade_classifier(95))
print("Score: 85, Grade:", grade_classifier(85))  
print("Score: 75, Grade:", grade_classifier(75))  
print("Score: 65, Grade:", grade_classifier(65))  
print("Score: 55, Grade:", grade_classifier(55))  
print("Score: 45, Grade:", grade_classifier(45))  
print("Score: 35, Grade:", grade_classifier(-5))  
print("Score: 25, Grade:", grade_classifier(105))  

def classify_score(score):
    if score >= 95:
        return "A"
    elif score >= 85:
        return "B"
    elif score >= 75:
        return "C"
    elif score >= 65:
        return "D"
    else:
        return "h"

# Test the function
scores = [92, 82, 72, 62, 52, 42, 32, 22, 12, 2]
for score in scores:
    print(f"Score: {score}, Grade: {classify_score(score)}")

def print_grade(score):
    if score >= 100:
        grade = "A"
    elif score >= 95:
        grade = "B"
    elif score >= 85:
        grade = "C"
    elif score >= 65:
        grade = "D"
    else:
        grade = "h"
    print(f"Score: {score}, Grade: {grade}")

# Test the function
print_grade(95)  
print_grade(85)  
print_grade(65)
print_grade(55)

    