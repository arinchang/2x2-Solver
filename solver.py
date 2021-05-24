import numpy as np 
import sys 
from cube2 import Cube, moves_abridged
from copy import deepcopy

def bfs(scrambled_cube):
    """
    1. at current state, generate all 12 possible resulting states from 12 possible moves (actually only 6 states)
    2. insert these 12 states into fringe
    4. repeat until the goal state is selected for expansion 
    Args:
        scrambled_cube: cube instance that has been scrambled according to user input 
    Returns:
        solution: list containing sequence of moves algorithm took to solve the cube
    """

    fringe = []
    expanded = []
    solution = []
    edgeTo = {}
    current_state = scrambled_cube
    fringe.append(current_state)
    while fringe:
        curr_state = fringe.pop(0)
        if curr_state.is_solved():
            curr = edgeTo[curr_state]
            solution.append(curr[1])
            while curr[0] is not current_state:
                curr = edgeTo[curr[0]]
                solution.append(curr[1])
            solution.reverse()
            return solution 
        flag = True
        for state in expanded:
            if curr_state.is_equal(state):
                flag = False
                break
        if flag: # curr_state hasn't been expanded yet 
            expanded.append(curr_state)
        for i in range(len(moves_abridged)):
            curr_copy = deepcopy(curr_state)
            curr_copy.move(moves_abridged[i])
            fringe.append(curr_copy)
            edgeTo[curr_copy] = curr_state, moves_abridged[i]
    return 

# usage: python3 solver.py [scramble]
if __name__ == '__main__':
    assert len(sys.argv) == 2
    scramble = sys.argv[1]
    cube = Cube()
    cube.do_moves(scramble)
    solution_list = bfs(cube)
    print(" ".join(str(x) for x in solution_list))
