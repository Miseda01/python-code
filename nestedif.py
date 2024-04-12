# Prompting the user to enter exam score
score = float(input("Enter your exam score: "))

# Nested if statements to determine the grade
if score > 95:
        grade = 'A+'
        if score >= 90:
             grade = 'A'

else:
    if score >= 80:
        grade = 'B'
    else:
        if score >= 70:
            grade = 'C'
        else:
            if score >= 60:
                grade = 'D'
            else:
                grade = 'F'
#Printin
print (f"Your grade is {grade}")          




