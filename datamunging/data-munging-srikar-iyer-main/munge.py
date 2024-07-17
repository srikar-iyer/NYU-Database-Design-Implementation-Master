'''
Srikar Iyer - Data Munging Assignment - Database Systems and Implementation
Opens two files: the file with the NASA Weather data to read, and the empty csv file to write
the munged data in. The inputfile takes the file as input and outputfile returns a new csv.
'''
with open("data/readme.txt", 'r') as inputfile, open("data/clean_data.csv", 'w') as outputfile:

    '''We directly define the heading since it only appears once, and is easier to deal with this way
    Because the logic of the munging revolves around deleting text, it is fine to directly
    input the heading. The delimiter of the csv is chosen to be commas since the csv is more readable
    '''
    outputfile.write('Year,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec,J-D,D-N,DJF,MAM,JJA,SON\n')

    for line in inputfile:
        '''The choice is made to delete the *. This is because the missing annual means in 1880
        contaminate the entire row by bringing uncertainty as to how reliable the input data  for 
        1880 is. Also, .contains() returns a boolean based off of the input
        '''
        if line.__contains__("*"):
            continue
        '''This block first checks if the line consists of only numbers and the first 4 indices are 
        numbers; this indicates years, signaling the start of the data. (this is because all of the 
        data starts with a year.)
        In the data defined, the munging begins : .strip() removes the leading and trailing spaces,
        .split() turns the line into a list of the individual strings and deletes the middle spaces, 
        .join concatinates the strings in the list with a set number of spaces, and \n
        adds a new line per line, maintaining structural integrity. Then, for all but the first and last
        elements (which represent the year), the data in milliCelsius is converted to farenheit by 
        f(x)=x*0.01*1.8=0.018x. Each number in each line is casted to float, multiplied by 0.018, 
        formatted with .format to round to 1 decimal, and recasted to str. Then, we remove the last 
        year column with .split()[:-1] since negative indices return to the last col, and take this 
        aptly named 'result', and add the comma delimiters here. Finally, we write the final string, 
        resultStr, into the aforementioned csv with .write
        '''
        if line[0].isdigit and line[0:4].isdigit():
            rawLine = " ".join(line.strip().split()) + '\n'
            rawLine = rawLine.split()
            for i in range(1, len(rawLine)-1):
                rawLine[i] = str('{x:.1f}'.format(x=float(rawLine[i]) * 0.018 ))
                
            result = " ".join(rawLine).split()[:-1]
            resultStr= ','.join(result) + '\n'
            outputfile.write(resultStr)