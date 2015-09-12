import unittest
from ISSA.MemberMailer.Objects.database import Database

class TestDelete(unittest.TestCase):
	def test_delete_mem(self):
		test_member = Database()
		test = test_member.delete(3)
		self.assertEqual(test, "Success!")

if __name__ == '__main__':
    unittest.main()
