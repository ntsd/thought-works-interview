from trains.trains import Trains

import unittest


class TestTrains(unittest.TestCase):
    
    def setUp(self):
        self.test_input = Trains("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7") 


if __name__ == "__main__":
    unittest.main()
