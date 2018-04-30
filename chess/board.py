from .piece import Piece
from .moves import *

class Board:
  def __init__(self):
    self.board = fen_parse_board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
    self.whites_turn = True
    self.black_king_castle = True
    self.black_queen_castle = True
    self.white_king_castle = True
    self.white_queen_castle = True
    self.en_passant_space = None
    self.fifty_move_rule_moves = 0
    self.full_move_count = 1

  @classmethod
  def fromfen(cls, fen):
    parts = fen.split()
    if len(parts) != 6:
      raise ValueError("FEN does not have exactly 6 required parts")

    board = cls()
    board.board = fen_parse_board(parts[0])
    board.whites_turn = parts[1] == 'w' or parts[1] == 'W'
    board.black_king_castle = Piece.B_KING.value in parts[2]
    board.black_queen_castle = Piece.B_QUEEN.value in parts[2]
    board.white_king_castle = Piece.W_KING.value in parts[2]
    board.white_queen_castle = Piece.W_QUEEN.value in parts[2]
    board.en_passant_space = None if parts[3] == '-' else convert_from_chess_space(parts[3])
    board.fifty_move_rule_moves = int(parts[4])
    board.full_move_count = int(parts[5])
    return board

  _backward = range(7, -1, -1)
  _forward = range(8)

  def print_board(self, invert=False):
    for i in (self._forward if invert else self._backward):
      for j in (self._backward if invert else self._forward):
        space = self.board[i][j]
        print('|{}'.format(space.symbol if isinstance(space, Piece) else ' '), end='')
      print('|')

  def is_whites_turn(self):
    return self.whites_turn

  def is_valid_move(self, move):
    pass

  def move(self, move):
    self.whites_turn = not self.whites_turn
    if self.whites_turn:
      self.full_move_count += 1
    # TODO logic

  def get_fen_board(self):
    string = ""
    for row in reversed(self.board):
      blanks = 0
      for space in row:
        if space is None:
          blanks += 1
          continue
        if blanks != 0:
          string += str(blanks)
          blanks = 0
        string += space.value
      if blanks != 0:
          string += str(blanks)
          blanks = 0
      string += '/'
    return string[:-1]

  def get_fen(self):
    p2 = "w" if self.whites_turn else "b"

    p3 = p4 = ""
    if self.white_king_castle:
      p3 += Piece.W_KING.value
    if self.white_queen_castle:
      p3 += Piece.W_QUEEN.value
    if self.black_king_castle:
      p3 += Piece.B_KING.value
    if self.black_queen_castle:
      p3 += Piece.B_QUEEN.value

    if self.en_passant_space is not None:
      p4 = convert_to_chess_space(*self.en_passant_space)

    return "{} {} {} {} {} {}".format(self.get_fen_board(), p2, p3 or '-',
        p4 or '-', self.fifty_move_rule_moves, self.full_move_count)

def fen_parse_board(fen_board):
  valid_spaces = range(1, 9)
  board = list()
  rows = reversed(fen_board.split('/'))
  for row in rows:
    board_row = list()
    for char in row:
      if char.isdigit() and int(char) in valid_spaces:
        for i in range(int(char)):
          board_row.append(None)
      else:
        board_row.append(Piece(char))
    board.append(board_row)

  if len(board) != 8:
    raise ValueError("FEN board not 8x8, not 8 columns")
  for row in board:
    if len(row) != 8:
      raise ValueError("FEN board not 8x8, not 8 rows")

  return board

