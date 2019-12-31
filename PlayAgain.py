from logicForRps import loggic
def playAgain():
    signal2= input("DO YOU STILL WISH TO PLAY THE ROCK PAPER SCISSORS GAME?...Type (Y) for Yes, (N) for No").upper()
    if  signal2=="Y":
        loggic()
    elif  signal2=="N":
        print("You've Exited the game")
