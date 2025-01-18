"""
Option 1:
    - Model the state as the state of the board
    - e.g. 3x3 array of arrays with player tokens for each item
    - New moves are entered as (x, y) coords
    - New moves are valid if array location is empty
    - ...how to compute victory?
    - Printing the board is basically printing the state
    - Maybe we also store who is the current player
    - Would we need to be able to undo move?
    - We wouldn't be able to reply the game? Or save partial game in a database and continue?

Option 2:
    - Model the state as the sequence of moves
    - Derive the board current from the prior seq of moves
    - Computing victory is comparably hard/easy
    - A little more work to validate moves?
    - If we want to support replaying ir undoing move etc, this will be straightforward

We'll use option 2
1). State is a sequence of moves in a python list
2). Each move will be modeled as an integer between 0 and eight inclusive
3). Validation: must be an integer in range that hasn't already been selected

functions:
    add_move(moves, m) --> True/False
        - validate the move
        - append m to moves
    check_winner(moves) -> 0, 1 or None
        - deinterleave played move into those played by player 0 and player 1 e.g. [0, 9, 1, 2] would become [0, 1, 2] and [9, 8]
        - treat each player's moves as sets
        - compare the played moves to victory condition move sets, e.g. {0, 1, 2} would be a horizontal victory
        - substracting played set from victory condition set results in an empty or non-empty set ... if empty, that player has won
    print_board(moves)
        - reformat 1 x 9 list as 3 x 3 grid, for printing
        - have default items of A to I, so that player can select which square to play
        - for each move that has been made, overwrite the placeholder ketter with x or 0
    next_player(moves)
        -len(moves) % 2
"""



