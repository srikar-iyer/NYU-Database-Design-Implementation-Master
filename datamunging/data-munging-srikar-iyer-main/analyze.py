'''Srikar Iyer - Data Munging Assignment - Database Systems and Implementation
Takes the average of temperature variances for each month in each year to return
the final average for each decade 
Imports the csv module.
'''
import csv

# This line opens the CSV file
with open("data/clean_data.csv") as file:

    # csv.reader creates a csv reader object, allowing for a few more convenient methods
    reader = csv.reader(file)

    #This convenient method skips the header row, as we don't want it.
    next(reader)

    # Initializes variables 
    year = None
    decade_temps = []
    decades = {}

    ''' This block iterates over each line in the csv, and does most of the logic.
    year is defined as the first column, or the 0th element of each row. The corresponding decade
    is simply the floor of the year, or // 10 * 10 (since // 10 removes the unit digit)
    year % 10 lets us know when the units digit of the year is 9, and when to calculate the average
    temp, and iterate again. Before that, a decade_temps list appends each temperature for every
    month. finally, the sum of elements in decade_temps divided by the length of decade_temps
    gives the average temperature. The dictionary decades allows all of the decades and average
    temps to be formatted nicely, with keys being the decades and values being the average temps. 
    Finally, we print the elements in decades to 2 decimal places.
    '''
    for row in reader:
        year= int(row[0])
        
        decade = year // 10 * 10
        decade_temps.append(float(row[1]))

        if year % 10 == 9:
            avg_temp = sum(decade_temps) / len(decade_temps)

            decades[decade] = avg_temp

            # Reset the list for the next decade
            decade_temps = []

    for decade, avg_temp in decades.items():
        print(f'{decade}s: {avg_temp:.2f}')