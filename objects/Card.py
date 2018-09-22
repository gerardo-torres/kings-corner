class Card:
    def __init__(self, value):
        self.value = value
        self.slots = Card.determineSlots(self, value)
    
    def determineSlots(self, value):
        if (value == "k"):
            return [(0, 0), (3, 0), (0, 3), (3, 3)]
        if (value == "q"):
            return [(1, 0), (2, 0), (1, 3), (2, 3)]
        if (value == "j"):
            return [(0, 2), (0, 2), (3, 1), (3, 2)]
        else: # all the other cards
            return [(1, 1), (2, 1), (1, 2), (2, 2)]

    def __repr__(self):
        return str(self.value)