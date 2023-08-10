import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Unit tests for BaseModel class.
    """
    def test_init(self):
        """
        Test initialization of BaseModel instance.
        """
        # Test code for BaseModel initialization
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_str(self):
        """
        Test string representation of BaseModel instance.
        """
        # Test code for BaseModel __str__ method
        base_model = BaseModel()
        string_representation = str(base_model)
        expected_representation = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(string_representation, expected_representation)

    def test_save(self):
        """
        Test save method of BaseModel instance.
        """
        # Test code for BaseModel save method
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(base_model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """
        Test to_dict method of BaseModel instance.
        """
        # Test code for BaseModel to_dict method
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

if __name__ == '__main__':
    unittest.main()
