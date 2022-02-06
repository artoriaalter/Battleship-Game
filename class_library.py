import random
class Vessel:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.initial = name[0]
        self.health = length

class Game:
    vessels = [Vessel("Carrier",5),Vessel("Battleship",4),Vessel("Destroyer",3),Vessel("Submarine",3), Vessel("Patrol Boat",2)]

    def __init__(self,player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.turn_list = [player_1, player_2]
        player_1.vessels = self.vessels
        player_2.vessels = self.vessels


    def change_turn(self):
        self.turn_list.insert(len(self.turn_list)-1, self.turn_list[0])
        self.turn_list.remove(self.turn_list[0])


    def check_placement_feasibility(self, player, indexes, vessel, direction):
        limit = 9
        row_index = indexes[0]
        column_index = indexes[1]
        if direction == "S":
            if limit - row_index + 1 >= vessel.length:
                return True

        elif direction == "N":
            if row_index + 1 >= vessel.length:
                return True

        elif direction == "E":
            if limit - column_index + 1 >= vessel.length:
                return True

        elif direction == "W":
            if column_index + 1 >= vessel.length:
                return True

        return False







    def input_placement(self, player, flag = 0):
        letter_to_index = {'A':0, 'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}
        directions = ["N","S","W","E"]
        while flag < len(self.vessels):
            print("{name} please select where you want to place your {vessel}. Input as A4, J2".format(name = player.name, vessel = self.vessels[flag].name))
            print(player.vessel_board)
            placement_grid = input()
            split_row_column = tuple(placement_grid)

            try:
                row_index = letter_to_index[split_row_column[0]]
                column_index = int(split_row_column[1]) - 1
            except:
                print("An error occurred! Please input again")

            placement_grid = (row_index, column_index)


            direction = input("In which direction you want to place your vessel?")


            while (direction not in directions) or (self.check_placement_feasibility(player, placement_grid, self.vessels[flag], direction) == False):
                print("An error")
                direction = input("In which direction you want to place your vessel? To return to the previous step, please input q")

                if direction == "q":
                    self.input_placement(player, flag = flag)

            #print(self.check_placement_feasibility(self.turn_list[0], placement_grid, self.vessels[flag], direction))


            player.place_vessel(placement_grid, direction, self.vessels[flag])

            print(player.vessel_board)

            flag += 1
            #check for overflow
            """
            if limit - row_index + 1 <= vessels[flag].length:
            turn_list[0].place_vessel()
            """








class Bot:
    pass

class Player:
    def __init__(self,name):
        self.name = name
        self.vessel_board = Board()
        self.record_board = Board()

    def __repr__(self):
        pass

    def place_vessel(self, head_grid, vector, vessel):
        #end and starting points cannot exceed index 9 in both rows and columns
            if vector == "S":
                for placement_grid in range(head_grid[0], head_grid[0] + vessel.length):
                    self.vessel_board.grid[placement_grid][head_grid[1]].append(vessel.initial)
            elif vector == "N":
                for placement_grid in range(head_grid[0], head_grid[0] - vessel.length,-1):
                    self.vessel_board.grid[placement_grid][head_grid[1]].append(vessel.initial)
            elif vector == "E":
                for placement_grid in range(head_grid[1], head_grid[1] + vessel.length):
                    self.vessel_board.grid[head_grid[0]][placement_grid].append(vessel.initial)
            elif vector == "W":
                for placement_grid in range(head_grid[1], head_grid[1] - vessel.length,-1):
                    self.vessel_board.grid[head_grid[0]][placement_grid].append(vessel.initial)






"""
    def make_a_move(self):
        letter_to_index = {'A':0, 'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}

        \"""
        Get input as Row:Column f.i J4, A2, E3
        \"""
        split_row_column = tuple(move)

        row_index = letter_to_index(split_row_column[0])
        column_index = letter_to_index(split_row_column[1])

        return row_index, column_index
"""




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
                    board += "[{}]\t".format(element[0])
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
    G   [[{}][{}][{}][{}][{}][{}][{}][{}][{}][{}]]
    F   [[{}][{}][{}][{}][{}][{}][{}][{}][{}][{}]]
    H   [[{}][{}][{}][{}][{}][{}][{}][{}][{}][{}]]
    I   [[{}][{}][{}][{}][{}][{}][{}][{}][{}][{}]]
    J   [[{}][{}][{}][{}][{}][{}][{}][{}][{}][{}]]

"""
