"""
Course: CST8002
Assignment: Practical Project 02
Author: Khalil Toure
Description: Main controller for Mercury Concentration Management System.
"""

from business.mercury_manager import MercuryManager
from model.mercury import MercuryRecord
from persistence.csv_reader import CSVReader
from persistence.csv_writer import CSVWriter
from presentation.menu import display_menu


DATA_FILE = "data/NCP_ArcticMarineEcosystems_Mercury_Concentrations_EN_FR.csv"


def create_record_from_input():
    site = input("Site Name: ")
    number = input("Site Number: ")
    year = input("Year: ")
    latitude = input("Latitude: ")
    longitude = input("Longitude: ")
    depth = input("Water Column Depth: ")
    thg = input("THg: ")
    gem = input("GEM: ")
    methyl = input("Methylated Hg: ")
    dmhg = input("DMHg: ")

    return MercuryRecord(
        site, number, year, latitude, longitude,
        depth, thg, gem, methyl, dmhg
    )


def main():
    manager = MercuryManager()
    reader = CSVReader(DATA_FILE)
    writer = CSVWriter()

    records = reader.read_first_100_records()
    manager.load_records(records)

    print("Mercury Concentration Management System")
    print("--------------------------------------")
    print("Program by Khalil Toure")
    print("Loaded records:", len(manager.get_records()))

    while True:
        display_menu()

        choice = input("Enter choice: ")

        if choice == "1":
            manager.display_records()

        elif choice == "2":
            record = create_record_from_input()
            manager.add_record(record)
            print("Record added successfully")

        elif choice == "3":
            try:
                record_number = int(input("Enter record number to edit: "))
                new_record = create_record_from_input()
                manager.edit_record(record_number - 1, new_record)
            except ValueError:
                print("Please enter a valid number")

        elif choice == "4":
            try:
                record_number = int(input("Enter record number to delete: "))
                manager.delete_record(record_number - 1)
            except ValueError:
                print("Please enter a valid number")

        elif choice == "5":
            writer.save_records(manager.get_records())

        elif choice == "6":
            print("Total records:", len(manager.get_records()))

        elif choice == "7":
            records = reader.read_first_100_records()
            manager.load_records(records)
            print("Data reloaded successfully")
            print("Loaded records:", len(manager.get_records()))

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()