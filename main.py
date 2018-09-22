from random import shuffle
from objects.Board import Board
from objects.Card import Card
# from folder.file import Klasa

message = "Welcome to the king's corner card game! \n\nCreated by: \tGerardo Torres \nDate: \t\t9/22/2018"
usage = "\n\tUsage: \n-----------------------\nusage\t\tprint this menu\nplay\t\tplay the game\nrules\t\tprint the rules\nclose		close program\n"
rules = """In this card game, there is a 4-by-4 grid of slots. Each slot is initially empty with 	all the cards being shuffled into a main stack from which the player will select the top most card.
There are special cards which must be placed in their specified slots in order to win the game. 

The special cards are and their placements are:

| Card   | place on grid  |
|--------|----------------|
| King   | four corners   |
| Queen  | top and bottom |
| Jack   | left and right |

The objective of the game is to have all these special cards in their correct place.
Cards that are not the special cards are treated as their number values and can be placed anywhere on the grid (although the player should try to avoid placing them in the slots where the special cards should be).

Once the board is filled with cards and the next card from the pile is NOT a special card, the player must remove pairs of cards that add up to ten. Once all the cards that add up to ten are removed, the next card from the pile can be placed. 

If the board is filled with cards and the next card IS a special card OR the special card cannot be placed in its specified slot, the game is over.

The board will be represented in the terminal as follows:

| Item   | symbol         |
|--------|----------------|
| King   |        k       |
| Queen  |        q       |
| Jack   |        j       |
| Empty  |        -       |"""

def build_grid():
    card_stack = []
    for i in range(1, 5):
        for card_val in range(1, 14):
            if (card_val < 11):
                curr_card = Card(card_val)
                card_stack.append(curr_card)
            else:
                special_card = card_val - 10
                if (special_card == 1):
                    card_stack.append("k")
                elif (special_card == 2):
                    card_stack.append("q")
                elif (special_card == 3):
                    card_stack.append("j")
    shuffle(card_stack)  # shuffle the card stack
    return card_stack

def delete_pairs(board):
    board.data = [["-" for i in range(4)] for j in range(4)]
    board.count = 0

def display_board(board):
    print(board)

def coordinate_invalid(row, col, board):
    if (row == -1 and col == -1):
        return True
    if board.data[row][col] == "-":
        return False
    else:
        return True

def row_invalid(row):
    return ((row > 3) or (row < 0))

def col_invalid(col):
    return ((col > 3) or (col < 0))

def play(card_stack):
    """ driver function for the game program """
    board = Board()
    while (True):
        popped_card = card_stack.pop()
        print("current card:", popped_card)
        usr_row = -1
        usr_col = -1
        coordinate_valid = False  # avoid re-wrtitting values if they exist
        while (coordinate_invalid(usr_row, usr_col, board)):
            if (board.is_full()):
                print("it's full")
                delete_pairs(board)
                display_board(board)
            usr_row = int(input("enter row: "))
            while (row_invalid(usr_row)):
                usr_row = int(input("enter row: "))
                if (row_invalid(usr_row)):
                    print("out of range; try again")
            usr_col = int(input("enter col: "))
            while (col_invalid(usr_col)):
                usr_col = int(input("enter col: "))
                if (col_invalid(usr_col)):
                    print("out of range; try again")
            if (coordinate_invalid(usr_row, usr_col, board) and not board.is_full()):
                print("a card already exists in that location")
        board.data[usr_row][usr_col] = popped_card
        board.add_count()
        display_board(board)
        

def main():
    """ main driver function for the terminal program """
    print(message)
    print(usage)
    while (True):
        answer = input("--> ")
        if answer == "close":
            print("closing program")
            return
        elif answer == "usage":
            print(usage)
        elif answer == "rules":
            print(rules)
        elif answer == "play":
            card_stack = build_grid()
            return play(card_stack)
        else:
            print("invalid command")

main()
