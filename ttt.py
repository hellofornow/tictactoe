"""
TicTacToe

x goes first
board is a list of 9 elements from ['x','o','.']. '.' means empty spot.
"""

import types


class GameStates(object):
    """
    there are lots of ways to accomplish an enum like object
    this is the one we're going with since it's simple
    """
    invalid = 'invalid'
    unfinished = 'unfinished'
    x_wins = 'x wins'
    o_wins = 'o wins'
    draw = 'draw'


def game_state(board):
    return Board(board).current_state()


class Board(object):
    """
    I represent a Tic Tac Toe board.
    """

    def __init__(self, board):
        """
        :param board: an array of 9 chars representing the current
           state. Each char is either 'x', 'o' or '.'
        """
        self._board = board

    def row(self, n):
        return self._board[n*3:n*3+3]

    def col(self, n):
        ret = []
        for i in range(3):
            ret.append(self._board[n+i*3])

        return ret

    def diag(self, n):
        "0 is diag down-left \, 1 is diag down-right /"
        ret = []
        if n == 0:
            for i in range(3):
                ret.append(self._board[i*4])
        if n == 1:
            for i in range(3):
                ret.append(self._board[2+i*2])

        return ret

    def current_state(self):
        if not isinstance(self._board, types.ListType):
            return GameStates.invalid

        if len(self._board) != 9:
            return GameStates.invalid

        for c in self._board:
            if c not in ('x', 'o', '.'):
                return GameStates.invalid

        if abs(self._board.count('x') - self._board.count('o')) > 1:
            return GameStates.invalid

        if self._board.count('x') < self._board.count('o'):
            return GameStates.invalid

        if self.is_winner('x') > 1 or self.is_winner('o') > 1:
            return GameStates.invalid

        if self.is_winner('x') >= 1 and self.is_winner('o') >= 1:
            return GameStates.invalid

        if self.is_winner('x') == 1:
            return GameStates.x_wins

        if self.is_winner('o') == 1:
            return GameStates.o_wins

        if self._board.count(".") == 0:
            return GameStates.draw

        return GameStates.unfinished

    def same(self, three):
        return three.count(three[0]) == 3

    def winner(self, three):
        if self.same(three):
            return three[0]
        return False

    def is_winner(self, c):
        "return number of times c has won"
        count = 0
        for i in range(3):
            r = self.row(i)
            if self.winner(r) == c:
                count += 1

            col = self.col(i)
            if self.winner(col) == c:
                count += 1

        if self.winner(self.diag(0)) == c:
            count += 1

        if self.winner(self.diag(1)) == c:
            count += 1

        return count
