"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
markets = {}
total = {}    
for data in texts:
     total[data[0]] = 1
     total[data[1]] = 1
for data in calls:
     markets[data[0]] = 1
     total[data[1]] = 1    
total = list(total)
markets = list(markets)
isMarkets = []
for number in markets:
    if number not in total:
        isMarkets.append(number)
isMarkets.sort() 
print("These numbers could be telemarketers: ")
for result in isMarkets:
  print(result)    
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

