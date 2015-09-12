import unittest
from ISSA.MemberMailer.Objects.database import Database

class TestInsert(unittest.TestCase):

    def test_insert_member(self):
        test_member = Database()
        test = test_member.insert("Johny", "Nguyen","jnguyen@gmail.com", "1029384123", 2017)
        self.assertEqual(test, "Success!")

if __name__ == '__main__':
    unittest.main()