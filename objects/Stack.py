from random import shuffle
from objects.Card import Card

class Stack:
    def __init__(self):
        self.data = []
        for i in range(1, 5):
            for card_val in range(1, 14):
                if (card_val < 11):
                    curr_card = Card(str(card_val))
                elif (card_val == 11):
                    curr_card = Card("k")
                elif (card_val == 12):
                    curr_card = Card("q")
                else:
                    curr_card = Card("j")
                self.data.append(curr_card)
        shuffle(self.data)  # shuffle the card stack

    def __le__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        return self.data[-1]

    def __repr__(self):
        return str([self.data[i] for i in range(len(self.data))])