"""Unittests for review"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test suite for the Review class."""

    def setUp(self):
        """Set up for the tests."""
        self.review = Review()

    def test_instance_creation(self):
        """Test instance creation and attributes."""
        self.assertIsInstance(self.review, Review)
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))


if __name__ == '__main__':
    unittest.main()
