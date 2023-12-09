#Getting Data into python

import csv

# Reading from a CSV file
with open('incomee.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# Reading from a Text file
with open('output.txt', 'r') as file:
    text_data = file.read()
    print(text_data)

