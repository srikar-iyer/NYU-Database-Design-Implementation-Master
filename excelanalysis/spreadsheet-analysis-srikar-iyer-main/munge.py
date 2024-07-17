'''
Srikar Iyer - Spreadsheet Assignment - Database Systems and Implementation
Opens two files: the file with the NASA Weather data to read, and the empty csv file to write
the munged data in. The inputfile takes the file as input and outputfile returns a new csv.
'''
with open("data/readme.txt", 'r') as inputfile, open("data/clean_data.csv", 'w') as outputfile:

    '''We create a file in read mode to read the raw data, then munge, and write the cleaned data in a csv with write mode.
    '''
    for line in inputfile:
        '''Cleans data in each line
        '''
        if line.__contains__("s,s"):
            continue
        '''Removes rows with incomplete indices, and writes the resulting row without the first element. Because .split removes the comma
        in csv files, it must be re-added before .join
        '''
        outputfile.write(",".join(line.split(",")[1:]))