#marks = int(input("Enter marks: "))
#result = ""
#if marks < 30:
    #result = "Failed"
#elif marks > 75:
    #result = "Passed with distinction"    
#else:
    #
result = "Passed"
#print ("Result =" ,result)

#name = "Frank"
#if "c" in name:
    #print("There is letter c in provided name: ", name)
#else:
    #print ("There is no letter c in provided name: ", name)


#name = "Frank"
#lname = "Onyango"f discount_amount < amount / 2 :
        decision 
#if "c" in name and "c" lname :
#    print(f"There is letter c in both names: {name} and {lname} ")
#else:
 #   print (f"There is no letter c in provided name: {name} and {lname} ")


#discount IF, ELIF, ELSE Statements
discount = 20
discount_amount = 0
amount = 10000 
decision = "" if amount < 1200:
    discount_amount = amount * discount / 100
    if= "expensive"
    elif discount_amount < amount / 4 :
     decision = "Moderate"
    else:
        decision = "Cheap"
print (f"discount = {amount- discount_amount} decision = {decision}")



def temperature_converter():
    choice = input("Convert from Celsius to Fahrenheit (C) or from Fahrenheit to Celsius (F): ").upper()

    if choice == "C":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F.")
    elif choice == "F":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C.")
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")

temperature_converter()


# Grade Classifier

def grade_classifier():
    score = float(input("Enter your score: "))

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Your grade is: {grade}")

grade_classifier()

# Odd or Even Number Checker

def odd_even_checker():
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

odd_even_checker()

# Simple Calculator

def simple_calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero!")
            return
        result = num1 / num2
    else:
        print("Invalid operator!")
        return

    print(f"The result is: {result}")

simple_calculator()


