from enum import Enum

class Piece(Enum):
  W_KING = '♔'
  W_QUEEN = '♕'
  W_ROOK = '♖'
  W_BISHOP = '♗'
  W_KNIGHT = '♘'
  W_PAWN = '♙'
  B_KING = '♚'
  B_QUEEN = '♛'
  B_ROOK = '♜'
  B_BISHOP = '♝'
  B_KNIGHT = '♞'
  B_PAWN = '♟'

class Board:
  def __init__(self):
    self.whites_turn = True
    self.board = [
        [Piece.B_ROOK, Piece.B_KNIGHT, Piece.B_BISHOP, Piece.B_QUEEN,
          Piece.B_KING, Piece.B_BISHOP, Piece.B_KNIGHT, Piece.B_ROOK],
        [Piece.B_PAWN] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [Piece.W_PAWN] * 8,
        [Piece.W_ROOK, Piece.W_KNIGHT, Piece.W_BISHOP, Piece.W_QUEEN,
          Piece.W_KING, Piece.W_BISHOP, Piece.W_KNIGHT, Piece.W_ROOK]]

  def print(self):
    for i in range(8):
      for j in range(8):
        space = self.board[i][j]
        if isinstance(space, Piece):
          space = space.value
        else:
          space = ' '
        print('|{}'.format(space), end='')
      print('|')

  def is_whites_turn(self):
    return self.whites_turn

  def is_valid_move(self, move):
    pass

  def move(self, move):
    self.whites_turn = not self.whites_turn
    # TODO logic

