numbers = []

while True:
    number = input("Enter a list of numbers separated by commas (or 'done' to finish): ")
    if number.lower() == "done":
        break
    try:
        number_list = [int(num.strip()) for num in number.split(",")]
        numbers.extend(number_list)
    except ValueError:
        print("Please enter valid numbers separated by commas.")

if not numbers:
    print("No numbers entered")
else:
    minimum = min(numbers)
    maximum = max(numbers)
    summation = sum(numbers)
    average = summation / len(numbers)
    
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Sum:", summation)
    print("Average:", average)
