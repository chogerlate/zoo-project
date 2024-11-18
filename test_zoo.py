import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_invalid_age_ticket_price(self):
        """Test ticket price for invalid age (negative)"""
        self.assertEqual(self.zoo.get_ticket_price(-1), 0)

    def test_child_ticket_price(self):
        """Test ticket price for children (age <= 12)"""
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_teenager_ticket_price(self):
        """Test ticket price for teenagers (13-20)"""
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_adult_ticket_price(self):
        """Test ticket price for adults (21-60)"""
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_senior_ticket_price(self):
        """Test ticket price for seniors (age >= 61)"""
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()