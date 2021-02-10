from bfs_maze import *


class Grids():

    grid1 = ["XXXXXXXXXXXXXXXXXXXX",
                "X     X    X       X",
                "X XXXXX XXXX XXX XXX",
                "X       X      X X X",
                "X X XXX XXXXXX X X X",
                "X X   X        X X X",
                "X XXX XXXXXX XXXXX X",
                "X XXXX   X X X     X",
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
    grid1start = (1,1)
    grid1goal = (19,18)

    grid2 = ['XXXXXX', 'X   XX', 'X X XX', 'X X XX', 'XXXXXX', 'XXXXXX']
    grid2start = (1,1)
    grid2goal = (3,3)

    grid3 = ['XXXXXX', 'X   XX', 'X XXXX', 'X   XX', 'X X XX', 'X X XX', 'X X XX', 'X X XX', 'X XXXX', 'X   XX', 'XXXXXX', 'XXXXXX']
    grid3start = (1,1)
    grid3goal = (9,3)

    grid4 = ['XXXXXXXXXX', 'X     X XX', 'X X XXX XX', 'X X     XX', 'X XXXXXXXX', 'X       XX', 'X XXXXXXXX', 'X       XX', 'XXXXXXXXXX', 'XXXXXXXXXX']
    grid4start = (1,1)
    grid4goal = (7,7)

    grid5 = ['XXXXXXXXXXXXXXXXXXXX', 'X                 XX', 'X X XXXXX XXXXXXXXXX', 'X X     X         XX', 'X XXX X X X X X X XX', 'X   X X X X X X X XX', 'X XXXXXXX XXX X X XX', 'X       X   X X X XX', 'X X XXX XXXXXXX XXXX', 'X X   X       X   XX', 'X X XXXXXXXXX X X XX', 'X X     X   X X X XX', 'X X X XXX XXXXX XXXX', 'X X X         X   XX', 'X X X X XXX XXXXXXXX', 'X X X X   X       XX', 'X X XXX X X XXXXXXXX', 'X X   X X X       XX', 'XXXXXXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXXXXX']
    grid5start = (1,1)
    grid5goal = (17,17)


def test_moves1():
    result = Maze(Grids.grid1, (1, 1)).moves()
    gold = ["E", "S"]
    assert len(result) == len(gold)
    assert set(result) == set(gold)


def test_moves2():
    result = Maze(Grids.grid1, (1, 2)).moves()
    gold = ["E", "W"]
    assert len(result) == len(gold)
    assert set(result) == set(gold)


def test_moves3():
    result = Maze(Grids.grid1, (2, 1)).moves()
    gold = ["N", "S"]
    assert len(result) == len(gold)
    assert set(result) == set(gold)


def test_moves4():
    result = Maze(Grids.grid1, (3, 1)).moves()
    gold = ["N", "E", "S"]
    assert len(result) == len(gold)
    assert set(result) == set(gold)


def test_neighbor1():
    result = Maze(Grids.grid1, (1, 1)).neighbor("S")
    assert Maze(Grids.grid1, (1, 1)).grid == result.grid


def test_neighbor2():
    result = Maze(Grids.grid1, (1, 1)).neighbor("S")
    assert (2, 1) == result.location


def test_neighbor3():
    result = Maze(Grids.grid1, (19, 18)).neighbor("N")
    assert (18, 18) == result.location


def test_bfs1():
    result = Agent().bfs(Maze(Grids().grid1, Grids().grid1start),
                         Maze(Grids().grid1, Grids().grid1goal))
    assert result == ['S', 'S', 'E', 'E', 'E', 'E', 'E', 'E', 'S', 'S', 'E', 'E', 'E', 'E', 'E', 'S', 'S', 'S', 'E', 'E', 'S', 'E', 'E', 'S', 'S', 'S', 'S', 'S', 'E', 'E', 'S', 'S', 'S', 'S', 'S']


def test_bfs2():
    result = Agent().bfs(Maze(Grids().grid2, Grids().grid2start),
                         Maze(Grids().grid2, Grids().grid2goal))
    assert result == ['E', 'E', 'S', 'S']


def test_bfs3():
    result = Agent().bfs(Maze(Grids().grid3, Grids().grid3start),
                         Maze(Grids().grid3, Grids().grid3goal))
    assert result == ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'E', 'E']


def test_bfs4():
    result = Agent().bfs(Maze(Grids().grid4, Grids().grid4start),
                         Maze(Grids().grid4, Grids().grid4goal))
    assert result == ['S', 'S', 'S', 'S', 'S', 'S', 'E', 'E', 'E', 'E', 'E', 'E']


def test_bfs5():
    result = Agent().bfs(Maze(Grids().grid5, Grids().grid5start),
                         Maze(Grids().grid5, Grids().grid5goal))
    assert result == ['S', 'S', 'S', 'S', 'S', 'S', 'E', 'E', 'S', 'S', 'S', 'S', 'E', 'E', 'S', 'S', 'E', 'E',  'E', 'E', 'E', 'E', 'S', 'S', 'S', 'S', 'E', 'E', 'E', 'E', 'E', 'E']




