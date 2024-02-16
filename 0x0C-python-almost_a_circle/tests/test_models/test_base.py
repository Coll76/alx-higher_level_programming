import unittest
from models.base import Base
"""
acts as the base class for test cases in the unittestframeork
"""


class TestBase(unittest.TestCase):
    """
    base class for test cases
    """
    def test_constructor_with_id(self):
        """
        Test when id is set to a certain number
        """
        obj = Base(id=4)
        self.assertEqual(obj.id, 4)
    """
    constructor when id is None
    """
    def test_with_no_id(self):
        """
        Test when id is None
        """
        obj_4= Base()
        obj_5 = Base()
        self.assertEqual(obj_4.id, 1)
        self.assertEqual(obj_5.id, 2)

if __name__ == '__main__':
    unittest.main()
