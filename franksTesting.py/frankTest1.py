# Exercise-Integer
#1. Assign two integer variables, `a`and `b`, with values 10 and5 respectively. Print their sum.
#a=10
#b=5
#print("1. Sum of a and b is:",a+b)

#2. Assign an integer variable `num` with a value of 25.Printits square.
#num1=25
#print("2. Square of num1 is:",num1 **2)

#Assign an integer variable `count` with a value of 1. Printits value.
#count=20
#print("3.Value of count is:",count)

#temperature=20
#if temperature > 25:
    #print("4.It's a hot day.")
#else:
    #print("4.It's not a hot day")

#minutes=130
#hours=minutes//60
#remaining_minutes=minutes%60
#print("5.Time is:",hours,"hours and",remaining_minutes,
#"minutes.")

#year=2029
#if(year % 4 == 0 and year % 100!=0)or(year % 400==0):
    #print("6. It's a leap year.")
#else:
    #print ("6.It's not a leap year.")


#radius=5
#area=3.14159*radius**2
#print("7. Area of the circle is:",area)

#num1=30
#num2=7
#division_result=num1//num2
#print("8.Division result rounded down is:",division_result)

#length=30
#width=5
#perimeter=2*(length+width)
#print("9. Perimeter of the rectangle is:",perimeter)

seconds=3800
hours=seconds//3600
minutes=(seconds%3600)//60
remaining_seconds=seconds % 60
print("10. Time is:", hours,"hours,",minutes,"minutes,and", remaining_seconds,"seconds.")
      

number=37
is_prime=True
if number > 1:
    for i in range(2, int(number**0.5)+1):
        if number % i==0:
           is_prime=False
           break
if is_prime:
    print("11.It's a prime number.")
else:
    print("11. It's not a prime number.")            


      