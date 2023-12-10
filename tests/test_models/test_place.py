#!/usr/bin/python3
"""Test Place"""
import pep8
import models
import inspect
import unittest
from models import place
from datetime import datetime
from models.base_model import BaseModel
Place = place.Place


class TestPlaceDocs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up"""
        cls.place_f = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_conformance_place(self):
        """Test PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_place(self):
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_place_module_docstring(self):
        self.assertIsNot(place.__doc__, None,
                         "place.py needs a docstring")
        self.assertTrue(len(place.__doc__) >= 1,
                        "place.py needs a docstring")

    def test_place_class_docstring(self):
        self.assertIsNot(Place.__doc__, None,
                         "Place class needs a docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class needs a docstring")

    def test_place_func_docstrings(self):
        """Test docstrings"""
        for func in self.place_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestPlace(unittest.TestCase):
    """Test Place"""
    def test_is_subclass(self):
        place = Place()

        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_city_id_attr(self):
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        if models.storage_t == 'db':
            self.assertEqual(place.city_id, None)
        else:
            self.assertEqual(place.city_id, "")

    def test_user_id_attr(self):
        """Test user_id"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        if models.storage_t == 'db':
            self.assertEqual(place.user_id, None)
        else:
            self.assertEqual(place.user_id, "")

    def test_name_attr(self):
        """Test attr name"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        if models.storage_t == 'db':
            self.assertEqual(place.name, None)
        else:
            self.assertEqual(place.name, "")

    def test_description_attr(self):
        """Test description"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        if models.storage_t == 'db':
            self.assertEqual(place.description, None)
        else:
            self.assertEqual(place.description, "")

    def test_number_rooms_attr(self):
        """Test number_rooms"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        if models.storage_t == 'db':
            self.assertEqual(place.number_rooms, None)
        else:
            self.assertEqual(type(place.number_rooms), int)
            self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """Test number_bathrooms"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        if models.storage_t == 'db':
            self.assertEqual(place.number_bathrooms, None)
        else:
            self.assertEqual(type(place.number_bathrooms), int)
            self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """Test max_guest"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        if models.storage_t == 'db':
            self.assertEqual(place.max_guest, None)
        else:
            self.assertEqual(type(place.max_guest), int)
            self.assertEqual(place.max_guest, 0)

    def test_price_by_night_attr(self):
        """Test price_by_night"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        if models.storage_t == 'db':
            self.assertEqual(place.price_by_night, None)
        else:
            self.assertEqual(type(place.price_by_night), int)
            self.assertEqual(place.price_by_night, 0)

    def test_latitude_attr(self):
        """Test latitude"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        if models.storage_t == 'db':
            self.assertEqual(place.latitude, None)
        else:
            self.assertEqual(type(place.latitude), float)
            self.assertEqual(place.latitude, 0.0)

    def test_longitude_attr(self):
        """Test longitude"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        if models.storage_t == 'db':
            self.assertEqual(place.longitude, None)
        else:
            self.assertEqual(type(place.longitude), float)
            self.assertEqual(place.longitude, 0.0)

    @unittest.skipIf(models.storage_t == 'db', "not testing File Storage")
    def test_amenity_ids_attr(self):
        """Test amenity_ids"""
        place = Place()

        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(len(place.amenity_ids), 0)

    def test_to_dict_creates_dict(self):
        """test to_dict"""
        p = Place()
        new_d = p.to_dict()

        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in p.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Place()
        new_d = p.to_dict()

        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(t_format))

    def test_str(self):
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))
