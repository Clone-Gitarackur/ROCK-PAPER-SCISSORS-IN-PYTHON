from logicForRps import loggic, scores
import random
from PlayAgain import playAgain

signal= input("WELCOME TO THE ROCK PAPER SCISSORS GAME...Type (P) for Play, (E) for Exit (H) for Help").upper()


def gameplay():
    if signal=="P":
        loggic()
    elif signal=="H":
        print('''
        This is how the game goes...- the player selects between rock, paper and scissors 
        which will be selected using numbers 0( for Rock). 1( for Paper), 2(for Scissors) respectively..
        and then play against a computer that chooses the same randomly..
        
        the rules and the way to win or lose are: 
        Rock beats Scissors
        Scissors beat Paper
        Paper beats Rock
        
        rest combinations are Draws
        ''')
        playAgain()

    elif signal=="E":
        print("you've exited the game")
        print(f"Player: {scores[0]} , computer: {scores[1]}")
        playAgain()



gameplay()