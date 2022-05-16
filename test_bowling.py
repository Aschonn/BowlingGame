import unittest
from Bowling import BowlingGame

class TestBowling(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:

        # prints when tests start

        print("Startup tests")
        print("----------------------------------------")


    @classmethod
    def tearDownClass(cls) -> None:

        # prints as soon as testing class ends

        print("----------------------------------------")
        print("Tear down class")


    def setUp(self) -> None:

        # Limits the amount of duplication in code (DRY principle). 

        self.newgame = BowlingGame()

        return super().setUp()

    def tearDown(self) -> None:

        # removes code when done with test (DRY principle). 
        print("Teardown")
        return super().tearDown()


    def test_checkvalidity(self):

        # test function is it cna accurately verify inputs in different situations

        result = self.newgame.checkValidity('/', 0, 1, None, 1)
        self.assertEqual(result, False)
        result = self.newgame.checkValidity("X", 1, 1, 3, 2)
        self.assertEqual(result, False)


    def test_strike(self):

        # test strike function

        # newgame = BowlingGame()
        result = self.newgame.strike([4, 5])
        self.assertEqual(result, 19)

    def test_spare(self):

        # tests if spare returns correct 

        result = self.newgame.spare(7)
        self.assertEqual(result, 17)

    def test_calcScore(self):
        
        # tests different rollists to see if calculates an accurate score or not

        tests = {

            "strikes" : (300, ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]),
            "spares"  : (245, [4, "/", "x", "x", "x", "x", "x", "x", "x", 7, 2, "x", 3, "/"]),
            "Numbers" : (40, [2] * 20),
        }

        for key, values in tests.items():
            self.newgame.setRollList(values[1])
            self.newgame.calcScore()
            gamescore = self.newgame.getScore()
            self.assertEqual(gamescore, values[0], f"{key} test equals {values[0]} not {gamescore}")


    def test_getScore(self):

        # tests if it returns score
        self.assertEqual(None, self.newgame.getScore(), "Error: score should not be available right after object creation.")


    def test_setScore(self):

        # test is function sets score

        self.newgame.setScore("40")
        self.assertNotEqual(self.newgame.getScore(), 40, f"The function only accepts integers not characters.")
        self.newgame.setScore(40)
        self.assertEqual(self.newgame.getScore(), 40, f"Should allow 40 to be set as score.")
        self.newgame.setScore(400)
        self.assertNotEqual(self.newgame.getScore(),400, f"The function only accepts integers between 300 and 0.")


    def test_getRollList(self):

        # makes sure rolllist function returns a function

        self.assertEqual([0]*21, self.newgame.getRollList(), "Error: list should be as default a list of 21 0's.")


    def test_resetScoreList(self):

        # tests to see if resetscore function works

        self.newgame.setRollList(["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"])
        self.newgame.resetRollList()
        self.assertEqual([0]*21, self.newgame.getRollList(), "List was not reset. Check function.")


    def test_dropItemNextToStrike(self):

        #make sure that this function drops next value if current value is strike
        
        self.newgame.setRollList([3, 4, "x", 1, 2, "x", "x", "x", "x", "x", "x", "x", "x", "x"])
        self.newgame.dropItemNextToStrike(2)
        self.assertEqual(self.newgame.getRollList()[3], 2, "Element was not removed.")



    def test_filter(self):

        # check and make sure it only accepts 0-9, X (upper and lower), and /

        self.assertEqual(False, self.newgame.filter(f'f'))
        self.assertEqual(True, self.newgame.filter(f'0'))
        self.assertEqual(True, self.newgame.filter(f'9'))
        self.assertEqual(True, self.newgame.filter(f'x'))
        self.assertEqual(True, self.newgame.filter(f'X'))
        self.assertEqual(True, self.newgame.filter(f'/'))


if __name__ == '__main__':
    unittest.main()