import sqlite3

# Connect to the SQLite database

con = sqlite3.connect("database.db")

c = con.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS employees (

first TEXT,

last TEXT,

pay INTEGER)''')

# Insert data into the 'employees' table

c.execute("INSERT INTO employees VALUES ('Ali' , 'Akbar' , 80000)")

c.execute("INSERT INTO employees VALUES ('Ahmed' , 'Ali' , 50000)")

# Commit the insertions

con.commit()

# Retrieve and display all employees with last name 'Javaid'

c.execute("SELECT * FROM employees WHERE last = 'Ali'")

# Fetch multiple rows (you can specify how many rows to fetch in fetchmany)

print(c.fetchmany(2)) # Fetch two rows

# Close the connection

con.close()
