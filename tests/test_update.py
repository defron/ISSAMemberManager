import unittest
from Test import Database

class TestUpdate(unittest.TestCase):
	def test_update_member(self):
		test_member = Database()
		test = test_member.update(1, "people", firstname= "Thomas", lastname= "Brown", email="tbrown@gmail", phone="5034567890")
		self.assertEqual(test, "Success!")

if __name__ == '__main__':
    unittest.main()
