# PYTHON SCRIPT TO CONVERT .DB FILE TO .CSV FILE # (Developed By Syed Shehroz Ali)
# Import Libraries
import csv
import sqlite3
from alpha import test_alpha
from sys import argv, exit

def db_to_csv():

    # UI Menu
    print("\n---| DB TO CSV |---\n")
    print("1. Convert     2.Exit\n")
    print("======================\n")

    # Keep prompting till valid input
    while (True):

        # Prompt for option
        ask = input("Type Option: ")

        # If no, exit program
        if ask == "2":
            print("\nOperation Cancelled by the user\n\n")
            exit(1)
    
        # If yes, execute below code, generate .csv file in current directory
        if ask == "1":

            # Keep prompting for valid CSV filename
            while (True):

                print("\nEnter without .(extension)")
                csv_filename = input("\nNEW CSV Filename: ")

                check = test_alpha(csv_filename)

                if check == True:
                    break       

            # Keep prompting for valid database filename
            while (True):

                print("\nEnter without .(extension)")
                db_filename = input("\nDatabase Filename: ")

                check = test_alpha(db_filename)

                if check == True:
                    break

                print("\nPlease Enter Correct Filename!\n")

            # Print New-line
            print()

            # Connection to sqlite3 database file
            connection = sqlite3.connect(f"PUT YOUR DATABASE FILE HERE/{db_filename}.db")

            # Cursor to connect to database
            cursor = connection.cursor()

            # Select all data from database file [CHANGE TABLE NAME HERE]
            database = cursor.execute("SELECT * from students")

            # Fetch all data as nested Lists
            students_data = database.fetchall()

            # Create fieldnames for CSV file
            fieldnames = ["ID", "First", "Middle", "Last", "Age", "Class", "Father's Name", "Phone Number"]

            # Declare filename for CSV file
            filename = f"{csv_filename}.csv"

            # Open CSV file as Write mode
            with open(filename, "w") as csvfile:

                # CSV writer object
                csv_writer = csv.writer(csvfile)

                # Write fieldnames to CSV file
                csv_writer.writerow(fieldnames)

                # Write each row in CSV file
                csv_writer.writerows(students_data)

                print("All records exported Successfully!")
                print("Check your directory for the generated .csv file\n")
                print("Developed By Syed Shehroz Ali\n\n")

            # Close CSV file, Exit program Successfully
            csvfile.close()
            exit(0)

        # Else
        print("Type Correct Option!\n")

