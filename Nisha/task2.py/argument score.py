def classify_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test the function
scores = [85, 75, 65, 55, 45, 35, 25, 15, 11, 2]
for score in scores:
    print(f"Score: {score}, Grade: {classify_score(score)}")