import unittest
from square import getSquare, won, spotClaimedCheck

class TesterClass(unittest.TestCase):

    def test_11X(self):
        a = "x"
        self.assertEqual(a,getSquare(1,1))

    def test_11O(self):
        a = "o"
        self.assertEqual(a,getSquare(1,1))

    def test_won(self):
        self.assertTrue(won("x"))

    def test_unclaimed22(self):
        self.assertFalse(spotClaimedCheck(2,2))

#if __name__=='__main__':
    #unittest.main()