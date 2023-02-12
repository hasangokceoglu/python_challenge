import os
import csv

resource_path = os.path.join('/Users/hasan/Data Analytics/Projects/Modules/Week3/Week 3 Challenge/Instructions/PyBank/Resources')

import os
import csv
import pandas as pd


from google.colab import files
files.upload()
count_row=0
total_p_l=0
change=0
with open('budget_data.csv') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
   # print(f"CSV Header: {csv_header}")

    # Count each row of data after the header
    for month in csvreader:
        count_row = count_row + 1 
        
        # Sum profit/loss    
        total_p_l=total_p_l+int(month[1]) 

        # change average calculation
       
       

    #print results

    print(f"Total Months:", (count_row))
    print(f"Total Profit/Loss:$",(total_p_l))  
    print(change) 
