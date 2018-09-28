import os
import csv

# Path to collect data from the Resources folder
budgetCSV = os.path.join('.', 'Resources', 'budget_data.csv')
# Read in the CSV file

with open(budgetCSV, 'r') as csvfile:

    # Split the data on commas
    budget = csv.reader(csvfile, delimiter=',')

    header = next(budget)
     
    k=[]
    
    for row in budget:
        k.append(int(row[1]))
        
   
    z=[]
    for y in range(len(k)-1):
        z.append(k[y+1]-k[y])
        avg=sum(z)/len(z)
        
    a=max(z)
    b=min(z)










# Read in the CSV file
with open(budgetCSV, 'r') as csvfile:

    # Split the data on commas
    budget = csv.reader(csvfile, delimiter=',')

    header = next(budget)
    
    record=0
     # Read each row of data after the header
    for row in budget:
        if len(row)==0:
            record=record+0
        else: 
            record=record+1



# Read in the CSV file
with open(budgetCSV, 'r') as csvfile:

    # Split the data on commas
    budget = csv.reader(csvfile, delimiter=',')

    header = next(budget)
    
    total=0
     # Read each row of data after the header
    for row in budget:
        total=total+int(row[1])