""" CST8002 Practical Project 2
 Course: CST8002
 Author: Khalil Toure"""

import csv
import glob
import os
from model.mercury import MercuryRecord


class CSVReader:

    def __init__(self, file_path=None):
        self.file_path = file_path

    def find_csv_file(self):
        if self.file_path is not None and os.path.exists(self.file_path):
            return self.file_path

        csv_files = glob.glob("**/*.csv", recursive=True)

        if len(csv_files) == 0:
            print("Dataset file not found.")
            return None

        return csv_files[0]

    def read_first_100_records(self):
        records = []
        count = 0

        filename = self.find_csv_file()

        if filename is None:
            return records

        print("Loading file:", filename)

        try:
            with open(filename, "r", newline="", encoding="utf-8-sig") as file:
                reader = csv.reader(file)

                next(reader, None)

                for row in reader:
                    if count >= 100:
                        break

                    if len(row) < 10:
                        continue

                    record = MercuryRecord(
                        row[0], row[1], row[2], row[3], row[4],
                        row[5], row[6], row[7], row[8], row[9]
                    )

                    records.append(record)
                    count += 1

        except FileNotFoundError:
            print("Dataset file not found.")

        except Exception as error:
            print("Error reading dataset:", error)

        return records