import unittest
from ISSA.MemberMailer.Objects.database import Database

class TestUpdate(unittest.TestCase):
	def test_update_member(self):
		test_member = Database()
		test = test_member.update(9, "People", firstname = "Danny", email = "dnguyen@gmail.com")
		self.assertEqual(test, "Success!")


if __name__ == '__main__':
	unittest.main()
