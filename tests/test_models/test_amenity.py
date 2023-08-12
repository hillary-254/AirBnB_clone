"""Unittest for amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test suite for the Amenity class."""

    def setUp(self):
        """Set up for the tests."""
        self.amenity = Amenity()

    def test_instance_creation(self):
        """Test instance creation and attributes."""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")


if __name__ == '__main__':
    unittest.main()
