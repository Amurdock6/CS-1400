import random
import time

gameRunning = True
myTurn = True
myPts = 0
devilPts = 0
myRndPts = 0
devilRndPts = 0
die = 0

print("\t Welcome to Devil's Dice")


# r = input("Press 'r' To Roll or Press 'p' To Pass: ")
# while (r != 'r' and r != 'p'):
#     print("Invalid Input")
#     r = input("action: ")

def uDie(die):
    # die - Integer valued 1-6.  The rolled die value.

    if die == 1: return "\u2620"
    if die == 2: return "\u2681"
    if die == 3: return "\u2682"
    if die == 4: return "\u2683"
    if die == 5: return "\u2684"
    if die == 6: return "\u2685"


def printSimpleBoard(die, myPts, devilPts, myTurn, myRndPts, devilRndPts):
    # die - Integer valued 1-6.  The rolled die value.
    # myPts - Integer valued 0-100. The current saved score of the human player.
    # devilPts - Integer valued 0-100. The current saved score of the devil.
    # myTurn - Boolean value.  True if it is the human player's turn.
    # myRndPts - Integer valued 0-100.  The human's saved score plus points gained that round.
    # devilRndPts - Integer valued 0-100.  The devil's saved score plus points gained that round.

    print("my\t\tthis\tdevil's\t this")
    print("score\tround\tscore\tround")
    print("  ", myPts, "\t  ", myRndPts, "\t  ", devilPts, "\t  ", devilRndPts)
    print("")
    print("\t     die")
    print("\t     ", uDie(die))
    print("\n\n")


while gameRunning:
    # Player Logic 
    while myTurn:
        r = input("Press 'r' To Roll or Press 'p' To Pass or Press 'q' To Quit Cowered: ")
        while r != 'r' and r != 'p' and r != 'q':
            print("Invalid Input")
            r = input("Press 'r' To Roll or Press 'p' To Pass or Press 'q' To Quit Cowered: ")

        if myPts + myRndPts >= 100:
            print("Game Over You Won!")
            printSimpleBoard(die, myPts, devilPts, myTurn, myRndPts, devilRndPts)
            gameRunning = False
            break

        if r == 'r':
            die = random.randint(1, 6)
            myRndPts = myRndPts + die
            printSimpleBoard(die, myPts, devilPts, myTurn, myRndPts, devilRndPts)
            if die == 1:
                print("You Suck. Devil's Turn.")
                myRndPts = 0
                myTurn = False
                time.sleep(3)

        if r == 'p':
            myPts = myPts + myRndPts
            myRndPts = 0
            die = 0
            printSimpleBoard(die, myPts, devilPts, myTurn, myRndPts, devilRndPts)
            myTurn = False
            time.sleep(3)

        if r == 'q':
            print("GAME OVER YOU LOSE QUITTER!")
            gameRunning = False
            break

    # Devil's Logic
    while not myTurn:
        if devilPts + devilRndPts >= 100:
            print("DEVIL WON!")
            printSimpleBoard(die, myPts, devilPts, myTurn, myRndPts, devilRndPts)
            gameRunning = False
            break

        # If Devil is winning logic 
        if devilPts >= myPts:
            if devilRndPts >= 21:
                devilPts = devilRndPts + devilPts
                devilRndPts = 0
                printSimpleBoard(die, myPts, devilPts, myTurn, myRndPts, devilRndPts)
                myTurn = True
                print("Your Turn.")
                time.sleep(3)
            if devilRndPts < 21:
                die = random.randint(1, 6)
                devilRndPts = devilRndPts + die
                printSimpleBoard(die, myPts, devilPts, myTurn, myRndPts, devilRndPts)
                time.sleep(1)
                if die == 1:
                    print("Devil Rolled A One.")
                    devilRndPts = 0
                    myTurn = True
                    time.sleep(2)

        # If player is winning devil logic
        if devilPts < myPts:
            if devilRndPts >= 30:
                devilPts = devilRndPts + devilPts
                devilRndPts = 0
                printSimpleBoard(die, myPts, devilPts, myTurn, myRndPts, devilRndPts)
                myTurn = True
                print("Your Turn.")
                time.sleep(3)

            if devilRndPts < 30:
                die = random.randint(1, 6)
                devilRndPts = devilRndPts + die
                printSimpleBoard(die, myPts, devilPts, myTurn, myRndPts, devilRndPts)
                time.sleep(1)
                if die == 1:
                    print("Devil Rolled A One.")
                    devilRndPts = 0
                    myTurn = True
                    time.sleep(2)
