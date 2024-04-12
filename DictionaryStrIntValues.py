# Dictionary with string keys and integer values
student_scores = {'Alice': 85, 'Bob': 90, 'Charlie': 75, 'Frank': 70, 'Carol': 80, 'Peris': 79}

# Looping through dictionary keys and printing student names
print("Student Names:")
for name, scores in student_scores.items():
    print(f"{name}:{scores}")
