import re

class BowlingGame:

    #############################

    def __init__(self):
        self.rollList = [0] * 21 # nested list for scores
        self.score = None #display nothing as default

    #############################

    # getters amd setters

    '''
    Function: getScore, setScore, and getScoreList return values as suggested by its name
    Args:
        getScore = no args
        setScore = needs int 
        getScoreList = no args
    Returns:
        returns either a list or int
    '''


    def getScore(self):
        return self.score

    def setScore(self, num):

        if type(num) == int:
            if num >= 0 and num <= 300:
                self.score = int(num)
            else:
                print("invalid number. Must be between 0 and 300.")
        else:
            print("This functions only accepts integers.")        
            
    def getRollList(self):
        return self.rollList

    def setRollList(self, newscorelist):

        if len(newscorelist) >= 12 or len(newscorelist) <= 21:
            self.rollList = newscorelist
        else:
            print("Unable to setlist due to not correct number of values.")

    ##############################

        

    def resetRollList(self):

        '''
           
            Function: Reset score list, so user can redo score board if needed.
            Args:
                No args
            Returns:
                object list value gets reset to zeros

        '''
        self.rollList = [0] * 21


    def dropItemNextToStrike(self, index):

        '''           
            Function: Removes zero (roll) from list everytime a strike appears in the first 9 frames
            Args:
                takes index so it can remove the next zero
            Returns:
                object list value gets reset to zeros

        '''
        try:
            self.rollList.pop(index + 1)
        except:
            print("Could not remove item since list ended")


    def checkValidity(self, value, index, frame, prev, count):

        '''
            Function: Checks the validity of rolllist 
            Args:
                if X:
                    1) Removes 1 from list unless its in the last frame
                    2) cannot be added in at an odd index (done)
            

                if /: 
                    1) Cannot be ahead of strike
                    2) Must be odd index

                if 0-9:
                    1) Cannot be equal to more than 9
            
            Returns:
                returns true or false value whether roll is valid or not.
        
        '''

        if frame != 10:
            if value.upper() == "X" and count == 1:
                self.dropItemNextToStrike(index)
                return True
            
            elif value == '/':

                if index != 0 and self.rollList[index - 1].upper() != "X" and prev != "/":
                    return True
                else:
                    print("cannot have spare symbol after strike or put it as first value")
                    return False

            elif value.upper() == "X" and count == 2:
                print("cannot put strike (X) as second roll. use the spare symbol (/)")
                return False

            else:
                
                if prev and count == 2:
                    if int(prev) + int(value) > 9:
                        print("previous and current roll cannot exceed 10. Please enter spare instead.")
                        return False
                    else:
                        return True
                else:
                    return True

        else:

            if value == "/" and index == len(self.rollList) - 3:    
                print("Invalid placement of spare symbol")
                return False
            elif value == "/" and prev.upper() == "X":
                print("The previous element of a spare cannot be a strike")
                return False
            else:
                return True


    def filter(self, value):

        '''
            Function: filter outs all user input that longer than one character/number and checks for characters that are:
            1) 0-9 -> number of pins
            2) X or x -> strike symbol
            3) / -> spare symbol
            Args:
                Takes in a string value
            Returns:
                return value (true) or nothing (False)
        '''

        pattern = re.compile('^[0-9 xX\/]$')
        if re.match(pattern, value):
            return True
        else:
            print("invalid format for roll")
            return False
        
    def spare(self, nextroll):


        '''
            Function: outputs score from spare and adds next roll.
            Args:
                takes in index in order to keep track of which frame we are in
            Returns:
                returns sum from strike
        '''

        total = 10 
        if not type(nextroll) == int and nextroll.upper() == "X":
            total += 10
        else:
            total += int(nextroll)
        
        return total

    def strike(self, nextrolls):

        '''
            Function: outputs score from strike and adds next two rolls
            Args:
                takes in index in order to keep track of which frame we are in
            Returns:
                returns sum from strike

        '''

        total = 10
        prev = None
        for i in nextrolls:
            if type(i) == int:               
                total += int(i)
            elif i.upper() == "X":
                total += 10
            else:
                total += 10 - int(prev)


            prev = i

        #testing
        # print(f"rolls after: {self.rollList[index + 1 : index + 3]}\nTotal: {total}")
 

        return total


    def calcScore(self):

        '''
            Function: Calculates score from rolllist after user has inputed list or set list
            Args:
                accepts object parameter of rolllist (all values are string)
            Returns:
                calculated score of all ten frames and changed self.score to generated score
        '''
        frame = 1
        count = 0
        sum = 0
        prev = 0
        sumList = []
        for index, roll in enumerate(self.rollList):
            
            if frame != 10 and index < len(self.rollList) - 3:

                if str(roll).isdigit():
                    sum += int(roll)
                    if count == 2:
                        count = 1
                    else:
                        count = 2
                elif roll.upper() == "X":
                    sum += self.strike(self.rollList[index + 1: index + 3])
                    frame += 1

                else:
                    sum += self.spare(self.rollList[index + 1]) - int(prev)
                    frame += 1


            else:
                
                if type(roll) == int:
                    sum += int(roll)
                elif roll.upper() == "X":
                    sum += 10
                else:
                    sum += 10 - int(prev)
                


            sumList.append(sum)
            prev = roll

        # TESTING
        # print(sumList)


        self.setScore(sum)

                    


    def addScores(self):

        '''
        Function: Sets user inputed data in the rollList attribute
        Args:
            accepts self parameter roll
        Returns:
            sets rollList with user input
        '''

        print("'X' -> Strike")
        print("'/' -> Spare")
        print("Accepts 0-9 numbers, X (case doesnt matter), and /\n")
        print("only one character/number is allowed")

        frame = 1
        count = 1
        rollNum = 0
        prev = None

        while frame != 10:

            roll = input(f"Frame ({frame}) Roll: ({count}) RollTotal: ({rollNum + 1}) roll score = ")
            while not (self.filter(roll) and self.checkValidity(roll, rollNum, frame, prev, count)):
                roll = input(f"Frame ({frame}) Roll: ({count}) RollTotal: ({rollNum + 1}) roll score = ")
            

            #testing purposes
            # print("rollnum", rollNum)
            # print("frame:", frame)
            # print("listlength", listLength)
            # print("previous:", prev)

            # calculates and keeps track of frames

            if roll.upper() == "X" or count == 2:
                frame += 1  
                count = 1
            else:
                count += 1



            self.rollList[rollNum] = roll            #sets rollscore to list
            rollNum += 1                             #goes to next roll
            prev = roll                              #keeps track of previous roll


        # holds values for last frame

        frame10 = []

        # gets first two value (mandatory)

        for i in range(2):
            roll = input(f"Frame ({frame}) Roll: ({count}) RollTotal: ({rollNum + 1}) roll score = ")
            while not (self.filter(roll) and self.checkValidity(roll, rollNum, frame, prev, count)):
                roll = input(f"Frame ({frame}) Roll: ({count}) RollTotal: ({rollNum + 1}) roll score = ")
            frame10.append(roll)
            self.rollList[rollNum] = roll
            rollNum += 1
            prev = roll

        # grabs last value in frame if it meet criteria
                
        if "/" in frame10 or "X" in frame10 or 'x' in frame10:
            roll = input(f"Frame ({frame}) Roll: ({count}) RollTotal: ({rollNum + 1}) roll score = ")
            while not (self.filter(roll) and self.checkValidity(roll, rollNum, frame, prev, count)):
                roll = input(f"Frame ({frame}) Roll: ({count}) RollTotal: ({rollNum + 1}) roll score = ")
            self.rollList[rollNum] = roll
            prev = roll


    # print object

    def __str__ (self):
        return 'RollList: ' + str(self.getRollList()) + '\n' + 'Score:' + str(self.getScore())




                
    
