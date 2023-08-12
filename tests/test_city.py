"""Unittests for city"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test suite for the City class."""

    def setUp(self):
        """Set up for the tests."""
        self.city = City()

    def test_instance_creation(self):
        """Test instance creation and attributes."""
        self.assertIsInstance(self.city, City)
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")


if __name__ == '__main__':
    unittest.main()
