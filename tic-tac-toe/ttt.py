"""
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
import os

PLAYER_SYMBOLS = ('X', 'O')
VICTORY_CONDITIONS = (
    {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, # horizontal
    {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, # vertical
    {0, 4, 8}, {2, 4, 6},            # diagonal 

)

class Game(object):
    def __init__(self):
        self.moves = [] 

    def __str__(self):
        board = list('abcdefghi')
        for i, m in enumerate(self.moves):
            board[m] = PLAYER_SYMBOLS[i % 2]
        return '\n---+---+---\n'.join(
            '|'.join(f' {c} ' for c in row) 
            for row in (board[0:3], board[3:6], board[6:9]))

    def winner(self):
        for i, played in enumerate((set(self.moves[::2]), set(self.moves[1::2]))):
            for needed in VICTORY_CONDITIONS:
                if len(needed  - played) == 0:
                    return i

    def add_move(self, m):
        try:
            mi = ord(m.lower()) - ord('a')
            assert 0 <= mi < 9
            assert mi not in self.moves
        except (AttributeError, TypeError, AssertionError):
            return False
        self.moves.append(mi)
        return True

    def next_player(self):
        return len(self.moves) % 2


if __name__ == '__main__':
    g = Game()
    while g.winner() is None:
        os.system('clear')
        print(g)
        print()
        while True:
            m = input(f'Player {PLAYER_SYMBOLS[g.next_player()]} turn: ')
            if g.add_move(m):
                break
            print('Invalid move!')
    print(f'Player {PLAYER_SYMBOLS[g.winner()]} wins!')

