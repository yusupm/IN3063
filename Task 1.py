import numpy as np

class GridGame:
    # Initialising the game class with necessary args
    def __init__(self, height, width, highest):
        self.path = []
        self.grid = np.random.randint(0, highest, size=(height, width))  # creating grid with random numbers between 0 and n with sizes passed in
        # Print the gird in pretty way
        print("Grid:")
        for a in self.grid:
            print("   " + str(a))
        print()
        self.height = height
        self.width = width
        self.posx = 0  # position x of the agent
        self.posy = 0  # position y of the agent
        self.cost = self.grid[self.posy][self.posx]  # cost of movement - starts with cost at position 0,0

    # normal mode 1
    def mode1(self):

        # keep running the process until end point is reached
        while (self.posy != self.height - 1) or (self.posx != self.width - 1):
            goDown = False  # initialise a bool to check if going down is possible
            goRight = False  # initialise a bool to check if going right is possible
            rightCost = 0
            downCost = 0
            # check if a cell is available to move below
            if self.posy < self.height - 1:
                downCost = self.grid[self.posy + 1][self.posx]
                goDown = True

            # check if a cell is available to move right
            if self.posx < self.width - 1:
                rightCost = self.grid[self.posy][self.posx + 1]
                goRight = True

            # check if there is a way to both direction
            if goDown and goRight:
                # compare the costs
                if rightCost > downCost:
                    self.cost = self.cost + downCost
                    self.posy = self.posy + 1  # change agent position
                else:
                    self.cost = self.cost + rightCost  # add the cost to total
                    self.posx = self.posx + 1  # change agent position
                self.path.append((self.posy, self.posx))  # Add position to path to keep track
            else:
                # check which direction is available to move
                if goDown:
                    self.cost = self.cost + downCost
                    self.posy = self.posy + 1
                elif goRight:
                    self.cost = self.cost + rightCost
                    self.posx = self.posx + 1
                self.path.append((self.posy, self.posx))

        return self.cost, self.path

    def mode2(self):
        self.cost = 0  # set the cost to 1 since its start
        # continue looking for paths until end cell is reached
        while (self.posy != self.height - 1) or (self.posx != self.width - 1):
            goDown = False
            goRight = False
            rightCost = 0
            downCost = 0

            if self.posy < self.height - 1:
                # calculate the down cost, absolute value of the difference
                downCost = abs(self.grid[self.posy][self.posx] - self.grid[self.posy + 1][self.posx])
                goDown = True

            if self.posx < self.width - 1:
                # calculate the down cost, absolute value of the difference
                rightCost = abs(self.grid[self.posy][self.posx] - self.grid[self.posy][self.posx + 1])
                goRight = True

            # check if movement to both positions are possible
            if goDown and goRight:
                # compare costs
                if rightCost > downCost:
                    self.cost = self.cost + downCost
                    self.posy = self.posy + 1
                else:
                    self.cost = self.cost + rightCost
                    self.posx = self.posx + 1
                self.path.append((self.posy, self.posx))
            else:
                if goDown:
                    self.cost = self.cost + downCost
                    self.posy = self.posy + 1
                elif goRight:
                    self.cost = self.cost + rightCost
                    self.posx = self.posx + 1
                self.path.append((self.posy, self.posx))

        return self.cost, self.path

    def find_neighbours(self):
        neighbours = []
        positions = []

        if self.posx + 1 < self.width - 1:
            positions.append((self.posy, self.posx + 1))
        if self.posx - 1 > 0:
            positions.append((self.posy, self.posx - 1))
        if self.posy + 1 < self.height - 1:
            positions.append((self.posy + 1, self.posx))
        if self.posy - 1 > 0:
            positions.append((self.posy - 1, self.posx))

        for i in positions:
            neighbours.append((i, self.grid[i[0], i[1]]))
        return neighbours

    def dijkstra(self):
        neighbours = self.find_neighbours()
        unvisited = {}
        visited = {}
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                unvisited[(i, j)] = 999999

        # print(unvisited)
        while unvisited:
            minNode = min(unvisited, key=unvisited.get)
            visited[minNode] = unvisited[minNode]

            for neighbour in neighbours:
                if neighbour in visited:
                    pass
                tempDist = unvisited[minNode] + neighbours[neighbour]
                if tempDist < unvisited[neighbour]:
                    unvisited[neighbour] = tempDist
            unvisited.pop(minNode)
        print(f'{visited=}')

        return self.cost, self.path


def main():
    # Main menu
    print("     Welcome to Grid Game    \n" )
    print("Game types:")
    print("1. Heuristic")
    print("2. Dijkstra")
    gameType = int(input("Choose: "))
    print()
    # While loop to ensure user chose the right mode
    while True:
        print("Game Modes:")
        print("1. Mode 1")
        print("2. Mode 2")
        modeNo = int(input("Choose your mode: "))
        if modeNo > 2:
            print("\nIncorrect Mode, Chose again\n")
            continue
        break
    # user input
    height = int(input("Height of the grid: "))
    width = int(input("Width of the grid: "))
    highest = int(input("Enter max range for random numbers in grid: "))
    # initialise a game class with user input
    game = GridGame(height, width, highest)

    if gameType == 1:
        if modeNo == 1:
            cost, path = game.mode1()
        elif modeNo == 2:
            cost, path = game.mode2()
    else:
        if modeNo == 1:
            cost, path = game.dijkstra1()
    # print final result
    print("Total cost: " + str(cost))
    print("Path: ", end='')
    if path:
        for a in path[:-1]:
            print(a, end=", ")
        print(path[-1:][0])
    else:
        print("N/A")

main()
