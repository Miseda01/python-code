from collections import Counter
from operator import itemgetter
from itertools import groupby


words = ["loop","eye", "eye","in","into","jane",
         "look","around","number","sum","square",
         "value","loop","eye","in","into","look",
         "around,", "number", "between"]
wordCount = Counter(words)
topWord=wordCount.most_common(4)
print(topWord)

rows = [
{"address":"5412 N CLARK","date":"07/01/2023"},
{"address":"5148 N CLARK","date":"07/04/2023"},
{"address":"4040 R NAIROBI","date":"08/03/2023"},
{"address":"1060 W KISUMU","date":"08/03/2023"},
{"address":"1039 S MOMBASA","date":"07/01/2023"},
{"address":"4040 R NAIROBI","date":"04/03/2023"},
{"address":"1039 S NAIROBI","date":"07/01/2023"}               
]

rows.sort(key= itemgetter("date"))
for date,items in groupby(rows, key=itemgetter("date")):
    print(date)
    for i in items:
        print(f"{i}")

# while loop for increamenting or decreamenting a counter
counter = 0
end = int(input("Enter the last count:"))

while end >= counter: 
    print(f"Counter:{end}")
    end -= 5

# counting the number of characters in a statement
start = 0
sentence = '''
while loop for increamenting or decreamenting a counter 
while loop for increamenting or decreamenting a counter
counting the number of characters in a statement
counting the number of characters in a statement
''' 

c = len(sentence)
for char in sentence: 
    start += 1
print(f"Total characters : {start}")
print(f"Total length : {c} ")