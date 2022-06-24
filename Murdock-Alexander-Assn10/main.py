# Alexander Murdock
# CS-1400-002

import random
import time


# write all your code below this line
class Card:
    def __init__(self, num=1, suit="S"):
        # each card has a number value between 1 and 13 (inclusive)
        # each card has a suit: "C", "D", "H", and "S"
        self.__num = num
        self.__suit = suit
        

    def __lt__(self, other):
        # define which cards are less than others for sorting
        # first decide by card suit, in alphabetical order
        # then decide by card number
        if self.__suit < other.__suit: return True
        if self.__suit > other.__suit: return False
        return self.__num < other.__num

    def print(self):
        # print out a card (see example output for details)
        if self.__num == 1:
            printstring = " A"
        elif self.__num == 11:
            printstring = " J"
        elif self.__num == 12:
            printstring = " Q"
        elif self.__num == 13:
            printstring = " K"
        else:
            printstring = format(self.__num, "2d")

        if self.__suit == "C": printstring += "\u2663"
        if self.__suit == "D": printstring += "\u2662"
        if self.__suit == "H": printstring += "\u2661"
        if self.__suit == "S": printstring += "\u2660"
        print(printstring, end=" ")

    def blackJackValue(self):
        # return the value of a card.
        # face cards are worth 10
        # aces are worth 11 always here
        retval = self.__num
        if retval == 11: retval = 10
        if retval == 12: retval = 10
        if retval == 13: retval = 10
        if retval == 1: retval = 11
        return retval


class Deck:
    def __init__(self):
        # create a deck of 52 cards in order
        self.cards = []
        self.build()

    def build(self):
        for s in ["\u2663", "\u2662", "\u2661", "\u2660"]:
            for n in range(1, 14):
                if n == 1:
                    n = " A"
                elif n == 11:
                    n = " J"
                elif n == 12:
                    n = " Q"
                elif n == 13:
                    n = " K"
                else:
                    n = format(n, "2d")

                str(n)
                singleCard = "%s%s" % (n,s)
                self.cards.append(singleCard)
                print("%s%s" % (n, s))

    def print(self):
        # print all the cards in the deck, one per line
        for c in self.cards:
            print(c)

    def shuffle(self):
        # randomly shuffle all the cards in the deck
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def arrange(self):
        # put all the cards currently in the deck back in order
        return

    def restore(self):
        # restore all the missing cards from the deck and arrange them
        return

    def deal(self):
        # remove a card from the top of the deck and return it to the client
        return 

    def numCards(self):
        # return the number of cards currently in the deck
        return


class Hand:
    def __init__(self):
        # create an empty list of cards
        return

    def addCard(self, card):
        # add a card to the hand (for example, from the deck)
        return

    def numCards(self):
        # return the number of cards currently in the hand
        return

    def print(self):
        # print the cards currently in the hand, without newlines
        # see example output for details
        return

    def printBlackJackDealer(self):
        # print the cards currently in the hand, without newlines
        # replace the first card with "??" to hide it
        # see example output for details
        return

    def blackJackValue(self):
        # return the blackjack value of this hand
        # aces are worth 11 unless that causes a bust.
        # then the minimum number of aces are counted as 1s
        # so that no bust occurs. ("bust" == any value over 21)
        return


# write all your code above this line


