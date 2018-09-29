from objects.Colors import Colors
from objects.Card import Card

class Board:
    
    EXPECTED_SUM = 10

    def __init__(self):
        self.data = [[Card("-") for i in range(4)] for j in range(4)]
        self.count = 0
        self.map = {0:1, "k": 0, "q": 0, "j": 0}

    def add_count(self):
        """ increase the number of cards by 1 """
        self.count += 1

    def dec_count(self):
        """ decrease the number of cards by 1 """
        self.count -= 1

    def add_card(self, card):
        """ add a card to the map """
        if (not self.is_special(card.value)):
            card.value = int(card.value)
        if card.value in self.map:
            self.map[card.value] += 1
        else:
            self.map[card.value] = 1

    def remove_card(self, card):
        """ remove a card from the map """
        if self.is_special(card.value):
            self.map[card.value] -= 1
        else:
            self.map[int(card.value)] -= 1
            

    def count_pairs(self):
        """ count the number of pairs that add up to 10 when the 
            board is filled """
        pairs = 0
        for r in range(len(self.data)):
            for c in range(len(self.data[r])):
                # iterate through all the items
                curr = self.data[r][c].value
                if (not self.is_special(curr)):
                    minus = self.EXPECTED_SUM - int(curr)
                    if int(curr) == 10:
                        pairs += 1
                    if (minus in self.map):
                        pairs += self.map[minus]
                    if (minus == int(curr)):
                        pairs -= 1
        return int(pairs / 2)

    def is_special(self, data):
        return (str(data) in "jkq-")

    def is_full(self):
        return self.count == 16

    def kings(self):
        return self.map["k"] == 4

    def queens(self):
        return self.map["q"] == 4

    def jacks(self):
        return self.map["j"] == 4

    def game_won(self):
        return (self.kings() and self.queens() and self.jacks())

    def game_lost(self):
        return (self.is_full() and (self.count_pairs() == 0))

    def __repr__(self):
        """ string representation of the board data structure """
        string = "\n"
        for r in range(len(self.data)):
            for c in range(len(self.data[r])):
                special = False
                curr = str(self.data[r][c].value)
                if curr != "-":
                    if curr == "k":
                        string += Colors.ORANGE
                        special = True
                    if curr == "j":
                        string += Colors.PURPLE
                        special = True
                    if curr == "q":
                        string += Colors.CYAN
                        special = True
                string += "  " + str(curr) + "  "
                if special:
                    string += Colors.NORMAL
            string += "\n\n"
        return string
    
