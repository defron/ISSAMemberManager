import unittest
from ISSA.MemberMailer.Objects.member import Member

__author__ = 'Defron'


class TestMember(unittest.TestCase):

    def test_print_member(self):
        test_member = Member()
        test_member.first_name = "Jeff"
        test_member.last_name = "Schultz"
        self.assertEqual(str(test_member), "Jeff Schultz")

if __name__ == '__main__':
    unittest.main()