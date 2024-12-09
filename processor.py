import openpyxl
import psycopg2

# Given a list of accounts numbers to be validated in an hipothetic DBs with card numbers or cvv or something like that.
#  We are commissioned to create a script to read the list of values stored in the column A (thinking about an .xlsx file) and then
#  query the database with every account number and in case it has a card number or CVV asigned in the  DB we should write this
#  just next to the account number in the file. 

# Connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="dbname",
    user="username",
    password="password",
    host="domain",
    port="portnumber"
)

# Create a cursor object
cur = conn.cursor()

# Load the workbook and select the active worksheet
workbook = openpyxl.load_workbook('file name.xlsx')
sheet = workbook.active

# Iterate through the rows and print values
index = 1
for row in sheet.iter_rows(min_row=1, max_row=29026, min_col=1, max_col=1):
    for cell in row:

        #We are taking accounts numbers from the cell in the file with the format of xxx , xxxx , xxxx.
        #As we need to search with the format of (idsuc, idprod, idaux) we'll need to split the parameters up to set up the query.
        account = cell.value.split(',');

        print(account)

        print('Executing the query..')
        # Execute a SELECT query to fetch the 'name' field 
        cur.execute("select cc.cvv as cvv from credit_card where (idsucursal, idproducto, idauxiliar) = ( %s, %s, %s)", (str(account[0]), str(account[1]), str(account[2])))

        print('Fetching results to be printed')
        row = cur.fetchone()

        # Check if a row was fetched 
        if row: 
            clabe = row[0] 
            sheet['B' + str(index)] = str(clabe)
        else: 
            sheet['B' + str(index)] = 'No data returned'

        #Saving changes made on the .xlsx file
        workbook.save('file name.xlsx')
        print('index: ' + str(index))
        index += 1
    print()


# Closing the resources before opened 
cur.close() 
conn.close()
