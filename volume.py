import math

# Dictionary to store shape names and their respective volume formulas
volume_formulas = {
    'cuboid': ('l * w * h', ['l', 'w', 'h']),
    'cube': ('s ** 3', ['s']),
    'cylinder': ('pi * (r ** 2) * h', ['r', 'h']),
    'wedge': ('0.5 * l * w * h', ['l', 'w', 'h']),
    'prism': ('b * h', ['b', 'h']),
    'pyramid': ('(1/3) * b * h', ['b', 'h'])
}

# Input shape and dimensions
shape = input("Enter the shape (cuboid, cube, cylinder, wedge, prism, pyramid): ")

if shape in volume_formulas:
    if shape in ['cuboid', 'cylinder', 'wedge', 'prism']:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
    elif shape == 'cube':
        side = float(input("Enter the side length: "))
    elif shape == 'pyramid':
        base_area = float(input("Enter the base area: "))
        height = float(input("Enter the height: "))

    # Prompt user for fraction
    fraction = input("Enter fraction (1/1, 1/2, 1/4, 3/4): ")
    fraction = eval(fraction)  # Evaluating fraction input to handle fractions

    # Calculate volume based on shape and fraction
    if fraction in [1/1, 1/2, 1/4, 3/4]:
        if shape in ['cuboid', 'cylinder', 'wedge', 'prism']:
            variables = volume_formulas[shape][1]
            expression = volume_formulas[shape][0]
            volume = eval(expression, {**locals(), **globals()}) * fraction
        elif shape == 'cube':
            expression = volume_formulas[shape][0]
            variables = volume_formulas[shape][1]
            volume = eval(expression, {**locals(), **globals()}) * fraction
        elif shape == 'pyramid':
            expression = volume_formulas[shape][0]
            variables = volume_formulas[shape][1]
            volume = eval(expression, {**locals(), **globals()}) * fraction

        # Output the calculated volume
        print("The volume of", shape, "is:", volume)
    else:
        print("Invalid fraction input. Please enter 1/1, 1/2, 1/4, or 3/4.")
else:
    print("Invalid shape input. Please enter a valid shape.")
