"""
Course: CST8002
Assignment: Practical Project 02
Author: Khalil Toure
Description: Persistence layer for saving CSV data using UUID.
"""

import csv
import uuid


class CSVWriter:

    def save_records(self, records):
        filename = str(uuid.uuid4()) + ".csv"

        try:
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                writer.writerow([
                    "SiteName", "SiteNumber", "Year", "Latitude", "Longitude",
                    "Water_Column_Depth", "THg", "GEM", "Methylated_Hg", "DMHg"
                ])

                for record in records:
                    writer.writerow([
                        record.SiteName,
                        record.SiteNumber,
                        record.Year,
                        record.Latitude,
                        record.Longitude,
                        record.Water_Column_Depth,
                        record.THg,
                        record.GEM,
                        record.Methylated_Hg,
                        record.DMHg
                    ])

            print("Records saved to", filename)

        except Exception as error:
            print("Error saving records:", error)