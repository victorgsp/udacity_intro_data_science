import csv

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file by downloading these files from the resources:
    
    Sample input file: turnstile_110528.txt
    Sample updated file: solution_turnstile_110528.txt
    '''
    for name in filenames:
        with open(name, 'rb') as f:
            reader = csv.reader(f)
            arrayToWrite = []
            for row in reader:
                rowStart = [row[0],row[1],row[2]]
                count = 0
                newRow = [] + rowStart
                for i in range(3,len(row)):
                    newRow.append(row[i].strip())
                    count = count + 1
                    if(count == 5):
                        count = 0
                        arrayToWrite.append(newRow)                
                        newRow = [] + rowStart
            writeFile(arrayToWrite, 'updated_' + name)

def writeFile(outputData, filename):
    with open(filename, mode='w') as outputFile:
        data_writer = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in outputData:
            data_writer.writerow(row)    
        

fix_turnstile_data(["turnstile_Test.txt"])