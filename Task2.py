"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
numbers = dict()

for data in calls:
    if data[0] not in numbers:
         numbers[data[0]] = int(data[3])
    else:
        numbers[data[0]] += int(data[3])
    if data[1] not in numbers:
         numbers[data[1]] = int(data[3])
    else:
        numbers[data[1]] += int(data[3])
key = ''
value = 0
for k, v in numbers.items():
    if int(v) > value:
        value = int(v)
        key = k
print('%s spent the longest time, %d seconds, on the phone during September 2016.'%(key,value))


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

