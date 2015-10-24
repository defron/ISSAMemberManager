import unittest
from ISSA.MemberMailer.Objects.database import Database

class TestInsert(unittest.TestCase):

    def test_insert_member(self):
        test_member = Database()
        test = test_member.insert("boardtitle", "Vice Presiden")
        self.assertEqual(test, "Success!")

if __name__ == '__main__':
    unittest.main()