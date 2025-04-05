import mysql.connector
from mysql.connector import errorcode
import csv

def execute_sql_script(filename, connection):
    """
    Execute an SQL script file using the provided database connection.
    """
    print(f"Executing {filename}...")
    with open(filename, 'r', encoding='utf-8') as file:
        sql_script = file.read()
    
    # Split the script into commands
    commands = sql_script.split(';')
    
    cursor = connection.cursor()
    for command in commands:
        try:
            if command.strip():
                cursor.execute(command)
        except mysql.connector.Error as err:
            print(f"Failed executing command: {command}")
            print(f"Error: {err}")
    
    cursor.close()
    connection.commit()
    print(f"Successfully executed {filename}.")

def export_to_csv(cursor, filename="exported_data.csv"):
    """
    Export data from the database to a CSV file.
    """
    query = "SELECT * FROM jobs"  # Adjust this query based on your table and columns
    cursor.execute(query)
    rows = cursor.fetchall()
    
    # Get column headers
    column_headers = [i[0] for i in cursor.description]
    
    # Write to CSV
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(column_headers)  # Write the headers first
        writer.writerows(rows)
    print(f"Data exported to {filename} successfully.")

def main():
    # Database configuration
    config = {
        'user': 'root',
        'password': 'pwd',
        'host': 'localhost',
        'port': '3306',
        'database': 'template_db'
    }

    try:
        # Establish a database connection
        connection = mysql.connector.connect(**config)
        print("Successfully connected to the database.")
        
        # Execute SQL scripts
        execute_sql_script('setup.sql', connection)
        execute_sql_script('data.sql', connection)
        
        # Export data to CSV
        cursor = connection.cursor()
        export_to_csv(cursor)
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()