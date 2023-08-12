"""Unittests for user"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test suite for the User class."""

    def setUp(self):
        """Set up for the tests."""
        self.user = User()

    def test_instance_creation(self):
        """Test instance creation and attributes."""
        self.assertIsInstance(self.user, User)
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")


if __name__ == '__main__':
    unittest.main()