class BlackJackGame:
    def __init__(self):
        self.__d = Deck()
        self.__d.shuffle()

    def displayLine(self, who, hand):
        # print a "hand" line of the output
        print(who + ": ", end="")
        print(" (" + str(hand.blackJackValue()) + ")\t", end="")
        hand.print()
        if hand.numCards() <= 5: print("\t", end="")
        if hand.numCards() <= 3: print("\t", end="")

    def pickWinner(self, n, dn, b, db, pf, df):
        # print out the winner of the hand
        print()
        if n and not dn:
            print("\t\tyou win!")
        elif n and dn:
            print("\t\t(push)")
        elif not n and dn:
            print("\t\tdealer wins.")
        elif b and not db:
            print("\t\tdealer wins.")
        elif not b and db:
            print("\t\tyou win!")
        elif pf == df:
            print("\t\t(push)")
        elif pf > df:
            print("\t\tyou win!")
        else:
            print("\t\tdealer wins.")
        print()

    def play(self):
        print()
        print("        Welcome to Simple BlackJack")
        print()

        # the main event loop
        while True:
            # dealer reshuffles cards when 75% dealt
            if self.__d.numCards() < 14:
                print("\t\t\t\t\tDealer shuffles the deck")
                self.__d.restore()
                self.__d.shuffle()

            # dealer and player each have a hand
            dealer = Hand()
            player = Hand()

            # flags used to determine the eventual winner
            natural = False
            dnatural = False
            busted = False
            dbusted = False
            playerfinal = 0
            dealerfinal = 0

            # dealer gets a hand
            dealer.addCard(self.__d.deal())
            dealer.addCard(self.__d.deal())

            # dealer hand displayed with one card hidden 
            print("dealer" + ": ", end="")
            print(" (??)\t", end="")
            dealer.printBlackJackDealer()
            print()

            # player gets a hand
            player.addCard(self.__d.deal())
            player.addCard(self.__d.deal())

            # check for player natural
            if player.blackJackValue() == 21:
                self.displayLine("player", player)
                print("natural blackjack!")
                natural = True

            # player get more cards if desired
            while player.blackJackValue() < 21:
                self.displayLine("player", player)
                response = input("hit? [y/n] ")
                if response == "n": break
                player.addCard(self.__d.deal())

            # find final player status for hand
            self.displayLine("player", player)
            playerfinal = player.blackJackValue()
            if playerfinal == 21 and not natural:
                print("blackjack!")
            elif playerfinal > 21:
                print("you busted.")
                busted = True
            else:
                print("you hold.")

            time.sleep(1)

            # now it is the dealers turn
            if dealer.blackJackValue() == 21:
                self.displayLine("dealer", dealer)
                print("dealer blackjack!")
                dnatural = True

            # if player busted, dealer does nothing
            if busted:
                self.displayLine("dealer", dealer)
                print()

            # dealer gets to add cards if no naturals
            if not natural and not busted:
                while dealer.blackJackValue() <= 15 and not busted:
                    self.displayLine("dealer", dealer)
                    print("dealer hits.")
                    time.sleep(1)

                    dealer.addCard(self.__d.deal())

                # find final dealer status for hand
                self.displayLine("dealer", dealer)
                dealerfinal = dealer.blackJackValue()
                if dealerfinal == 21 and not dnatural:
                    print("dealer blackjack!")
                elif dealerfinal > 21:
                    print("dealer busted.")
                    dbusted = True
                else:
                    print("dealer holds.")
            time.sleep(1)

            # find the winner for this hand
            self.pickWinner(natural, dnatural, busted, dbusted, playerfinal, dealerfinal)

            response = input("\t\t\t\t\tplay again? [y/n] ")
            if response == "n": break

        print("\t\t\t\t\tso long!")
        print()


def cardTest():
    print()
    print("Card Test")
    print()
    c1 = Card()
    c2 = Card(13, "H")
    c3 = Card(3, "C")
    c4 = Card(3, "D")

    c1.print()
    c2.print()
    c3.print()
    c4.print()
    print()
    print(format(c1.blackJackValue(), "3.0f"), end=" ")
    print(format(c2.blackJackValue(), "3.0f"), end=" ")
    print(format(c3.blackJackValue(), "3.0f"), end=" ")
    print(format(c4.blackJackValue(), "3.0f"), end=" ")
    print()
    print()

    c0 = Card(13, "C")
    c1 = Card(1, "D")
    c2 = Card(2, "D")
    c3 = Card(3, "D")
    c4 = Card(10, "D")
    c5 = Card(11, "D")
    c6 = Card(12, "D")
    c7 = Card(13, "D")
    c8 = Card(1, "H")
    c9 = Card(1, "S")
    c0.print()
    c1.print()
    c2.print()
    c3.print()
    c4.print()
    c5.print()
    c6.print()
    c7.print()
    c8.print()
    c9.print()
    print()
    print(c0 < c1)
    print(c1 < c2)
    print(c2 < c3)
    print(c3 < c4)
    print(c4 < c5)
    print(c5 < c6)
    print(c6 < c7)
    print(c7 < c8)
    print(c8 < c9)
    print(c9 < c0)


def deckTest():
    print()
    print("Deck Test")
    print()
    d = Deck()
    d.print()
    print()
    d.shuffle()
    d.print()
    print()
    print("I Have Not Completed The Game Yet")
    # d.arrange()
    # d.print()
    # print()
    # c0 = d.deal()
    # c1 = d.deal()
    # c0.print()
    # c1.print()
    # print()
    # print()
    # d.print()
    # print()
    # print(d.numCards())
    # d.restore()
    # print(d.numCards())
    # print()
    # d.print()
    # print()


def handTest():
    print()
    print("Hand Test")
    print()
    c1 = Card(1, "S")
    c2 = Card(13, "H")
    c3 = Card(3, "C")
    h = Hand()
    h.addCard(c1)
    h.addCard(c2)
    h.print()
    print()
    print(h.numCards())
    h.addCard(c3)
    h.print()
    print()
    print(h.numCards())
    print()

    h2 = Hand()
    h2.addCard(c1)
    h2.addCard(c2)
    h2.printBlackJackDealer()
    print()
    h2.print()
    print("=", h2.blackJackValue())
    print()
    h2.addCard(c3)
    h2.print()
    print("=", h2.blackJackValue())
    print()


def test():
    cardTest()
    deckTest()


#    handTest()


def main():
       # game = BlackJackGame()
       # game.play()

    test()


main()
