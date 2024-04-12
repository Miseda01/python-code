from math import pi, sqrt


sentence = "Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!"

print(sentence)

#Question 4 

'''
Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
A = pi * r **2
r**2 = A // pi
r = sqrt(A//pi)
'''
area = float(input("\n\n\t Enter The Area "))
r = sqrt (area)