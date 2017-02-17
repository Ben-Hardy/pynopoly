import os, random


class Property:
    loc = 0
    name = ""
    value = 0

    def __init__(self, loc, name, value):
        self.loc = loc
        self.name = name
        self.value = value

    def __str__(self):
        return "loc: {}, name: {}, value: {}".format(self.loc, self.name, self.value)


class Player:
    number = 0
    loc = 0
    props = []
    cash = 0

    def __init__(self, num):
        self.number = num

properties = []


# set up the board by reading in file info on the board squares
def setup():
    i = 0
    file_op = open("board_info.txt", "r")
    for line in file_op:
        properties.append(Property(i, line.split("/")[0], int(line.split("/")[1])))
        i += 1
    file_op.close()


def roll():
    roll_one = random.randint(1,6)
    roll_two = random.randint(1,6)

    # If doubles, let the game know so rules can be applied appropriately
    if roll_one == roll_two:
        return [roll_one + roll_two, True]
    else:
        return [roll_one + roll_two, False]


def run():
    players = []
    for i in range(1,5):
        players.append(Player(i))
    for i in range(20):
        for player in players:
            roll_amount = roll()[0]
            player.loc += roll_amount
            if player.loc > 39:
                player.loc -= 40
                player.cash += 200
            print("Player {} rolled {} and is currently at {}".format(player.number, roll_amount, properties[player.loc].name))
    for player in players:
        print("Player {}: ${}".format(player.number, player.cash))



def main():
    setup()
    run()


if __name__ == '__main__':
    main()