import unittest
from ISSA.MemberMailer.Objects.database import Database

class TestDelete(unittest.TestCase):
	def test_delete_mem(self):
		test_member = Database()
		test = test_member.delete("people",10)
		self.assertEqual(test, "Success!")

if __name__ == '__main__':
	unittest.main()
