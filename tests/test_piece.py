#!/usr/bin/env py.test

import pytest

from chess.piece import *

def test_is_white():
  assert Piece.W_KING.is_white()
  assert Piece.W_KING.is_white()
  assert Piece.W_QUEEN.is_white()
  assert Piece.W_ROOK.is_white()
  assert Piece.W_BISHOP.is_white()
  assert Piece.W_KNIGHT.is_white()
  assert Piece.W_PAWN.is_white()
  assert not Piece.B_KING.is_white()
  assert not Piece.B_QUEEN.is_white()
  assert not Piece.B_ROOK.is_white()
  assert not Piece.B_BISHOP.is_white()
  assert not Piece.B_KNIGHT.is_white()
  assert not Piece.B_PAWN.is_white()

def test_values():
  assert Piece.W_KING.value == 'K'
  assert Piece.W_KING.symbol == '♔'
  assert Piece.W_KING.type is PieceType.KING
  assert Piece.W_KING.color is PieceColor.WHITE

def test_creation():
  assert Piece('K') is Piece.W_KING
  assert Piece('♔') is Piece.W_KING
  with pytest.raises(ValueError):
    Piece(PieceType.KING)
  with pytest.raises(ValueError):
    Piece(PieceColor.WHITE)

