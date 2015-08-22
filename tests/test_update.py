import unittest
from ISSA.MemberMailer.Objects.database import Database

class TestUpdate(unittest.TestCase):
	def test_update_member(self):
		test_member = Database()
		test = test_member.update(1, "People", firstname = "Thomas2", lastname = "Brown2", email = "tbrown2@gmail",phone = "5034567890")
		self.assertEqual(test, "Success!")

if __name__ == '__main__':
    unittest.main()
