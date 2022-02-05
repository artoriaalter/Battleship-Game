import random

class Game:
    pass



class Bot:
    pass

class Player:
    pass

class Board:
    def __init__(self):
        self.grid = []
        for x in range(10):
            self.grid.append([])
            for y in range(10):
                self.grid[x].append([])

    def __repr__(self):
        index_to_letter = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J"}
        board = """
        1       2      3       4       5       6       7       8       9       10
        """
        for index in range(len(self.grid)):
            flag = 1
            if flag == 1:
                board += "\n" + index_to_letter[index] + "\t"
                flag += 1
            for element in self.grid[index]:
                if element != []:
                    board += "[{}]".format(element[0])
                else:
                    board += "[]\t"
        return board



#desired board
"""
          1   2   3   4   5   6   7   8   9   10
    A   [[{}][{}][{}][{}][{}][{}][{}][{}][{}][{}]]
    B   [[{}][{}][{}][{}][{}][{}][{}][{}][{}][{}]]
    C   [[{}][{}][{}][{}][{}][{}][{}][{}][{}][{}]]
    D   [[{}][{}][{}][{}][{}][{}][{}][{}][{}][{}]]
    E   [[{}][{}][{}][{}][{}][{}][{}][{}][{}][{}]]
    F   [[{}][{}][{}][{}][{}][{}][{}][{}][{}][{}]]
    G   [[{}][{}][{}][{}][{}][{}][{}][{}][{}][{}]]
    H   [[{}][{}][{}][{}][{}][{}][{}][{}][{}][{}]]
    I   [[{}][{}][{}][{}][{}][{}][{}][{}][{}][{}]]
    J   [[{}][{}][{}][{}][{}][{}][{}][{}][{}][{}]]

"""
