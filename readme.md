
Requirements:
Create a program in your choice of language that can calculate the score of a full round of bowling, based on user inputs and the following rules:

If you roll a strike in the first shot of the 10th frame, you get 2 more shots.
If you roll a spare in the first two shots of the 10th frame, you get 1 more shot.
If you leave the 10th frame open after two shots, the game is over and you do not get an additional shot.

How to run:
1) type `python bowling.py`
2) Enter in scores
3) If successful it should output all frames as inputed as well as score.

Improvements:

Instead of writing the code frame by frame it would have been easier to go roll by roll. The data checking process would have been easier. Sadly, in the middle of finals I wasn't able to implement that solution. Also adding more try-excepts would make this more efficient and would work better than using if-elif-else, but I went for readability.


Side Note:

I am sorry for being late. I honestly thought the due date was on the 4th and thought I could submit it today (5/4). Plus finals and group projects don't make things easier, but that is no excuse. I will communicate more effectively from now on. 

Bugs:

if user enters in '3/' it will only provide the error "an error has occured in function "checkValidity"

if user outputs a spare, strike, strike the spare will add the current value of strike than update value