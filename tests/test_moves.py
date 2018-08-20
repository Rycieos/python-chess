#!/usr/bin/env pytest

import pytest

from chess.moves import *
from chess.piece import *

def test_space_on_board():
  assert space_on_board(0, 0)
  assert space_on_board(1, 1)
  assert space_on_board(7, 7)

  assert not space_on_board(-1, 0)
  assert not space_on_board(0, -1)
  assert not space_on_board(-1, -1)

  assert not space_on_board(8, 0)
  assert not space_on_board(0, 8)
  assert not space_on_board(8, 8)

  assert not space_on_board(.5, 0)
  assert not space_on_board('a', 1)
  assert not space_on_board(2, None)

def test_convert_from_chess_space():
  assert convert_from_chess_space('a1') == (0, 0)
  assert convert_from_chess_space('h8') == (7, 7)
  assert convert_from_chess_space('c7') == (2, 6)
  with pytest.raises(ValueError):
    convert_from_chess_space('i8')
  with pytest.raises(ValueError):
    convert_from_chess_space('')
  with pytest.raises(ValueError):
    convert_from_chess_space('1a')
  with pytest.raises(ValueError):
    convert_from_chess_space('a0')
  with pytest.raises(ValueError):
    convert_from_chess_space('a9')
  with pytest.raises(ValueError):
    convert_from_chess_space('a2a')

def test_convert_to_chess_space():
  assert convert_to_chess_space(0, 0) == 'a1'
  assert convert_to_chess_space(7, 7) == 'h8'
  assert convert_to_chess_space(2, 6) == 'c7'
  with pytest.raises(ValueError):
    convert_to_chess_space(-1, 6)
  with pytest.raises(ValueError):
    convert_to_chess_space(0, 8)
  with pytest.raises(ValueError):
    convert_to_chess_space(2, None)

def test_valid_piece_move():
  assert is_valid_piece_move(Piece("K"), (0, 0, 1, 1))
  assert not is_valid_piece_move(Piece("k"), (0, 0, 5, 1))
  assert is_valid_piece_move(Piece("q"), (0, 0, 3, 3))
  assert not is_valid_piece_move(Piece("Q"), (0, 0, 5, 2))
  assert is_valid_piece_move(Piece("R"), (0, 0, 4, 0))
  assert not is_valid_piece_move(Piece("r"), (0, 0, 5, 1))
  assert is_valid_piece_move(Piece("B"), (0, 0, 3, 3))
  assert not is_valid_piece_move(Piece("b"), (0, 0, 3, 2))
  assert is_valid_piece_move(Piece("N"), (0, 0, 2, 1))
  assert not is_valid_piece_move(Piece("n"), (0, 0, 5, 1))
  assert is_valid_piece_move(Piece("P"), (0, 0, 1, 1))
  assert is_valid_piece_move(Piece("P"), (0, 0, 0, 1))
  assert not is_valid_piece_move(Piece("P"), (1, 1, 1, 0))
  assert is_valid_piece_move(Piece("p"), (1, 6, 1, 5))
  assert is_valid_piece_move(Piece("p"), (1, 6, 1, 4))
  assert not is_valid_piece_move(Piece("p"), (1, 6, 1, 7))
  with pytest.raises(ValueError):
    is_valid_piece_move("K", (1, 6, 1, 7))
  with pytest.raises(ValueError):
    is_valid_piece_move(None, (1, 6, 1, 7))

def test_all_valid_knight_moves():
  assert valid_knight_moves(0, 0) == {(2, 1), (1, 2)}
  assert valid_knight_moves(1, 1) == {(0, 3), (2, 3), (3, 2), (3, 0)}
  assert valid_knight_moves(3, 3) == {(5, 4), (5, 2), (1, 4), (1, 2),
                                      (4, 5), (2, 5), (4, 1), (2, 1)}

def test_valid_knight_move():
  assert is_valid_knight_move(3, 3, 2, 5)
  assert not is_valid_knight_move(3, 3, 2, 4)
  assert not is_valid_knight_move(3, 3, 3, 3)
  assert not is_valid_knight_move(0, 0, -2, -1)

