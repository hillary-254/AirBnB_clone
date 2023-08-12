"""Unittests for state"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test suite for the State class."""

    def setUp(self):
        """Set up for the tests."""
        self.state = State()

    def test_instance_creation(self):
        """Test instance creation and attributes."""
        self.assertIsInstance(self.state, State)
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")


if __name__ == '__main__':
    unittest.main()
