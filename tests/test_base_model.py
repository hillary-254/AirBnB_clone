"""This module contains unittests for the base_model"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test suite for the BaseModel class.
    """

    def setUp(self):
        """
        Set up for the tests.
        """
        self.base = BaseModel()

    def tearDown(self):
        """
        Cleaning up after each test.
        """
        pass

    def test_init(self):
        """
        Test initialization.
        """
        self.assertIsInstance(self.base, BaseModel)

    def test_str(self):
        """
        Test the __str__ method.
        """
        expected_str = "[BaseModel] ({}) {}".format(
            self.base.id, self.base.__dict__)
        self.assertEqual(str(self.base), expected_str)

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(old_updated_at, self.base.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        base_dict = self.base.to_dict()
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertEqual(type(base_dict['created_at']), str)
        self.assertEqual(type(base_dict['updated_at']), str)


if __name__ == '__main__':
    unittest.main()
