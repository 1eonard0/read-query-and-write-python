import csv
import psycopg2
from psycopg2 import IntegrityError
from datetime import datetime

#Described the conversor script we can just say that this little script will read the results.csv file created before
#Then we update every account with the right code in the DB.
#And in case of any duplication constraint error it will be reported in an error.csv file
#printing the account number and the error message.

# Connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="dbname",
    user="username",
    password="password",
    host="host",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()
counter = 0;
print(f"Execution started at {datetime.now()}")
with open('results.csv', mode='r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        
        account_number = str(row[0])
        try:
            # Executing the update query 
            cur.execute("UPDATE account_user SET clabe=%s WHERE account_number=%s", (str(row[1]), account_number)) 
        
            # Commit the changes 
            conn.commit() 
        
            # Check the number of rows affected 
            rows_affected = cur.rowcount

            if rows_affected > 0: 
                print("Update successful. " + str(rows_affected) + " row(s) affected.") 
                counter += rows_affected
                print(f"Register inserted {counter}")
        
        except IntegrityError as e:
 
            conn.rollback()
            # Write to the CSV file 
            with open('error.csv', mode='a', newline='') as file: 
                writer = csv.writer(file) 
                # Write the data 
                writer.writerows([[str(row[0]), str(row[1]), 'duplicate key value violates unique constraint "clabe_unique"']])

cur.close() 
conn.close()