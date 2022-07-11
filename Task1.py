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
numbers = {}
for data in texts:
     numbers[data[0]] = 1
     numbers[data[1]] = 1
for data in calls:
     numbers[data[0]] = 1
     numbers[data[1]] = 1     
print('There are %d different telephone numbers in the records.'%len(numbers))
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
