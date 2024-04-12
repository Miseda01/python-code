#zen = '''
#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.
#'''
#for char in zen:
#   if char in 'aeiou':
#      print(char, end='')
#             
#
for i in range(10):
    if i % 2 == 0:
       continue
    print (i)    



for i in range(10,40):
    if i % 2 == 0:
       print(f"{i}is Even") 
       continue
    print (f"{i}is Odd")    


