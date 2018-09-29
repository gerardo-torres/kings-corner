# King's Corner
```
Description:    Terminal-based implementation of the King's Corner card game (solitare style)
Author:         Gerardo Torres
Date:           9/29/2018
Entry File:     main.py
Meta Files:     README.md, README.html
```

- [King's Corner](#king-s-corner)
    - [Rules](#rules)
    - [Playing](#playing)
    - [Design and Data Structures](#design-and-data-structures)
    - [Tools](#tools)
    - [Difficulties and Limitations](#difficulties-and-limitations)
    - [Other files](#other-files)

### Rules
In this card game, there is a 4-by-4 grid of slots. Each slot is initially empty with all the cards being shuffled into a main stack from which the player will select the top most card. 

There are special cards which must be placed in their specified slots in order to win the game. 

The special cards and their placements are:

| Card   | Place on grid  |
|--------|----------------|
| King   | four corners   |
| Queen  | left and right |
| Jack   | top and bottom |

The objective of the game is to have all these special cards in their correct place (regardless of where the number cards are). This would look like [so](http://www.lenagames.com/bp_files/rul/g_kings_corners.gif). Once the player achieves that, they win the game!

Special cards can be placed anywhere on their corresponding places. Cards that are not the special cards are treated as their number values and can be placed anywhere on the grid.

Once the board is filled with cards and the next card from the pile is NOT a special card, the player must remove pairs of cards that add up to ten (Ace is counted as a 1). Once all the cards that add up to ten are removed, the next card from the pile can be placed. 

The game is over when:

- The next card from the pile is a special card and it cannot be placed in its specified slot
- The board is filled and there are no pairs that add up to 10


### Playing
On a terminal, run the python file:

```
python3 main.py
```

You will be greeted with a command-line menu.

- Enter the `play` command in to begin the game.
- To read the rules, enter the `rules` command. 
- To exit the program, enter the `close` command.

The board will be represented in the terminal as follows:

| Item   | symbol         |
|--------|----------------|
| King   |       `k`      |
| Queen  |       `q`      |
| Jack   |       `j`      |
| Empty  |       `-`      |


### Design and Data Structures
A object-oriented approach was taken as there are the following objects:

- `Card`
    - represents a card in the game
    - only contains `value`, a string of the value of the card
- `Stack`
    - represents the stack of cards in the game
    - contains randomized `Card` objects in an array-based last in, first out (LIFO) structure
- `Board`
    - represents the 4-by-4 board in the game
    - contains the user-submitted `Card` objects in a 2D-array-based structure
    - contains a map to bring the `count_pair` method's runtime to `O(n)` where `n` is the number of slots
- `Colors`
    - represents the colors of the special cards for ease-of-use

Each of these objects have methods and data members that in order to make programming easier and more intuitive. 

In addition, the project was divided into two user-oriented loops:

- `main()` which takes in the user's commands
- `play()` which takes in the user's request to play the game and handled the gameplay
- `delete_pairs()` which handles the user's inputs to eliminate pairs of cards


### Tools
Python was used for this program because it is my strongest language and it comes pre-installed with (most) unix systems.

`random` was the only external library that was used since the focus of the project was not on techniques of randomization. 

### Difficulties and Limitations
A few difficulties that came up were 

- the logic of deciding which indicies were valid
- the board's `count_pairs` method's runtime (it was inititally `O(n^2)`)

A limitation of the project is that it does not deal with non-integer inputs well when deciding at which index to place a card (try inputing strings of characters multiple times).

### Other files
This document was written in Markdown and coverted to HTML using [Pandoc](https://gist.github.com/atelierbram/09c8fb742f1518f09ff9e4338ab8f7fb). The CSS file, `assets/style.css` was used to make the document a little cleaner.