def test_valid_rook_move():
  assert is_valid_rook_move(0, 0, 1, 0)
  assert is_valid_rook_move(0, 0, 0, 1)
  assert not is_valid_rook_move(0, 0, 1, 1)
  assert not is_valid_rook_move(0, 0, 0, 0)
  assert not is_valid_rook_move(0, 0, 8, 0)

def test_valid_bishop_move():
  assert is_valid_bishop_move(0, 0, 1, 1)
  assert is_valid_bishop_move(0, 0, 7, 7)
  assert is_valid_bishop_move(4, 3, 6, 5)
  assert not is_valid_bishop_move(4, 3, 6, 7)
  assert not is_valid_bishop_move(0, 0, 0, 0)
  assert not is_valid_bishop_move(0, 0, 8, 8)
  assert not is_valid_bishop_move(0, 0, -1, -1)

def test_valid_queen_move():
  assert is_valid_queen_move(0, 0, 1, 1)
  assert is_valid_queen_move(0, 0, 0, 1)
  assert is_valid_queen_move(0, 0, 1, 0)
  assert not is_valid_queen_move(0, 0, 1, 2)
  assert not is_valid_queen_move(0, 0, 0, 0)
  assert not is_valid_queen_move(0, 0, -1, 2)
  assert not is_valid_queen_move(0, 0, 1, 8)

def test_valid_king_move():
  assert is_valid_king_move(0, 0, 1, 1)
  assert is_valid_king_move(0, 0, 0, 1)
  assert is_valid_king_move(0, 0, 1, 0)
  assert not is_valid_king_move(0, 0, 2, 0)
  assert not is_valid_king_move(0, 0, 0, 2)
  assert not is_valid_king_move(0, 0, 0, 0)
  assert not is_valid_king_move(0, 0, 3, 4)
  assert not is_valid_king_move(0, 0, -1, 0)
  assert not is_valid_king_move(0, 0, 0, -1)
  # Castling
  assert is_valid_king_move(4, 0, 6, 0)
  assert is_valid_king_move(4, 0, 2, 0)
  assert is_valid_king_move(4, 7, 2, 7)
  assert is_valid_king_move(4, 7, 6, 7)
  assert not is_valid_king_move(3, 7, 5, 7)
  assert not is_valid_king_move(4, 6, 6, 6)

def test_value_pawn_move():
  assert is_valid_pawn_move(1, 1, 1, 2, True)
  assert is_valid_pawn_move(1, 1, 0, 2, True)
  assert is_valid_pawn_move(1, 1, 2, 2, True)
  assert is_valid_pawn_move(1, 1, 1, 3, True)
  assert is_valid_pawn_move(1, 1, 1, 3, PieceColor.WHITE)
  assert not is_valid_pawn_move(1, 1, 1, 3, PieceColor.BLACK)
  assert not is_valid_pawn_move(1, 1, 1, 4, True)
  assert not is_valid_pawn_move(1, 2, 1, 4, True)

  assert is_valid_pawn_move(1, 6, 1, 5, False)
  assert is_valid_pawn_move(1, 6, 0, 5, False)
  assert is_valid_pawn_move(1, 6, 2, 5, False)
  assert is_valid_pawn_move(1, 6, 1, 4, False)
  assert is_valid_pawn_move(1, 6, 1, 4, PieceColor.BLACK)
  assert not is_valid_pawn_move(1, 6, 1, 4, PieceColor.WHITE)
  assert not is_valid_pawn_move(1, 6, 1, 3, False)
  assert not is_valid_pawn_move(1, 5, 1, 3, False)

  assert not is_valid_pawn_move(0, 1, 0, 1, True)
  assert not is_valid_pawn_move(0, 6, 0, 6, False)
  assert not is_valid_pawn_move(0, 7, 0, 8, True)
  assert not is_valid_pawn_move(0, 6, 0, 7, False)

