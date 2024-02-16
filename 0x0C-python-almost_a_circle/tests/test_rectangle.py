import unittest
from models.rectangle import Rectangle
"""
base class for the test classes
"""


class TestRectangle(unittest.TestCase):
    """
    Test for inheritance of Rectangle from Base
    """
    def test_inherit(self):
        """
        Test initialization in the Rectangle
        """
        obj_4 = Rectangle(5, 6, 7, 8, 9)
        self.assertEqual(obj_4.width, 5)
        self.assertEqual(obj_4.height, 6)
        self.assertEqual(obj_4.x, 7)
        self.assertEqual(obj_4.y, 8)
        self.assertEqual(obj_4.id, 9)
        """
        Test for validation of attributes
        """
    def test_validation(self):
        """
        Test that validates that height or width are int type
        """
        with self.assertRaises(TypeError) as error:
            Rectangle(4, '4')
        self.assertEqual(str(error.exception), "height must be an integer")

    def test_validation4(self):
        """
        Test that validates that height or width are > 0
        """
        with self.assertRaises(ValueError) as context:
            Rectangle(-5, 8)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_validation5(self):
        """
        Test that validates that x or y are > 0
        """
        with self.assertRaises(ValueError) as context:
            Rectangle(5, 6, -7, 8, 9)
        self.assertEqual(str(context.exception), "x must be >= 0")
        """
        Test for validation of area method
        """
    def test_area(self):
        """
        Tests functionality of area method
        """
        obj = Rectangle(6, 7)
        self.assertEqual(obj.area(), 42)
        """
        Test functionality of display method
        """
    def test_display(self):
        """
        Tests if it print to stdout the Rectangle instance with the
        character #
        """
        obj = Rectangle(1, 1)
        self.assertEqual(obj.display(), "#")
        """
        Test for __str__ method
        """
    def test_str(self):
        """
        Test if __str__ gives a string representation of an object
        """
        obj = Rectangle(5, 5, 1)
        self.assertEqual(str(obj), "[Rectangle] (5) 1/0 - 5/5")
        """
        Test for assignment of arguments
        """
    def test_update(self):
        """
        Tests if the assignement is correct
        """
        obj = Rectangle(4, 5, 6, 7, 8)
        obj.update(9, 8, 7, 5, 4)
        self.assertEqual(obj.id, 9)
        self.assertEqual(obj.width, 8)
        self.assertEqual(obj.height, 7)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 4)
        """
        Test using the update ith key-ord arguments
        """
    def test_key_orded(self):
        """
        Test using the update ith key-ord arguments
        """
        obj = Rectangle(4, 5, 6, 7, 8)
        obj.update(id=9, width=8, height=7, x=6, y=5)
        self.assertEqual(obj.width, 8)
        self.assertEqual(obj.id, 9)
        self.assertEqual(obj.height, 7)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 5)
        """
        Test the update method with a mix of no-keyword
        and key-worded arguments
        """
    def test_key_and_non_key(self):
        """
        update method with a mix of no-keyword
        and key-worded arguments
        """
        obj = Rectangle(1, 1, 1, 1, 1)
        # Update with a mix of no-keyword and key-worded arguments
        obj.update(2, width=3, height=4, x=5, y=7)
        # Check if attributes are updated correctly
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.width, 3)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 7)

