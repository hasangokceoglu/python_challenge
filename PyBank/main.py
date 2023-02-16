import os
import csv

csv_path = os.path.join('Resources', 'budget_data.csv')

#variables assigment
count_row=0
total_p_l=0
change_list=[]
month_list=[]
delta_list=[]

with open (csv_path) as csvfile:

    
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row
    csv_header = next(csvreader)

    
    # Count each row of data after the header
    for month in csvreader:
        count_row = count_row + 1
        
        # Sum profit/loss
        total_p_l=total_p_l+int(month[1])

     
        # change average calculation
        change_list.append(month[1])
        month_list.append(month[0])

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
    print("Financial Analysis")
    print("--------------------")
    print(f"Total Months:", (count_row))
    print(f"Total Profit/Loss:$", (total_p_l)) 
    print(f"Average Change:$", (round(average_change,2))) 
    print(f"Greatest Increase:$", (month_list[max_index+1]) , (greatest_increase)) 
    print(f"Greatest Decrease:$", (month_list[min_index+1]) , (greatest_decrease)) 

with open('analysis/analysis.txt",'w') as text:
    text.write("Financial Analysis \n")
    text.write("--------------------\n")
    text.write("Total Months:" + str(count_row) + "\n")
    text.write("Total Profit/Loss:$" + str(total_p_l) + "\n") 
    text.write("Average Change:$" + str(round(average_change,2)) + "\n") 
    text.write("Greatest Increase:$"  +  str(month_list[max_index+1])  +   "(" + str(greatest_increase) +")" + "\n") 
    text.write("Greatest Decrease:$"  + str(month_list[min_index+1])  +  "(" + str(greatest_decrease) + ")" + "\n")
