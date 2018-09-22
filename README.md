# King's Corner
```
Description:    Terminal-based implementation of the King's Corner card game (solitare style)
Author:         Gerardo Torres
Date:           9/22/2018
Entry File:     main.py
Meta Files:     README.md, README.html
```

### Rules
In this card game, there is a 4-by-4 grid of slots. Each slot is initially empty with all the cards being shuffled into a main stack from which the player will select the top most card. 

There are special cards which must be placed in their specified slots in order to win the game. 

The special cards are and their placements are:

| Card   | place on grid  |
|--------|----------------|
| King   | four corners   |
| Queen  | top and bottom |
| Jack   | left and right |

The objective of the game is to have all these special cards in their correct place.
Cards that are not the special cards are treated as their number values and can be placed anywhere on the grid (although the player should try to avoid placing them in the slots where the special cards should be).

Once the board is filled with cards and the next card from the pile is NOT a special card, the player must remove pairs of cards that add up to ten (Ace is counted as a 1). Once all the cards that add up to ten are removed, the next card from the pile can be placed. 

If the board is filled with cards and the next card IS a special card OR the special card cannot be placed in its specified slot, the game is over.

### Playing
The board will be represented in the terminal as follows:

| Item   | symbol         |
|--------|----------------|
| King   |       `k`      |
| Queen  |       `q`      |
| Jack   |       `j`      |
| Empty  |       `-`      |