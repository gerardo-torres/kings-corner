from objects.Stack import Stack
from objects.Board import Board
from objects.Colors import Colors
from objects.Card import Card

message = "Welcome to the king's corner card game! \n\nCreated by: \tGerardo Torres \nDate: \t\t9/22/2018"
usage = "\n\t   Usage: \n----------------------------\nusage\t\tprint this menu\nplay\t\tplay the game\nrules\t\tprint the rules\nclose		close program\n"
rules = """In this card game, there is a 4-by-4 grid of slots. 
Each slot is initially empty with all the cards being shuffled into a main stack from which the player will select the top most card.
There are special cards which must be placed in their specified slots in order to win the game. 

The special cards are and their placements are:

| Card   | Place on grid  |
|--------|----------------|
| King   | four corners   |
| Queen  | left and right |
| Jack   | top and bottom |

The objective of the game is to have all these special cards in their correct place.
Cards that are not the special cards are treated as their number values and can be placed anywhere on the grid (although the player should try to avoid placing them in the slots where the special cards should be).

Once the board is filled with cards and the next card from the pile is NOT a special card, the player must remove pairs of cards that add up to ten. Once all the cards that add up to ten are removed, the next card from the pile can be placed. 

If the board is filled with cards and the next card IS a special card OR the special card cannot be placed in its specified slot, the game is over.

The board will be represented in the terminal as follows:

|  Item  | Symbol |
|--------|--------|
| King   |    k   |
| Queen  |    q   |
| Jack   |    j   |
| Empty  |    -   |"""

def delete_pairs(board):
    # board.data = [["-" for i in range(4)] for j in range(4)]
    # board.count = 0
    rem_pairs = board.count_pairs()
    if rem_pairs == 0:
        print("you lost!")
        return
    while rem_pairs > 0:
        print("remaining pairs:", rem_pairs)
        usr_row = -1
        usr_col = -1
        usr_row2 = -1
        usr_col2 = -1
        while(not coordinate_integer(usr_row, usr_col, board)):
            usr_row = int(input(Colors.BOLD + "enter row for card 1: " + Colors.NORMAL)) - 1
            while (row_invalid(usr_row)):
                usr_row = int(input(Colors.BOLD + "enter row for card 1: " + Colors.NORMAL)) - 1
                if (row_invalid(usr_row)):
                    print("out of range; try again")
            usr_col = int(input(Colors.BOLD + "enter col for card 1: " + Colors.NORMAL)) - 1
            while (col_invalid(usr_col)):
                usr_col = int(input(Colors.BOLD + "enter col for card 1: " + Colors.NORMAL)) - 1
                if (col_invalid(usr_col)):
                    print("out of range; try again")
        if board.data[usr_row][usr_col].value != 10:
            while (not coordinate_integer(usr_row2, usr_col2, board) or ((usr_col == usr_col2) and (usr_row == usr_row2))):
                usr_row2 = int(input(Colors.BOLD + "enter row for card 2: " + Colors.NORMAL)) - 1
                while (row_invalid(usr_row)):
                    usr_row = int(input(Colors.BOLD + "enter row for card 2: " + Colors.NORMAL)) - 1
                    if (row_invalid(usr_row)):
                        print("out of range; try again")
                usr_col2 = int(input(Colors.BOLD + "enter col for card 2: " + Colors.NORMAL)) - 1
                while (col_invalid(usr_col)):
                    usr_col = int(input(Colors.BOLD + "enter col for card 2: " + Colors.NORMAL)) - 1
                    if (col_invalid(usr_col)):
                        print("out of range; try again")
        card1 = (board.data[usr_row][usr_col])
        if int(card1.value) == 10:
            card2 = Card("0")
        else:
            card2 = board.data[usr_row2][usr_col2]
        if int(card1.value) + int(card2.value) == 10:
            board.data[usr_row][usr_col] = Card("-")
            board.dec_count()
            board.remove_card(card1)
            if int(card1.value) != 10:
                board.data[usr_row2][usr_col2] = Card("-")
                board.dec_count()
                board.remove_card(card2)
        display_board(board)
        rem_pairs = board.count_pairs()

