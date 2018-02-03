#By: Lena Corredor - Wed, Jan 31,2018
#Description: This script converts employee records to the required format.
# * In summary, the required conversions are as follows:

#   * The `Name` column should be split into separate `First Name` and `Last Name` columns.

#   * The `DOB` data should be re-written into `DD/MM/YYYY` format.

#   * The `SSN` data should be re-written such that the first five numbers are hidden from view.

#   * The `State` data should be re-written as simple two-letter abbreviations.

import os
import csv

#set file path
file_path=os.path.join("PyBoss","raw_data","employee_data2.csv")

#initialize variables
empID=[]
name=[]
dob=[]
ssn=[]
state=[]

#open file and extract data
with open(file_path)as file:
    csvreader=csv.reader(file,delimiter=",")

    # This skips the first row of the CSV file.
    next(csvreader)

    for row in csvreader:
        empID.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])

#convert data
#split name column
first_name=[]
last_name=[]
for each in name:
    first_name.append(each.split()[0])
    last_name.append(each.split()[1])

#reformat DOB
for each in dob:
    each=each.split("-")[1]+"/"+each.split("-")[2]+"/"+each.split("-")[0]

#reformat SSN
new_ssn=[]
for each in ssn:
    new_ssn.append("***-**-"+each[7:11])

#reformat state
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
new_state=[]
for each in state:
    if each in us_state_abbrev:
        new_state.append(us_state_abbrev[each])
    else:
        print("State is incorrect!")
        new_state.append("XX")

#output new data
output_path=os.path.join("PyBoss","raw_data","output_PyBoss2.csv")
reformatted_csv=zip(empID,first_name,last_name,dob,new_ssn,new_state)

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB",
                     "SSN", "State"])
    csvwriter.writerows(reformatted_csv)