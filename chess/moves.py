
def valid_knight_moves(x, y):
  all_moves = [
      (x + 2, y + 1), (x + 2, y - 1),
      (x - 2, y + 1), (x - 2, y - 1),
      (x + 1, y + 2), (x - 1, y + 2),
      (x + 1, y - 2), (x - 1, y - 2)]

  valid_moves = []
  for _x, _y in all_moves:
    if _x < 8 and _x >= 0 and _y < 8 and _y >= 0:
      valid_moves.append((_x, _y))

  return valid_moves

def is_valid_knight_move(start_x, start_y, end_x, end_y):
  return (end_x, end_y) in valid_knight_moves(start_x, start_y)

