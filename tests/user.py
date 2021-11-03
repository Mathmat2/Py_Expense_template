import unittest
from user import add_user

class TestUser(unittest.TestCase):

    def test_add_user(self):
        self.assertEqual(add_user('Mathieu'), True)
        self.assertEqual(add_user(), False)
        self.assertEqual(add_user('Dorian', 'Mathieu', 'Michel'), False)