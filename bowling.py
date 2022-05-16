from Game import BowlingGame




def main():

    game1 = BowlingGame()
    
    # method adds score to object one
    # print(game1)

    print(game1.getRollList())
    

    # calculates score
    game1.addScores()
    game1.calcScore()
    

    # outputs changes
    print(game1)



main()
