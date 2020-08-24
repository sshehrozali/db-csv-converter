# PYTHON SCRIPT TO CONVERT .CSV FILE TO .DB FILE # (Developed By Syed Shehroz Ali)
# Import Libraries
import csv
import sqlite3
from sys import exit
from alpha import test_alpha

def csv_to_db():

    # UI Menu
    print("\n---| CSV TO DB |---\n")
    print("1. Convert     2.Exit\n")
    print("======================\n")

    # Main loop until user exits
    while (True):

        # Prompt for option
        ask = input("Type Option: ")

        # If "2", exit the program
        if ask == "2":

            print("\nOperation Cancelled by the USER\n\n")
            exit(1)

        # If "1", execute the program
        if ask == "1":

            # Keep prompting for valid CSV filename
            while (True):

                print("\nEnter without .(extension)")
                csv_filename = input("\nCSV Filename: ")

                check = test_alpha(csv_filename)

                if check == True:
                    break

                print("\nPlease Enter Correct Filename!\n")

            # Keep prompting for valid database filename
            while (True):

                print("\nEnter without .(extension)")
                db_filename = input("\nNew Database Filename: ")

                check = test_alpha(db_filename)

                if check == True:
                    break

                print("\nPlease Enter Correct Filename!\n")

            # Keep prompting for valid table name
            while (True):

                print("\nJust Don't write 'table'")
            
                table_name = input("\nEnter Table Name: ")

                check = test_alpha(table_name)

                if check == True:
                    break

                print("\nPlease Enter Correct Table Name!\n")

            # Define connection to sqlite3 database
            connection = sqlite3.connect(f"{db_filename}.db")

            # Cursor to connect to database
            cursor = connection.cursor()

            # Create table [CHANGE COLUMN NAMES HERE]
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (ID integer, First text, Middle text, Last text, Age integer, Class integer, Father text, Number integer)")

            # Open CSV file [ENTER CSV FILENAME HERE]
            with open(f"PUT YOUR CSV FILE HERE/{csv_filename}.csv") as file:

                # Read all contents as Dict
                reader = csv.DictReader(file)

                # Iterate row by row
                for row in reader:

                    # Insert each row in database table [CHANGE NAMES HERE]
                    cursor.execute(f"INSERT INTO {table_name} (ID, First, Middle, Last, Age, Class, Father, Number) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (row['ID'], row['First'], row['Middle'], row['Last'], row['Age'], row['Class'], row['Father'], row['Number']))
                    connection.commit()

                # Print Success, exit the program
                print("\nAll records exported Successfully!")
                print("Check your current directory for the generated .db file\n")
                print("Developed By Syed Shehroz Ali\n")
                exit(0)

        # If not correct option is passed
        print("\nPlease Enter Correct Option!\n")