#!/usr/bin/env pytest

import pytest

from chess.moves import *

def test_all_valid_knight():
  assert valid_knight_moves(0, 0) == [(2, 1), (1, 2)]

def test_valid_knight():
  assert is_valid_knight_move(3, 3, 2, 5)
  assert not is_valid_knight_move(3, 3, 2, 4)

