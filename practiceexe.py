# 31 Define a string and count the occurrences of a specific character
string = "Hellow world"
character = "1"
count = 0
for char in string:
    if char == character:
        count += 1
        print(f"occurences of '[character]' in '{string}': {count}")


# 32 Print a parttern of astrisks using while loop
rows = 5
i = 1
while i <= rows:
    print('*' * i)
    i += 1


# 33: Define a list of strings and convert each string to uppercase
words = ['apple', 'banana', 'orange']
uppercased_words = [words.upper() for words in words]
print("Uppercased words: " uppercased_words)



# 34 Define a list of numbers and check if any of them are even
numbers = [1, 3, 5, 7, 9]
for num in numbers:
    if num % 2 == 0:
        print("Found an even number :", num)
        break
    else:
        print("No even mumber found in the list.")


# 35 Define a list and reverse its elements using a for loop
numbers[1, 2, 3, 4, 5]
reversed_numbers = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[i])
print("Reversed list :", reversed_numbers)


# 36 Ask the user for a number until they enter a positive number
while True
    number = int(input("Enter a positive number: "))
    if number > 0:
        print("You entered a positive number.")
        break
    else:
        print("Please enter a positive number")
        
        
# 37 Define a function to calculate the factorial of a number using a recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
    #Calculate and print the factorial of a number
    number = 5
    print ("Factorial of", number, "is", factorial(number))



# 38 Ask the user for a number and check its range using multiple of statements
number = int(input("Enter a number between 1 and 10:"))
if 1 <= number <= 3:
    print("Number is between 1 and 3.")
elif 4 <= number <= 7:
    print("Number is between 4 and 7.")
elif 8 <= number <= 10:
    print("Number is between 8 and 10.")
else:
    print("Number is not in the specified range.")



# 39 Define a list of numbers and calculate their sum using a for loop
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
print("Sum of numbers in the list:", sum)



# 40 Define a list of numbers and count the even and odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even Numbers:", even_count)
print("Odd numbers:", odd_count)



# 1 Define two interger variables and print their sum
num1 = 10
num2 = 5
print("Sum of", num1, "and" , num2, "is:", num1 + num2)



#2 Define two float variables and print their product
float1 = 3.5
float2 = 2.0
print ("Product of ",float1, "and", float2, "is: ", float1 * float2)



#3 Define a dictionary reprenting a person and print their age
person = {'name': 'John', 'age' : 25}
print(person['name'], "is" , person['age'], "years old,")



#4 Define a list of fruits and print each fruit in a separate line
fruits = ['apple', 'banana', 'orange', 'kiwi']
print("List of fruits:")
for fruit in fruits:
    print(fruit)



#5 Perform addition, subtrraction, multiplication, and division of two numbers
num3 = 15
num4 = 3
print("Addition :", num3 + num4)
print("Subtraction :", num3 - num4)
print("Multiplication:", num3 * num4)
print("Division:" ,num3 / num4)


#6 Check if a number is even or odd
num5 = 7
if num5 % 2 == 0:
    print(num5, "is even.")
else:
    print(num5, "is Odd.")



#7 Print numbers from 1 to 10 using a for loop
print ("Numbers from 1 to 10:")
for 1 in range(1,11):
    print(i)



#8 Define a string variable and print its length
text = "Hello, world!"
print ("Length of the string: ", len(text))


#9 Generate a list of squares of numbers from 1 to 5
squares = [x ** 2 for x in range(1.6)]
print ("List squares: ", squares)



# 21 Define variables and use f-string for string formatting 
name = "Emily"
age = 25
print(f"My name is {name} and I am {age} years old.")



#22 Ask the user for a sentence and find the longest word
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print ("The longest word in the sentence is: ", longest_word)



#23 Ask the user for a word and check if it's a palindrome
word = input("Enter a word: ")
if word == word[::-1]:
    print("The word is a palindrome.")
else:
    print ("The word is nor a palindrome.")



#24 Ask the user for their first name and last name and generate a username
First_name = input("Enter your first name: ")
last_name = input ("Enter your last name: ")
username = first_name.Lower() + "_" + last_name.lower()
print("Your username is: ", username)




#26 Ask the user for a word and count the number of vowels and consonants
word = input("Enter a word: ").lower()
vowels = 0
consonants = 0
for char in word:
    if char.isalpha():
        if char in 'aeiou':
            vowels += 1
        else:
            consonants += 1
print("Number of vowels: ", vowels)
print ("Number of consonants: ", consonants)



#27 Ask the use for a sentence and reverse the order of words
sentence = input("Enter a sentence: ")
reversed_sentence = ' '.join(sentence.split() [::-1])
print ("Reversed sentence: ", reversed_sentence) 


#28 Ask the user for a sentence and capitalise the first letter of each word
sentence = input("Enter a sentence: ")
capitalized_sentence = ' '.join(word.capitalize() for word in sentence.split()) 
print("Capitalized sentence: ", capitalized_sentence)


#29 Ask the user for a string and remove duplicate characters
string = input("Enter a string: ")
unique_chars = input ''.join(set(string))
print ("String with duplicate removed: ", unique_chars)



# 30 Ask the user for two words and check if they are anagrams
word1 = input("Enter the first word: ").lower()
word2 = input("Enter the second word: ").lower()
if sorted(word1) == sorted(word2):
    print("The words are anagrams.")
else :
    print("The words are not anagrams.") 




import random
import time
def generate_numbers():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    return num1, num2

def main():
    num1, num2 = generate_numbers()
    correct_sum = num1 + num2

print("Add these two numbers within 5 seconds: ")
print(num1, "+", num2)

try:
    user_input = int(input("Enter the sum: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    return

Start_time = time.time()
while time.time() - start_time < 5:
    if user_input == correct_sum:
        print("Pass")
        return
    else:
        print("Fail: Incorrect sum.")
        return

print("Fail: Time limit exceeded.")





        
            









    










