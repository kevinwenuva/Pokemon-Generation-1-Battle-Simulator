"""
This is the class Move, which assigns a move with its type, power, accuracy, and its effect.
"""


class Move(object):
    move_dictionary = {}

    def __init__(self, move):
        move_info = []
        if len(Move.move_dictionary) == 0:
            movedex = open("moves.csv", "r")
            for line in movedex:
                move_list = line.strip().split(",")
                Move.move_dictionary[move_list[0].lower()] = move_list
            movedex.close()
        for key in Move.move_dictionary:
            if key.lower() == move.lower():
                move_info = Move.move_dictionary[key]
                break
        self.name = move_info[0].lower()
        self.type = move_info[1].lower()
        self.category = move_info[2].lower()
        self.power = move_info[3]
        self.accuracy = move_info[4]
        self.pp = int(move_info[5])
        self.effect = move_info[6].lower().strip().split(" ")
        self.description = move_info[7]

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_category(self):
        return self.category

    def get_power(self):
        if self.power == "*":
            return self.power
        else:
            return int(self.power)

    def get_accuracy(self):
        if self.accuracy == "*":
            return self.accuracy
        else:
            return int(self.accuracy)

    def get_pp(self):
        return self.pp

    def get_effect(self):
        return self.effect

    def get_description(self):
        return self.description

    def decrease_pp(self):
        self.pp -= 1

    def set_accuracy(self, modifier):
        self.accuracy *= modifier







