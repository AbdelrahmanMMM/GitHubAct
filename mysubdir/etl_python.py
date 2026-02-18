import csv

# open the csv file
with open('Book1.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # loop through each row
    for row in reader:
        print(row)
