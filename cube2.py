import numpy as np 

colors = ['W', 'Y', 'G', 'B', 'R', 'O']
color_dict = {'W': 0, 'Y': 1, 'G': 2, 'B': 3, 'R': 4, 'O': 5}
reverse_color_dict = {0: 'W', 1: 'Y', 2: 'G', 3: 'B', 4: 'R', 5: 'O'}
moves = ["R", "R'", "L", "L'", "U", "U'", "D", "D'", "F", "F'", "B", "B'"]
moves_abridged = ["R", "R'", "U", "U'", "F", "F'"]

class Cube(object):
    """
    Sticker position on each face is denoted in same order as quadrants of coordinate plane.
    """
    def __init__(self):
        self.state = np.array([[x for i in range(4)] for x in colors])
        self.is_featurized = False 

    def rotate(self, side, cw):
        """
        Helper for move; rotate the side along axis of a turn clockwise if cw is True, counterclockwise otherwise.
        """
        temp1 = self.state[side][0]
        if cw:
            self.state[side][0] = self.state[side][1]
            temp2 = self.state[side][3] 
            self.state[side][3] = temp1
            temp1 = self.state[side][2]
            self.state[side][2] = temp2
            self.state[side][1] = temp1 
        else:
            self.state[side][0] = self.state[side][3]
            temp2 = self.state[side][1]
            self.state[side][1] = temp1
            temp1 = self.state[side][2]
            self.state[side][2] = temp2 
            self.state[side][3] = temp1

    def move(self, a):
        """
        State of cube after executing move a.
        """
        assert a in moves, "Not a valid move."
        if a == "R":
            top_right, bottom_right = self.state[0][0], self.state[0][3]
            self.state[0][0], self.state[0][3] = self.state[2][0], self.state[2][3]
            self.state[2][0], self.state[2][3] = self.state[1][0], self.state[1][3]
            self.state[1][0], self.state[1][3] = self.state[3][2], self.state[3][1]
            self.state[3][2], self.state[3][1] = top_right, bottom_right
            self.rotate(4, True)            
        elif a == "R'":
            top_right, bottom_right = self.state[0][0], self.state[0][3]
            self.state[0][0], self.state[0][3] = self.state[3][2], self.state[3][1]
            self.state[3][2], self.state[3][1] = self.state[1][0], self.state[1][3]
            self.state[1][0], self.state[1][3] = self.state[2][0], self.state[2][3]
            self.state[2][0], self.state[2][3] = top_right, bottom_right
            self.rotate(4, False)
        elif a == "L":
            top_left, bottom_left = self.state[0][1], self.state[0][2]
            self.state[0][1], self.state[0][2] = self.state[3][3], self.state[3][0]
            self.state[3][3], self.state[3][0] = self.state[1][1], self.state[1][2]
            self.state[1][1], self.state[1][2] = self.state[2][1], self.state[2][2]
            self.state[2][1], self.state[2][2] = top_left, bottom_left
            self.rotate(5, True)
        elif a == "L'":
            top_left, bottom_left = self.state[0][1], self.state[0][2]
            self.state[0][1], self.state[0][2] = self.state[2][1], self.state[2][2]
            self.state[2][1], self.state[2][2] = self.state[1][1], self.state[1][2]
            self.state[1][1], self.state[1][2] = self.state[3][3], self.state[3][0]
            self.state[3][3], self.state[3][0] = top_left, bottom_left 
            self.rotate(5, False)
        elif a == "U":
            top_left, top_right = self.state[2][1], self.state[2][0]
            self.state[2][1], self.state[2][0] = self.state[4][1], self.state[4][0]
            self.state[4][1], self.state[4][0] = self.state[3][1], self.state[3][0]
            self.state[3][1], self.state[3][0] = self.state[5][1], self.state[5][0]
            self.state[5][1], self.state[5][0] = top_left, top_right
            self.rotate(0, True)
        elif a == "U'":
            top_left, top_right = self.state[2][1], self.state[2][0]
            self.state[2][1], self.state[2][0] = self.state[5][1], self.state[5][0]
            self.state[5][1], self.state[5][0] = self.state[3][1], self.state[3][0]
            self.state[3][1], self.state[3][0] = self.state[4][1], self.state[4][0]
            self.state[4][1], self.state[4][0] = top_left, top_right
            self.rotate(0, False)
        elif a == "D":
            bottom_left, bottom_right = self.state[2][2], self.state[2][3]
            self.state[2][2], self.state[2][3] = self.state[5][2], self.state[5][3]
            self.state[5][2], self.state[5][3] = self.state[3][2], self.state[3][3]
            self.state[3][2], self.state[3][3] = self.state[4][2], self.state[4][3]
            self.state[4][2], self.state[4][3] = bottom_left, bottom_right
            self.rotate(1, True)
        elif a == "D'":
            bottom_left, bottom_right = self.state[2][2], self.state[2][3]
            self.state[2][2], self.state[2][3] = self.state[4][2], self.state[4][3]
            self.state[4][2], self.state[4][3] = self.state[3][2], self.state[3][3]
            self.state[3][2], self.state[3][3] = self.state[5][2], self.state[5][3]
            self.state[5][2], self.state[5][3] = bottom_left, bottom_right
            self.rotate(1, False)
        elif a == "F":
            bottom_right, bottom_left = self.state[0][3], self.state[0][2]
            self.state[0][3], self.state[0][2] = self.state[5][0], self.state[5][3]
            self.state[5][0], self.state[5][3] = self.state[1][1], self.state[1][0]
            self.state[1][1], self.state[1][0] = self.state[4][2], self.state[4][1]
            self.state[4][2], self.state[4][1] = bottom_right, bottom_left
            self.rotate(2, True)
        elif a == "F'":
            bottom_right, bottom_left = self.state[0][3], self.state[0][2]
            self.state[0][3], self.state[0][2] = self.state[4][2], self.state[4][1]
            self.state[4][2], self.state[4][1] = self.state[1][1], self.state[1][0]
            self.state[1][1], self.state[1][0] = self.state[5][0], self.state[5][3]
            self.state[5][0], self.state[5][3] = bottom_right, bottom_left
            self.rotate(2, False)
        elif a == "B":
            top_left, top_right = self.state[0][1], self.state[0][0]
            self.state[0][1], self.state[0][0] = self.state[4][0], self.state[4][3]
            self.state[4][0], self.state[4][3] = self.state[1][3], self.state[1][2]
            self.state[1][3], self.state[1][2] = self.state[5][2], self.state[5][1]
            self.state[5][2], self.state[5][1] = top_left, top_right
            self.rotate(3, True)
        elif a == "B'":
            top_left, top_right = self.state[0][1], self.state[0][0]
            self.state[0][1], self.state[0][0] = self.state[5][2], self.state[5][1]
            self.state[5][2], self.state[5][1] = self.state[1][3], self.state[1][2]
            self.state[1][3], self.state[1][2] = self.state[4][0], self.state[4][3]
            self.state[4][0], self.state[4][3] = top_left, top_right
            self.rotate(3, False)

    def is_solved(self):
        """
        Returns true if cube is in solved state, false otherwise.
        """
        if self.is_featurized:
            self.unfeaturize_state()
            for side in self.state:
                if not np.count_nonzero(side == side[0]) == len(side):
                    self.featurize_state()
                    return False
            self.featurize_state()
        else:
            for side in self.state:
                if not np.count_nonzero(side == side[0]) == len(side):
                    return False
        return True 

    def is_equal(self, other):
        """
        Returns true if self is in the same state as other, where other is also a Cube instance.
        """
        return np.count_nonzero(self.state == other.state) == 24

    def do_moves(self, algo):
        """
        Execute algo, a sequence of moves, onto cube object. 
        """
        split_moves = algo.split()
        for a in split_moves:
            self.move(a)

    def featurize_state(self):
        """
        Reshape state to be a 1 by 24 vector and convert values to be numeric. 
        """
        for side in self.state:
            for i in range(4):
                side[i] = color_dict[side[i]]
        self.state = self.state.reshape((1, 24)).astype('float')
        self.is_featurized = not self.is_featurized

    def unfeaturize_state(self):
        """
        Convert state back to unfeaturized 2d numpy array.
        """
        self.state = list(map(lambda x: reverse_color_dict[int(x)], self.state[0]))
        self.state = np.array(self.state)
        self.state = self.state.reshape((6, 4))
        self.is_featurized = not self.is_featurized
