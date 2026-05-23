"""
Course: CST8002
Assignment: Practical Project 02
Author: Khalil Toure
Description: Unit test for MercuryManager.
"""

import unittest

from business.mercury_manager import MercuryManager
from model.mercury import MercuryRecord


class TestMercury(unittest.TestCase):

    def test_add_record(self):
        manager = MercuryManager()

        record = MercuryRecord(
            "Test Site", "1", "2025", "60", "70",
            "10", "5", "3", "2", "1"
        )

        manager.add_record(record)

        self.assertEqual(len(manager.get_records()), 1)


if __name__ == "__main__":
    unittest.main()