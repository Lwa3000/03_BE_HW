#By: Lena Corredor
#Description:This script calculates the following values from a two column csv file with fields: date and revenue
# * The total number of months included in the dataset

# * The total amount of revenue gained over the entire period

# * The average change in revenue between months over the entire period

# * The greatest increase in revenue (date and amount) over the entire period

# * The greatest decrease in revenue (date and amount) over the entire period

import os
import csv
from decimal import Decimal

#File path
file_path=os.path.join("PyBank","raw_data","budget_data_2.csv")

#Initialize variables
date=[]
end_date=[]
rev=[]
tot_months=0
tot_rev=0
avg_rev=0
max_rev=0
min_rev=0
max_rev_date=""
min_rev_date=""
rev_first_value=[]
rev_second_value=[]

#calculation variables
month_list=[]
rev_change_list=[]
rev_change_date_list=[]

#Open file and extract data to 2 lists
with open(file_path,newline="") as file:
    csvreader=csv.reader(file,delimiter=",")

    # This skips the first row of the CSV file.
    next(csvreader)

    for row in csvreader:
        date.append(row[0])
        rev.append(int(row[1]))

#Calculate the values
#To calculate total months 
for each in date:
    if each in month_list:
        print("There is duplicate rows of months, please fix data.")
    else:
        month_list.append(each)
        tot_months=tot_months+1

#To calculate total revenue

for each in rev:
    tot_rev=tot_rev+each

#To calculate average revenue change
rev_second_value=rev[:]
rev_first_value=rev[:]
end_date=date[:]
del rev_second_value[0]
del rev_first_value[-1]
del end_date[0]

change_pairs=zip(rev_first_value,rev_second_value,end_date)

tot_change=0
count=0

for i,j,k in change_pairs:
    rev_change_list.append(j-i)
    rev_change_date_list.append(k)
    count=count+1
    tot_change=tot_change+j-i

#Set average revenue to 2 decimal places
avg_rev=round(Decimal(tot_change/count),2)
change_and_date=zip(rev_change_list,rev_change_date_list)

#Find greatest increase and greatest decrease in revenue
for i,j in change_and_date:
    if i> max_rev:
        max_rev=i
        max_rev_date=j
    else:
        pass
    if i< min_rev:
        min_rev=i
        min_rev_date=j
    else:
        pass


#Output the results
print("Financial Analysis \n----------------------------")
print("Total Months: "+str(tot_months))
print("Total Months: $"+str(tot_rev))
print("Average Revenue Change: $"+str(avg_rev))
print("Greatest Increase in Revenue: $"+max_rev_date+" ("+str(max_rev)+")")
print("Greatest Decrease in Revenue: $"+min_rev_date+" ("+str(min_rev)+")")

output_path = os.path.join('PyBank', 'PyBank_results.txt')
with open(output_path, 'w', newline='') as output_file:

    output_file.write("Financial Analysis \n----------------------------")
    output_file.write("\nTotal Months: "+str(tot_months))
    output_file.write("\nTotal Months: $"+str(tot_rev))
    output_file.write("\nAverage Revenue Change: $"+str(avg_rev))
    output_file.write("\nGreatest Increase in Revenue: $"+max_rev_date+" ("+str(max_rev)+")")
    output_file.write("\nGreatest Decrease in Revenue: $"+min_rev_date+" ("+str(min_rev)+")")