def display_board(board):
    print(board)

def coordinate_integer(r, c, board):
    """ returns true if the coordinate holds an integer """
    if (r == -1 and c == -1):
        return False
    curr_card = board.data[r][c].value
    if str(curr_card) in "kqj-":
        return False
    return True

def coordinate_invalid(r, c, board, popped_card):
    """ returns True if the coordinate is invalid"""
    if (r == -1 and c == -1):
        return True
    if popped_card.value in "kqj":
        if popped_card.value == "k":
            if not((r == 3 or r == 0) and (c == 0 or c == 3)):
                return True
        if popped_card.value == "q":
            if not((r == 1 or r == 2) and (c == 0 or c == 3)):
                return True
        if popped_card.value == "j":
            if not((r == 3 or r == 0) and (c == 1 or c == 2)):
                return True
    if board.data[r][c].value == "-" :
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
    display_board(board)
    while (True):
        popped_card = card_stack.pop()
        print("current card:", popped_card.value)
        if popped_card.value in "kqj":
            if popped_card.value == "k":
                if board.data[0][0].value != "-" and board.data[0][3].value != "-" and board.data[3][0].value != "-" and board.data[3][3].value != "-":
                    print("you lost!")
                    return
            if popped_card.value == "q":
                if board.data[1][0].value != "-" and board.data[2][0].value != "-" and board.data[1][3].value != "-" and board.data[2][3].value != "-":
                    print("you lost!")
                    return
            if popped_card.value == "j":
                if board.data[0][1].value != "-" and board.data[0][2].value != "-" and board.data[3][1].value != "-" and board.data[3][2].value != "-":
                    print("you lost!")
                    return
        usr_row = -1
        usr_col = -1
        while (coordinate_invalid(usr_row, usr_col, board, popped_card)):
            # avoid re-wrtitting values if they exist
            if (board.is_full()):
                print("board is full")
                delete_pairs(board)
                display_board(board)
                print("current card: ", popped_card.value)
            try:
                usr_row = int(input(Colors.BOLD + "enter row: " + Colors.NORMAL)) - 1
            except:
                print("invalid please enter an int")
            while (row_invalid(usr_row)):
                try:
                    usr_row = int(input(Colors.BOLD + "enter row: " + Colors.NORMAL)) - 1
                except:
                    print("invalid please enter an int")
                if (row_invalid(usr_row)):
                    print("out of range; try again")
            try:
                usr_col = int(input(Colors.BOLD + "enter col: " + Colors.NORMAL)) - 1
            except:
                print("invalid please enter an int")
            while (col_invalid(usr_col)):
                try:
                    usr_col = int(input(Colors.BOLD + "enter col: " + Colors.NORMAL)) - 1
                except:
                    print("invalid please enter an int")
                if (col_invalid(usr_col)):
                    print("out of range; try again")
            if (coordinate_invalid(usr_row, usr_col, board, popped_card) and not board.is_full()):
                print("invalid location")
        board.data[usr_row][usr_col] = popped_card
        board.add_count()
        board.add_card(popped_card)
        display_board(board)
        if (board.game_won()):
            print("you won!!!")
            return
        if (board.game_lost()):
            print("you lost...")
            return

def main():
    """ main driver function for the terminal program """
    print(message)
    print(usage)
    while (True):
        answer = input(Colors.GREEN + "--> " + Colors.NORMAL)
        if answer == "close":
            print("closing program")
            return
        elif answer == "usage":
            print(usage)
        elif answer == "rules":
            print(rules)
        elif answer == "play":
            card_stack = Stack()
            return play(card_stack.data)
        else:
            print("invalid command")

main()
