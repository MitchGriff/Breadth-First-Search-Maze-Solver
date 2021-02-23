import time


class Maze():
    """A pathfinding problem."""

    def __init__(self, grid, location, path = ''):
        """Instances differ by their current agent locations."""
        self.grid = grid
        self.location = location
        self.path = path

    def display(self):
        """Print the maze, marking the current agent location."""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if (r, c) == self.location:
                    print('\033[96m*\x1b[0m', end=' ')   # print a blue *
                else:
                    print(self.grid[r][c], end=' ')      # prints a space or wall
            print()
        print()

    def moves(self):
        """Return a list of possible moves given the current agent location."""
        y, x = self.location
        newFrontier = []
        # check N
        if self.grid[y-1][x] == " ":
            newFrontier.append("N")
        # check E
        if self.grid[y][x+1] == " ":
            newFrontier.append("E")
        # check S
        if self.grid[y+1][x] == " ":
            newFrontier.append("S")
        # check W
        if self.grid[y][x-1] == " ":
            newFrontier.append("W")
        return newFrontier

    def neighbor(self, move):
        """Return another Maze instance with a move made."""
        # YOU FILL THIS IN
        y, x = self.location
        if move == 'N':
            y = y - 1
        if move == 'E':
            x = x + 1
        if move == 'S':
            y = y + 1
        if move == 'W':
            x = x - 1
        return Maze(self.grid, (y, x), self.path + move)


class Agent():
    """Knows how to find the exit to a maze with BFS."""

    def bfs(self, maze, goal):
        """Return an ordered list of moves to get the maze to match the goal."""
        # YOU FILL THIS IN
        startTime = time.perf_counter()
        frontier = [maze]   # Frontier list
        visited = [maze.location]    # Visited Nodes
        total_nodes = 0
        while len(frontier) > 0:
            # new frontier for next tree level
            next_level_frontier = []
            # Loop through Frontier
            for maze in frontier:
                # Loop through moves for current maze
                for move in maze.moves():
                    # Make new maze for
                    new_maze = maze.neighbor(move)
                    # Check if the new maze is at the goal
                    if new_maze.location == goal.location:
                        # Count final node
                        total_nodes = total_nodes + 1
                        # Create array from maze.path
                        returnPath = [char for char in new_maze.path]
                        # Stop timer
                        stopTime = time.perf_counter()
                        print("Total nodes visited:", total_nodes)
                        print(f"Maze completed in {stopTime - startTime:0.5f} seconds")
                        print("Length of path:", len(returnPath))
                        return returnPath
                    # Check if new maze has been visited
                    if new_maze.location not in visited:
                        # Add node to visited
                        visited.append(new_maze.location)
                        # Add to next level
                        next_level_frontier.append(new_maze)
                        # Count node in total nodes
                        total_nodes = total_nodes + 1
            # Set Frontier to new_frontier too loop through next level of bfs discovered nodes
            frontier = next_level_frontier


def main():
    """Create a maze, solve it with BFS, and console-animate."""

    grid = ["XXXXXXXXXXXXXXXXXXXX",
            "X     X    X       X",
            "X XXXXX XXXX XXX XXX",
            "X       X      X X X",
            "X X XXX XXXXXX X X X",
            "X X   X        X X X",
            "X XXX XXXXXX XXXXX X",
            "X XXX    X X X     X",
            "X    XXX       XXXXX",
            "XXXXX   XXXXXX     X",
            "X   XXX X X    X X X",
            "XXX XXX X X XXXX X X",
            "X     X X   XX X X X",
            "XXXXX     XXXX X XXX",
            "X     X XXX    X   X",
            "X XXXXX X XXXX XXX X",
            "X X     X  X X     X",
            "X X XXXXXX X XXXXX X",
            "X X                X",
            "XXXXXXXXXXXXXXXXXX X"]

    maze = Maze(grid, (1, 1))
    maze.display()

    agent = Agent()
    goal = Maze(grid, (19, 18))
    path = agent.bfs(maze, goal)

    while path:
        move = path.pop(0)
        maze = maze.neighbor(move)
        time.sleep(0.50)
        maze.display()


if __name__ == '__main__':
    main()
