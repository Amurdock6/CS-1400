# Alexander Murdock
# CS-1400-002

import random


# the chess piece super class
class ChessPiece:
    def __init__(self, color, x, y):
        self.__color = color
        self.__x = x
        self.__y = y

    def color(self):
        return self.__color

    def location(self):
        return self.__x, self.__y

    def x(self):
        return self.__x

    def y(self):
        return self.__y


# TODO: write all your code below this line

class Pawn:
    def __init__(self, c, x, y):
        self.__color = c
        self.__x = x
        self.__y = y
    
    def pic(self):
        if self.__color == 'w':
            return '♙'
        elif self.__color == 'b':
            return '♟'
    
    def location(self):
        return self.__x, self.__y
        
    def x(self):
        return self.__x
    
    def y(self):
        return self.__y
    
    def validMove(self, j, i):
        return 1
        

class Queen:
    def __init__(self, c, x, y):
        self.__color = c
        self.__x = x
        self.__y = y
    
    def pic(self):
        if self.__color == 'w':
            return '♕'
        elif self.__color == 'b':
            return '♛'

    def location(self):
        return self.__x, self.__y
    
    def x(self):
        return self.__x
    
    def y(self):
        return self.__y
    
    def validMove(self, j, i):
        return 1


class King:
    def __init__(self, c, x, y):
        self.__color = c
        self.__x = x
        self.__y = y

    def pic(self):
        if self.__color == 'w':
            return '♔'
        elif self.__color == 'b':
            return '♚'
    
    def location(self):
        return self.__x, self.__y
    
    def x(self):
        return self.__x
    
    def y(self):
        return self.__y
    
    def validMove(self, j, i):
        return 1
        
    
class Rook:
    def __init__(self, c, x, y):
        self.__color = c
        self.__x = x
        self.__y = y

    def pic(self):
        if self.__color == 'w':
            return '♖'
        elif self.__color == 'b':
            return '♜'

    def location(self):
        return self.__x, self.__y
    
    def x(self):
        return self.__x
    
    def y(self):
        return self.__y
    
    def validMove(self, j, i):
        return 1
        

class Knight:
    def __init__(self, c, x, y):
        self.__color = c
        self.__x = x
        self.__y = y

    def pic(self):
        if self.__color == 'w':
            return '♘'
        elif self.__color == 'b':
            return '♞'
    
    def location(self):
        return self.__x, self.__y
    
    def x(self):
        return self.__x
    
    def y(self):
        return self.__y
    
    def validMove(self, j, i):
        return 1
    

class Bishop:
    def __init__(self, c, x, y):
        self.__color = c
        self.__x = x
        self.__y = y
        
    def pic(self):
        if self.__color == 'w':
            return '♗'
        elif self.__color == 'b':
            return '♝'
        
    def location(self):
        return self.__x, self.__y
    
    def x(self):
        return self.__x
    
    def y(self):
        return self.__y

    def validMove(self, j, i):
        return 
  
  
# TODO: write all your code above this line
# print a nice picture of the valid moves 
# white pawns only move "up" one space
# black pawns only move "down" one space
# other chess pieces move normally
def printValidMoves(cp):
    print("\t  ", cp.pic(), "at", cp.location())
    for i in range(7, -1, -1):
        print("\t" + str(i) + " ", end="")
        for j in range(0, 8):
            if cp.x() == j and cp.y() == i:
                print(str(cp.pic()) + " ", end="")
            elif cp.validMove(j, i):
                print("* ", end="")
            else:
                print(". ", end="")
        print()
    print("\t  ", end="")
    for i in range(0, 8):
        print(str(i) + " ", end="")
    print()
    print()


# returns a random chess piece at a random location
# each of these types must inherit from ChessPiece
def randomChessPiece():
    if random.randint(0, 1) == 0:
        c = "w"
    else:
        c = "b"
    t = random.randint(1, 6)
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    if t == 1: 
        return Pawn(c, x, y)
    if t == 2: 
        return Queen(c, x, y)
    if t == 3: 
        return King(c, x, y)
    if t == 4: 
        return Rook(c, x, y)
    if t == 5:
        return Knight(c, x, y)
    else:
        return Bishop(c, x, y)


def main():
    clist = []
    # make a list of random chess pieces
    for i in range(0, 10):
        clist.append(randomChessPiece())
    # display their valid moves
    for i in range(0, len(clist)):
        # behold! polymorphism works!
        printValidMoves(clist[i])


main()
