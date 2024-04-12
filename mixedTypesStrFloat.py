# List of mixed types (string and float)
grades = ['A', 90.5, 'B', 85.3, 'C', 70.2, 'D', 65.2, 'E', 50]

# Looping through list elements and printing grades
print("\nGrades:")
for grade in grades:
    if isinstance(grade, str):  # Checking if the element is a string
        print(f"Grade\t:{grade}")
    elif isinstance(grade, float):  # Checking if the element is a float
        print(f"Numeric Grade: {grade}" )
    elif isinstance(grade,int):
        print(f"Whole Number Grade: {grade}")
        
