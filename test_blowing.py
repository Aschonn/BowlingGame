import unittest
from Game import BowlingGame

class TestBowling(unittest.TestCase):
    def test_checkvalidity(self):
        newgame = BowlingGame()
        result = newgame.checkValidity('/', 0, 1, None, 1)
        self.assertEqual(result, False)
        result = newgame.checkValidity("X", 1, 1, 3, 2)
        self.assertEqual(result, False)


    def test_strike(self):
        newgame = BowlingGame()
        result = newgame.strike(4)
        self.assertEqual(result, 10)

    def test_spare(self):
        newgame = BowlingGame()
        result = newgame.strike(4)
        self.assertEqual(result, 10)

    def test_calcScore(self):
        pass

    def test_getScore(self):
        pass
    def test_setScore(self, num):
        pass

    def test_getRollList(self):
        pass


    ##############################

        

    def test_resetScoreList(self):

        pass

    def test_dropItemNextToStrike(self, index):
        
        pass




    def test_filter(self, value):

        pass
        
