import unittest
from Game import BowlingGame

class TestBowling(unittest.TestCase):
    
    def test_checkvalidity(self):

        # test function is it cna accurately verify inputs in different situations

        newgame = BowlingGame()
        result = newgame.checkValidity('/', 0, 1, None, 1)
        self.assertEqual(result, False)
        result = newgame.checkValidity("X", 1, 1, 3, 2)
        self.assertEqual(result, False)


    def test_strike(self):

        # test strike function

        newgame = BowlingGame()
        result = newgame.strike([4, 5])
        self.assertEqual(result, 19)

    def test_spare(self):

        # tests if spare returns correct 

        newgame = BowlingGame()
        result = newgame.spare(7)
        self.assertEqual(result, 17)

    def test_calcScore(self):
        
        # tests different rollists to see if calculates an accurate score or not

        tests = {

            "strikes" : (300, ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]),
            "spares"  : (245, [4, "/", "x", "x", "x", "x", "x", "x", "x", 7, 2, "x", 3, "/"]),
            "Numbers" : (40, [2] * 20),
        }

        newgame = BowlingGame()

        for key, values in tests.items():
            newgame.setRollList(values[1])
            newgame.calcScore()
            gamescore = newgame.getScore()
            self.assertEqual(gamescore, values[0], f"{key} test equals {values[0]} not {gamescore}")


    def test_getScore(self):

        # tests if it returns score

        newgame = BowlingGame()
        self.assertEqual(None, newgame.getScore(), "Error: score should not be available right after object creation.")


    def test_setScore(self):

        # test is function sets score

        newgame = BowlingGame()
        newgame.setScore("40")
        self.assertNotEqual(newgame.getScore(), 40, f"The function only accepts integers not characters.")
        newgame.setScore(40)
        self.assertEqual(newgame.getScore(), 40, f"Should allow 40 to be set as score.")
        newgame.setScore(400)
        self.assertNotEqual(newgame.getScore(),400, f"The function only accepts integers between 300 and 0.")


    def test_getRollList(self):

        # makes sure rolllist function returns a function

        newgame = BowlingGame()
        self.assertEqual([0]*21, newgame.getRollList(), "Error: list should be as default a list of 21 0's.")


    def test_resetScoreList(self):

        # tests to see if resetscore function works

        newgame = BowlingGame()
        newgame.setRollList(["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"])
        newgame.resetRollList()
        self.assertEqual([0]*21, newgame.getRollList(), "List was not reset. Check function.")


    def test_dropItemNextToStrike(self):

        #make sure that this function drops next value if current value is strike
        
        newgame = BowlingGame()
        newgame.setRollList([3, 4, "x", 1, 2, "x", "x", "x", "x", "x", "x", "x", "x", "x"])
        newgame.dropItemNextToStrike(2)
        self.assertEqual(newgame.getRollList()[3], 2, "Element was not removed.")



    def test_filter(self):

        # check and make sure it only accepts 0-9, X (upper and lower), and /

        newgame = BowlingGame()
        self.assertEqual(False, newgame.filter(f'f'))
        self.assertEqual(True, newgame.filter(f'0'))
        self.assertEqual(True, newgame.filter(f'9'))
        self.assertEqual(True, newgame.filter(f'x'))
        self.assertEqual(True, newgame.filter(f'X'))
        self.assertEqual(True, newgame.filter(f'/'))


