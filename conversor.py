import csv

#During this opportunity I was working on a solution for the scenario described below....
#Our client provided us two files with the structured described below...
#First file had three columns two of them were so important for us...

#|   ID  |   accountholder_number    |   account_number  |
#|   1   |   123456-332212           |   654321          |

#Then we had a second file with next structed

#|  consecutive_number  |   code    |
#|  332212              |   443322  |

#Here we have to contactenate the preffix 123456- (it always be the same) plus the consecutive_number value from the second file
#Once we had this number and for this example we can say that the results could be the example above (123456-332212)
#we had to take the account_number from the first file and update this account we the code from the second file.

#To do this in the simpler manner I found I decided to create a new file (the third) with the account_number, and code into a csv file

first_file_data = {}
with open('clientnumber-and-accountnumber-file.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        accountholder_number = row[1]
        account_number = row[2]
        first_file_data[accountholder_number] = account_number

with open('suffix-with-code.csv', mode='r') as clabe_file, open('results.csv', mode='w', newline='') as ultimate_file:
    reader = csv.reader(clabe_file)
    writer = csv.writer(ultimate_file)

    for row in reader:
        third_part = row[0]
        clabe = row[1]

        accountholder_number = f'100-10-{third_part}'

        if accountholder_number in first_file_data:
            account_number = first_file_data[accountholder_number]

            writer.writerow([account_number, clabe])
        else:
            print(f"{accountholder_number} not found in first_file_data collection")