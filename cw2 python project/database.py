import csv
import sqlite3
import os

# Create a db
conn = sqlite3.connect('scheduledata.db')
cursor = conn.cursor()

table_name = "schedule"

csv_folder = "raw_datas"

# putting csv files database
csv_files = [file for file in os.listdir(csv_folder) if file.endswith(".csv")]

for csv_file in csv_files:
    csv_path = os.path.join(csv_folder, csv_file)

    # Open the CSV file
    with open(csv_path, 'r') as file:
        csv_reader = csv.reader(file)

        next(csv_reader)

        # Insert data into the common table
        for row in csv_reader:
            # Generating the insert statement for the  table
            insert_sql = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(row))});"
            cursor.execute(insert_sql, row)


    def retrieve():
        conn = sqlite3.connect('scheduledata.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {table_name}")
        schedule_data = cursor.fetchall()

        conn.close()

        return schedule_data
# Commit changes and close
conn.commit()
conn.close()



