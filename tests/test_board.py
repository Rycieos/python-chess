#!/usr/bin/env py.test

import pytest

from chess.board import *

def test_new_board():
  board = Board()
  assert board.whites_turn
  assert board.white_king_castle
  assert board.white_queen_castle
  assert board.black_king_castle
  assert board.black_queen_castle
  assert board.en_passant_space is None
  assert board.fifty_move_rule_moves == 0
  assert board.full_move_count == 1

def test_fromfen():
  board = Board.fromfen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b Kkq e3 0 4')
  assert not board.whites_turn
  assert board.white_king_castle
  assert not board.white_queen_castle
  assert board.black_king_castle
  assert board.black_queen_castle
  assert board.en_passant_space == (4, 2)
  assert board.fifty_move_rule_moves == 0
  assert board.full_move_count == 4

def test_fen_in_out():
  fen = 'rnb3nr/pppp1ppp/8/4p3/8/8/PPPPPPPP/RNBQKBNR b Kq e3 4 16'
  board = Board.fromfen(fen)
  assert fen == board.get_fen()

  fen = 'rnb5/pppp1ppp/8/4p3/8/8/PPP3PP/RNBQKBNR w - - 0 1'
  board = Board.fromfen(fen)
  assert fen == board.get_fen()

