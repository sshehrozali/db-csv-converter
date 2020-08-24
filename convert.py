# Import Libraries and Functions
from sys import exit
from script import csv_to_db
from script1 import db_to_csv

# UI Menu
print("\n================================")
print("         DB/CSV - CONVERTER")
print("==================================\n")
print("1.Convert .DB to .CSV")
print("2.Convert .CSV to .DB\n")

# Prompt for valid option
while (True):

    # Ask for input
    ask = input("Type Option: ")

    # DB_to_CSV
    if ask == "1":

        db_to_csv()

    # CSV_to_DB
    if ask == "2":

        csv_to_db()

    # If wrong option is provided
    print("\nEnter Correct Option!\n")