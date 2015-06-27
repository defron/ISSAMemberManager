import unittest
from ISSA.MemberMailer.Objects.officer import Officer


class TestOfficer(unittest.TestCase):

    def test_print_officer(self):
        test_officer = Officer()
        test_officer.first_name = "Calvin"
        test_officer.last_name = "Tran"
        self.assertEqual(str(test_officer), "Calvin Tran")

if __name__ == '__main__':
    unittest.main()
