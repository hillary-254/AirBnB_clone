import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test suite for the FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.obj_base = BaseModel()
        self.obj_user = User()
        self.obj_amenity = Amenity()
        self.obj_city = City()
        self.obj_place = Place()
        self.obj_review = Review()
        self.obj_state = State()
        self.storage.new(self.obj_base)
        self.storage.new(self.obj_user)
        self.storage.new(self.obj_amenity)
        self.storage.new(self.obj_city)
        self.storage.new(self.obj_place)
        self.storage.new(self.obj_review)
        self.storage.new(self.obj_state)

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """Test the all() method."""
        objects = self.storage.all()
        self.assertEqual(type(objects), dict)
        self.assertIn(
            self.obj_base.__class__.__name__ + '.' + self.obj_base.id, objects)

    def test_new(self):
        """Test the new() method."""
        new_obj = BaseModel()
        self.storage.new(new_obj)
        obj_key = new_obj.__class__.__name__ + '.' + new_obj.id
        self.assertIn(obj_key, self.storage._FileStorage__objects)

    def test_save_reload(self):
        """Test the save() and reload() methods."""
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        objects_before = self.storage.all()
        objects_after = new_storage.all()
        self.assertEqual(objects_before, objects_after)

    def test_serialization_deserialization(self):
        """Test object serialization and deserialization."""
        base_dict = self.storage._serialize(self.obj_base)
        deserialized_base = self.storage._deserialize(base_dict)
        self.assertEqual(type(deserialized_base), BaseModel)

        user_dict = self.storage._serialize(self.obj_user)
        deserialized_user = self.storage._deserialize(user_dict)
        self.assertEqual(type(deserialized_user), User)


if __name__ == '__main__':
    unittest.main()
