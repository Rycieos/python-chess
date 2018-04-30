from enum import Enum

class PieceType(Enum):
  KING   = 'K'
  QUEEN  = 'Q'
  ROOK   = 'R'
  BISHOP = 'B'
  KNIGHT = 'N'
  PAWN   = 'P'

class PieceColor(Enum):
  WHITE = 'w'
  BLACK = 'b'

class Piece(Enum):
  W_KING   = 'K', '♔', PieceType.KING,   PieceColor.WHITE
  W_QUEEN  = 'Q', '♕', PieceType.QUEEN,  PieceColor.WHITE
  W_ROOK   = 'R', '♖', PieceType.ROOK,   PieceColor.WHITE
  W_BISHOP = 'B', '♗', PieceType.BISHOP, PieceColor.WHITE
  W_KNIGHT = 'N', '♘', PieceType.KNIGHT, PieceColor.WHITE
  W_PAWN   = 'P', '♙', PieceType.PAWN,   PieceColor.WHITE
  B_KING   = 'k', '♚', PieceType.KING,   PieceColor.BLACK
  B_QUEEN  = 'q', '♛', PieceType.QUEEN,  PieceColor.BLACK
  B_ROOK   = 'r', '♜', PieceType.ROOK,   PieceColor.BLACK
  B_BISHOP = 'b', '♝', PieceType.BISHOP, PieceColor.BLACK
  B_KNIGHT = 'n', '♞', PieceType.KNIGHT, PieceColor.BLACK
  B_PAWN   = 'p', '♟', PieceType.PAWN,   PieceColor.BLACK

  def __new__(cls, *values):
    obj = object.__new__(cls)
    # first value is canonical value
    obj._value_ = values[0]
    # second value is symbol, also a canonical value
    cls._value2member_map_[values[1]] = obj
    obj._all_values = values
    obj.symbol = values[1]
    obj.type = values[2]
    obj.color = values[3]
    return obj

  def is_white(self):
    return self.color is PieceColor.WHITE

