
def space_on_board(x, y):
  spaces = range(8)
  return x in spaces and y in spaces

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

