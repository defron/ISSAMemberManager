import unittest
from ISSA.MemberMailer.Objects import Indexer

__author__ = 'Defron'


class TestIndexer(unittest.TestCase):

    def test_search_by_name(self):
        foo = Indexer()
        self.assertIsNone(foo.search_by_name("foo"))



if __name__ == '__main__':
    unittest.main()