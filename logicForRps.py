import random

scores=[0,0]
objectz=["rock", "Paper", "Scissors"]
countt= 0


def loggic():
    while scores[0]<5 and scores[1]<5:
        player = int(input("which object do you wish to choose? 0 for rock, 1 for paper, 2 for scissors"))
        computer= random.choice(objectz)
        print("PLAYER:" + "" + objectz[player])
        print("COMPUTER:" + "" + computer)
        if objectz[player]==objectz[0] and computer==objectz[1]:
            print("computer wins")
            scores[1]+=1
            print(f"Player: {scores[0]} , computer: {scores[1]}")
        elif objectz[player]==objectz[0] and computer==objectz[1]:
            print("computer wins")
            scores[1]+=1
            print(f"Player: {scores[0]} , computer: {scores[1]}")
        elif objectz[player]==objectz[0] and computer==objectz[2]:
            print("player wins")
            scores[0]+=1
            print(f"Player: {scores[0]} , computer: {scores[1]}")
        elif objectz[player]==objectz[1] and computer==objectz[0]:
            print("player wins")
            scores[0]+=1
            print(f"Player: {scores[0]} , computer: {scores[1]}")
        elif objectz[player]==objectz[1] and computer==objectz[2]:
            print("computer wins")
            scores[1]+=1
            print(f"Player: {scores[0]} , computer: {scores[1]}")
        elif objectz[player]==objectz[2] and computer==objectz[0]:
            print("computer wins")
            scores[1]+=1
            print(f"Player: {scores[0]} , computer: {scores[1]}")
        elif objectz[player]==objectz[2] and computer==objectz[1]:
            print("player wins")
            scores[0]+=1
            print(f"Player: {scores[0]} , computer: {scores[1]}")
        else:
            if objectz[player]==objectz[0] and computer==objectz[0]:
                print("rock vs rock.... both draw")
                print(f"Player: {scores[0]} , computer: {scores[1]}")
            elif objectz[player]==objectz[1] and computer==objectz[1]:
                print("paper vs paper... both draw")
                print(f"Player: {scores[0]} , computer: {scores[1]}")
            elif objectz[player]==objectz[2] and computer==objectz[2]:
                print("scissors vs scissors... both draw")
                print(f"Player: {scores[0]} , computer: {scores[1]}")

    else:
        if scores[0]>scores[1]:
            print("PLAYER is the Winner")
        elif scores[0]<scores[1]:
            print("COMPUTER is the Winner")
