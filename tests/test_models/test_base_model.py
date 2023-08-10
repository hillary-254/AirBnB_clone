import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """
    Test the BaseModel class
    """

    def setUp(self):
        """
        Set up for the tests
        """
        self.base = BaseModel()

    def tearDown(self):
        """
        Cleaning up after each test
        """
        pass

    def test_attributes(self):
        """
        Test attributes of BaseModel
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """
        Test initialization
        """
        self.assertIsInstance(self.base, BaseModel)

    def test_str(self):
        """
        Test the __str__ method
        """
        self.assertEqual(str(self.base), "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__))

    @patch('models.base_model.storage')
    def test_save(self, mock_storage):
        """
        Test the save method
        """
        old_updated_at = self.base.updated_at
        self.base.save()
        mock_storage.save.assert_called_once_with()
        self.assertNotEqual(old_updated_at, self.base.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method
        """
        base_dict = self.base.to_dict()
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertEqual(type(base_dict['created_at']), str)
        self.assertEqual(type(base_dict['updated_at']), str)

    @patch('models.base_model.storage')
    def test_init_with_kwargs(self, mock_storage):
        """
        Test initialization with keyword arguments
        """
        base = BaseModel(id='123', created_at='2023-08-10T00:00:00.000000', updated_at='2023-08-10T00:00:00.000000')
        self.assertEqual(base.id, '123')
        self.assertEqual(base.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'), '2023-08-10T00:00:00.000000')
        self.assertEqual(base.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f'), '2023-08-10T00:00:00.000000')
        mock_storage.new.assert_called_once_with()

    def test_init_no_args(self):
        """
        Test initialization with no arguments
        """
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.created_at, datetime)
        self.assertEqual(base.created_at, base.updated_at)


if __name__ == '__main__':
    unittest.main()
