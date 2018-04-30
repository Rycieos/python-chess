#!/usr/bin/env pytest

import pytest

from chess.moves import *

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
  assert not is_valid_queen_move(0, 0, -1, 2)
  assert not is_valid_queen_move(0, 0, 1, 8)

def test_valid_king_move():
  assert is_valid_king_move(0, 0, 1, 1)
  assert is_valid_king_move(0, 0, 0, 1)
  assert is_valid_king_move(0, 0, 1, 0)
  assert not is_valid_king_move(0, 0, 2, 0)
  assert not is_valid_king_move(0, 0, 0, 2)
  assert not is_valid_king_move(0, 0, 3, 4)
  assert not is_valid_king_move(0, 0, -1, 0)
  assert not is_valid_king_move(0, 0, 0, -1)

def test_value_pawn_move():
  assert is_valid_pawn_move(1, 1, 1, 2, True)
  assert is_valid_pawn_move(1, 1, 0, 2, True)
  assert is_valid_pawn_move(1, 1, 2, 2, True)
  assert is_valid_pawn_move(1, 1, 1, 3, True)
  assert not is_valid_pawn_move(1, 1, 1, 4, True)
  assert not is_valid_pawn_move(1, 2, 1, 4, True)

  assert is_valid_pawn_move(1, 6, 1, 5, False)
  assert is_valid_pawn_move(1, 6, 0, 5, False)
  assert is_valid_pawn_move(1, 6, 2, 5, False)
  assert is_valid_pawn_move(1, 6, 1, 4, False)
  assert not is_valid_pawn_move(1, 6, 1, 3, False)
  assert not is_valid_pawn_move(1, 5, 1, 3, False)

  assert not is_valid_pawn_move(0, 1, 0, 1, True)
  assert not is_valid_pawn_move(0, 6, 0, 6, False)
  assert not is_valid_pawn_move(0, 7, 0, 8, True)
  assert not is_valid_pawn_move(0, 6, 0, 7, False)

