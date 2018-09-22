class Board:
    def __init__(self):
        self.data = [["-" for i in range(4)] for j in range(4)]
        self.count = 0

    def add_count(self):
        self.count += 1

    def count_pairs(self):
        pass

    def is_full(self):
        return self.count == 16

    def kings(self):
        for x in [0, 3]:
            for y in [0, 3]:
                if (self.data[x][y] != "k"):
                    return False
        return True

    def queens(self):
        for x in [1, 2]:
            for y in [0, 3]:
                if (self.data[x][y] != "q"):
                    return False
        return True

    def jacks(self):
        for x in [0, 3]:
            for y in [1, 2]:
                if (self.data[x][y] != "j"):
                    return False
        return True

    def game_won(self):
        return (self.kings and self.queens and self.jacks)

    def __repr__(self):
        string = "\n"
        for row in range(len(self.data)):
            for col in range(len(self.data[row])):
                string += "  " + str(self.data[row][col]) + "  "
            string += "\n\n"
        return string
    
