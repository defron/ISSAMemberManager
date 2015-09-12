import unittest
from ISSA.MemberMailer.Objects.database import Database

class TestPrint(unittest.TestCase):

	def test_print_table(self):
		test_member = Database()
		print = test_member.print()
		self.assertEqual(print, "Success!")

if __name__ == '__main__':
    unittest.main()