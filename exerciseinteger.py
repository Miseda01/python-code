#a = 10
#b = 5
#print(" sum of temperature a and b is:",a + b)

#num = 40
#print (" the square of num is :",num*num)
#print (" the square of num is :", num ** 2)

#v1 = 10
#print (" the value of count:" , v1)

temperature = 20
if temperature > 25:
    print ("it is a hot day")
else:
    print ("it is a cold day")

minutes = 130
hours=minutes//60
remaining_minutes=minutes % 60
print("Time is",hours,"hours and",remaining_minutes,"minutes.")

year=2024
if (year%4==0 and year % 100!=0) or (year % 400==0):
    print("Its a leap year.")
else:
    print("Its not a leap year")

radius=5
area=3.14159*radius**2
print("Area of the circle is:",area)

num1=15
num2=7
division_result=num1//num2
print(" Division result rounded down is:",division_result)

length=10
width=5
perimeter=2*(length+width)
print("Perimeter of the rectangle is:",perimeter)

seconds=3800
hours=seconds//3600
minutes=(seconds%3600)//60
remaining_seconds=seconds%60
print("Time is:",hours,"minutes",minutes,"and","remaining_seconds", "seconds")

age = 18
if age>=18:
    print("Person is eligible to vote.")
else:
    print("Person is not eligible to vote.")

miles=100
kilometres = miles*1.60934
print(" Conversion of miles to kilometres:",kilometres)

num = 12345
digit_sum=0
while num:
    digit_sum+=num%10
num//=10
print("Sum of digits:",digit_sum)

num=72
if num%2==0:
    print("Its an even number.")
else:
    print("Its not an even number.")

price=500
discounted_price=price*0.9
print("final price after discount:",discounted_price)

hours=45
weeks=hours//(7*24)
remaining_days=(hours%(7*24))//24
print(" Time is:",weeks,"weeks and",remaining_days,"days")

#Assign an integer variable 'weight' with a value of 75.Convert it to pounds and print the result.
base=4
exponent=3
result=base**exponent
print(" Power of base raised to exponent:",result)

num=98765
reverse_num=int(str(num)[::-1])
print(" Reverse of the number:",reverse_num)

num1=20
num2=3
result=num1**num2
print(" Result of raising num1 to the power of num 2:",result)

num = 123456
num_digits=len(str(num))
print("Number of digits in num:",num_digits)


#23
num=987654
digit = 0
digit_sum=sum(int(digit)) 
for digit in str(num):
    print("Sum of digits in num:", digit_sum)


#24
num=456789
num_str=str(num)
if num_str==num_str[::-1]:
    print("24.It's a palindrome number.")
else:
    print("24.It's not a palindrome number.")
    

num=100
factors=[]
for i in range(1,num+1):
    if num%i==0:
        factors.append(i)
print("Factors of num:',factors")
      
start=1
end=10
print("Even numbers between start and end:")
for i in range (start,end+1):
    if i % 2==0:
        print (i)

start=10
end=50
print("Odd numbers between start and end:")
for i in range(start, end +1):
    if i % 2!=0:
        print(i)


num=123456789
num_str=str(num)
reverse_num_str=num_str[::-1]
print

num = 2023
num_str=str(num)
if num_str==num_str[::-1]:
    print("It's a palindrome year.")
else:
    num=4567
first_digit=int(str)

#d=90
#n=30
#b="david"
#a="89.00"
#e=float()
#print("Enter a float:",e)
#x=e
#print(x)

j=49
e=float(j)
print(e)

num=4567
first_digit=int(str(sum)[0])
last_digit=num%10
sum_first_last=first_digit+last_digit
print(sum_first_last)


#Exercise-Float
x=3.5
y=2.7
print("Sum of x and y is:", x+y)

radius=4.5
area=3.14159*radius**2
print("Area of the circle is:",area)

temperature_celsius=37
temperature_fahrenheit=(temperature_celsius*9/5)+32
print(temperature_fahrenheit)

price=49.99
discounted_price=price*0.8
print(discounted_price)

length=10.5
width=5.2
perimeter=2*(length+width)
print(" Perimeter of the rectangle is:",perimeter)

num1=3.75
num2=1.25
division_result=num1/num2
print("Division result:", division_result)

distance_km=120
distance_miles=distance_km/1.60934
print

height=1.85
if height>1.80:
    print("Person is tall.")
else:
    print("Person is not tall.")

bill_amount=85.67
tip_amount=bill_amount*0.15
total_amount=bill_amount+tip_amount
print

#Convert it to pounds and print the result
weight_kg=68.5
weight_pounds=weight_kg*2.20462
print("Conversion of kilograms to pounds:",weight_pounds)
































