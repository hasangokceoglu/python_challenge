import os
import csv
import pandas as pd


from google.colab import files
files.upload()
count_row=0
total_p_l=0
change=0
change_list=[]
delta_list=[]
with open('budget_data.csv') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is row header)
    csv_header = next(csvreader)

    
    # Count each row of data after the header
    for month in csvreader:
        count_row = count_row + 1 
        
        # Sum profit/loss    
        total_p_l=total_p_l+int(month[1]) 

     
        # change average calculation
        change_list.append(month[1])

    for x in range(len(change_list)):
          if x < len(change_list)-1:
            fv=change_list[x]
            sv=change_list[x+1]
            delta=int(sv)-int(fv)
            delta_list.append(delta)
    
    #change calculations    
    average_change=sum(delta_list)/len(delta_list)
    
    greatest_increase=max(delta_list)
    max_index = delta_list.index(max(delta_list))

    greatest_decrease=min(delta_list)
    min_index = delta_list.index(min(delta_list))
    #print results

    print(f"Total Months:", (count_row))
    print(f"Total Profit/Loss:$",(total_p_l)) 
    print(f"Average Change:$",(average_change)) 
    print(f"Greatest Increase:$",(greatest_increase)) 
    print(f"Greatest Decrease:$",(greatest_decrease)) 
