"""
Course: CST8002
Assignment: Practical Project 02
Author: Khalil Toure
Description: Business layer for managing mercury records.
"""

class MercuryManager:

    def __init__(self):
        self.records = []

    def load_records(self, records):
        self.records = records

    def add_record(self, record):
        self.records.append(record)

    def get_records(self):
        return self.records

    def display_records(self):
        if len(self.records) == 0:
            print("No records found")
        else:
            for index, record in enumerate(self.records, start=1):
                print(f"Record #{index}")
                record.display()

    def edit_record(self, index, new_record):
        if 0 <= index < len(self.records):
            self.records[index] = new_record
            print("Record updated successfully")
        else:
            print("Invalid record number")

    def delete_record(self, index):
        if 0 <= index < len(self.records):
            self.records.pop(index)
            print("Record deleted successfully")
        else:
            print("Invalid record number")