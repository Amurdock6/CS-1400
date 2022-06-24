import time
from collections import namedtuple

SLEEPTIME = 0.1
FILENAME = "maze.txt"
VERBOSE = True

# TODO: write all your code below this line
Dir = namedtuple("Dir", ["char", "dy", "dx"])


class Maze:

    START = "S"
    END = "E"
    WALL = "X"
    PATH = " "
    OPEN = {PATH, END}  # map locations you can move to (not WALL or already explored)

    RIGHT = Dir(".", 0, 1)
    DOWN = Dir(".", 1, 0)
    LEFT = Dir(".", 0, -1)
    UP = Dir(".", -1, 0)
    DIRS = [RIGHT, DOWN, LEFT, UP]

    @classmethod
    def load_maze(cls, fname):
        with open(fname) as inf:
            lines = (line.rstrip("\r\n") for line in inf)
            maze = [list(line) for line in lines]
        return cls(maze)

    def __init__(self, maze):
        self.maze = maze

    def __str__(self):
        return "\n".join(''.join(line) for line in self.maze)

    def find_start(self):
        for y, line in enumerate(self.maze):
            try:
                x = line.index("S")
                return y, x
            except ValueError:
                pass

        # not found!
        raise ValueError("Start location not found")

    def solve(self, y, x):
        if self.maze[y][x] == Maze.END:
            # base case - endpoint has been found
            return True
        else:
            # search recursively in each direction from here
            for dir in Maze.DIRS:
                ny, nx = y + dir.dy, x + dir.dx
                if self.maze[ny][nx] in Maze.OPEN:  # can I go this way?
                    if self.maze[y][x] != Maze.START:  # don't overwrite Maze.START
                        self.maze[y][x] = dir.char  # mark direction chosen
                    if self.solve(ny, nx):  # recurse...
                        return True  # solution found!

            # no solution found from this location
            if self.maze[y][x] != Maze.START:  # don't overwrite Maze.START
                self.maze[y][x] = Maze.PATH  # clear failed search from map
            return False


# put the line "if VERBOSE: printMaze(maze)"
# every time you drop/retrieve a marker

# TODO: write all your code above this line


def readMaze(maze):
    mazefile = open(FILENAME, "r")
    for line in mazefile.read().splitlines():
        maze.append([])
        for c in line:
            maze[-1].append(c)
    mazefile.close()


def printMaze(maze):
    print("\n\n\n\n\n\n\n\n\n")
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            print(maze[i][j], end="")
        print()
    time.sleep(SLEEPTIME)
    print()


def main():
    loadMaze = Maze.load_maze("maze.txt")

    # maze = []
    # readMaze(maze)
    # if not solve(maze, 1, 0):
    #     print("no solution is possible.")
    # else:
    #     printMaze(maze)
    # if VERBOSE:
    #     printMaze(maze)

    try:
        sy, sx = loadMaze.find_start()
        
        if loadMaze.solve(sy, sx):
            print(loadMaze)
        else:
            print("No solution found")
    except ValueError:
        print("No start point found.")


main()
