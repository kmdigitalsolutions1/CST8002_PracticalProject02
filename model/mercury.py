"""
Course: CST8002
Assignment: Practical Project 02
Author: Khalil Toure
Description: Model class for mercury records.
"""

class MercuryRecord:

    def __init__(self, SiteName, SiteNumber, Year, Latitude, Longitude,
                 Water_Column_Depth, THg, GEM, Methylated_Hg, DMHg):
        self.SiteName = SiteName
        self.SiteNumber = SiteNumber
        self.Year = Year
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.Water_Column_Depth = Water_Column_Depth
        self.THg = THg
        self.GEM = GEM
        self.Methylated_Hg = Methylated_Hg
        self.DMHg = DMHg

    def display(self):
        print(f"Site Name: {self.SiteName}")
        print(f"Site Number: {self.SiteNumber}")
        print(f"Year: {self.Year}")
        print(f"Latitude: {self.Latitude}")
        print(f"Longitude: {self.Longitude}")
        print(f"Water Column Depth: {self.Water_Column_Depth}")
        print(f"THg: {self.THg}")
        print(f"GEM: {self.GEM}")
        print(f"Methylated Hg: {self.Methylated_Hg}")
        print(f"DMHg: {self.DMHg}")
        print("-" * 40)