import os
import csv

csv_path = os.path.join("C:/Users/hasan/Data Analytics/Projects/Modules/Week3/Week 3 Challenge/GitHub clone/python_challenge/Pypoll/Resources", 'election_data.csv')

#variables assigment

count_row=0
candidate=[]
poll_list=[]

vote_counter=-1

Charles_count= 0
Diana_count= 0
Raymon_count= 0

Charles_percent= 0
Diana_percent= 0
Raymon_percent= 0

with open(csv_path) as csvfile:

    # CSV reader 
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Count each row of data after the header
    for row in csvreader:
      count_row = count_row + 1 
      vote_counter += 1 
      # count of polls
  

      if row[2] == "Charles Casper Stockham":
            Charles_count += 1
      elif row[2] == "Diana DeGette":
            Diana_count += 1
      elif row[2] == "Raymon Anthony Doane":
            Raymon_count += 1
        
    results = {"Charles Casper Stockham":Charles_count, "Diana DeGette":Diana_count, "Raymon Anthony Doane":Raymon_count}

# percentage calculation

    Charles_percent = round((Charles_count / vote_counter) * 100, 3)
    Diana_percent = round((Diana_count / vote_counter) * 100, 3)
    Raymon_percent = round((Raymon_count / vote_counter) * 100, 3)

    # find winner
    winner = max(results, key=results.get)
      

       #print results
    print("Election Results")
    print("---------------------")
    print(f"Total Votes:", (count_row))
    print("---------------------")
    print(f"Charles Casper Stockham: %", (Charles_percent) ,(Charles_count) )
    print(f"Diana DeGette: %", (Diana_percent) ,(Diana_count) )
    print(f"Raymon Anthony Doane: %", (Raymon_percent) ,(Raymon_count) )
    print("---------------------")
    print(f"Winner:" ,(winner))

with open("C:/Users/hasan/Data Analytics/Projects/Modules/Week3/Week 3 Challenge/GitHub clone/python_challenge/PyPoll/analysis/analysis.txt",'w') as text:
    text.write("Election Results \n")
    text.write("--------------------\n")
    text.write("Charles Casper Stockham: %" + str(Charles_percent) + str(Charles_count) + "\n" )
    text.write("Diana DeGette: %" + str(Diana_percent) + str(Diana_count) + "\n")
    text.write("Raymon Anthony Doane: %" + str(Raymon_percent) + str(Raymon_count) + "\n" )
    text.write("--------------------- \n")
    text.write("Winner:" + winner )
