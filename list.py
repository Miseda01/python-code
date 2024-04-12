my_numbers = [1,2,3,4,5,1,2,8,8,1,1,1,52.00,10.1,] # integers
fruits = ["apple","tomatoes","mango","avocado","peas", "orange","pineapple",]
#myListString= []
print (fruits)
print (my_numbers)
print (fruits[4])  #indexing
print(my_numbers[7])
print (len(fruits))

#modifying elements in a list
fruits [4] = "Lemon"
fruits [5] = "Coconut"
print (fruits)

#Appending and removing elements
fruits.append("Coconut")
print (fruits) # Output: [10,2,4,5,6]
fruits.remove ("Coconut")
print (fruits) # Output: [10,2,4,5,6]
