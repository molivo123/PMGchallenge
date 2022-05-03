import os
import pandas as pd
import csv
import sys

#Did not have much time over past day with work/school, but hope this is sufficient
#also not sure how to submit link so posting on github
#if had more time would've available with CI/CD testing and Unit testing

#so previous combine isn't in file list, allows script to be run multiple times with not extra entries
if (os.path.exists('combine_csv.csv')):
    os.remove('combine_csv.csv')

#empty list to store csv data
csv_list = []

#counter
i=0

#reads file path from command line and adds appends to
#assigns new column File_Name which takes in name of file as value
#for loop reads each argument and only stops after one less than length of arguments
for sys.argv[i] in range(len(sys.argv)-1):
    i+=1
    csv_list.append(pd.read_csv(sys.argv[i]).assign(File_Name = os.path.basename(sys.argv[i])))


# merging list of csv data into one large panda df, ignore index as not necessary
csv_merged = pd.concat(csv_list, ignore_index=True)

# saving mergered csv to file name, again removing index, stores output in same location as script
with open('combine_csv.csv', 'w+', newline='') as file:
    file.truncate()
    csv_merged.to_csv('combine_csv.csv', index=False)
