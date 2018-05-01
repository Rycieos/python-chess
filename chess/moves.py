
cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
valid_spaces = range(8)

def space_on_board(x, y):
  return x in valid_spaces and y in valid_spaces

def convert_from_chess_space(space):
  if len(space) != 2:
    raise ValueError("input string '{}' not chess space".format(space))
  x = cols.index(space[0])
  y = int(space[1]) - 1
  if not space_on_board(x, y):
    raise ValueError("coords ({}, {}) not on board".format(x, y))
  return (x, y)

def convert_to_chess_space(x, y):
  if not space_on_board(x, y):
    raise ValueError("coords ({}, {}) not on board".format(x, y))
  return "{}{}".format(cols[x], y + 1)

def valid_knight_moves(x, y):
  all_moves = {
      (x + 2, y + 1), (x + 2, y - 1),
      (x - 2, y + 1), (x - 2, y - 1),
      (x + 1, y + 2), (x - 1, y + 2),
      (x + 1, y - 2), (x - 1, y - 2)}

  valid_moves = set()
  for _x, _y in all_moves:
    if space_on_board(_x, _y):
      valid_moves.add((_x, _y))

  return valid_moves

def is_valid_knight_move(start_x, start_y, end_x, end_y):
  if not space_on_board(end_x, end_y):
    return False
  return (end_x, end_y) in valid_knight_moves(start_x, start_y)

def is_valid_rook_move(start_x, start_y, end_x, end_y):
  if not space_on_board(end_x, end_y):
    return False
  return (start_x != end_x) ^ (start_y != end_y)

def is_valid_bishop_move(start_x, start_y, end_x, end_y):
  if not space_on_board(end_x, end_y):
    return False
  dx = abs(start_x - end_x)
  dy = abs(start_y - end_y)
  return dx == dy and dx + dy != 0

def is_valid_queen_move(start_x, start_y, end_x, end_y):
  return (is_valid_rook_move(start_x, start_y, end_x, end_y)
      or is_valid_bishop_move(start_x, start_y, end_x, end_y))

def is_valid_king_move(start_x, start_y, end_x, end_y):
  if not space_on_board(end_x, end_y):
    return False
  dx = abs(start_x - end_x)
  dy = abs(start_y - end_y)
  return dx <= 1 and dy <= 1 and dx + dy != 0

def is_valid_pawn_move(start_x, start_y, end_x, end_y, white):
  if not space_on_board(end_x, end_y):
    return False
  dx = start_x - end_x
  dy = start_y - end_y

  if white:
    return (dy == -1 and -1 <= dx <= 1) or (start_y <= 1 and dy == -2 and dx == 0)
  else:
    return (dy == 1 and -1 <= dx <= 1) or (start_y >= 6 and dy == 2 and dx == 0)

