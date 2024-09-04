# Video alternative: https://vimeo.com/954334009/67af9910fc#t=1054

# So far you've spent a lot of time writing new programs.

# This is great for learning the fundamentals of code, but
# actually isn't very realistic. Most software engineers
# spend their time modifying and maintaining existing
# programs, not writing entirely new ones.

# Below is the same program as in the example. Your
# challenge is to implement some improvements:

# 1. Right now users can place their tiles over the other
#    user's tiles. Prevent this.

# 2. Right now if the game reaches a draw with no more free
#    spaces, the game doesn't end. Make it end at that
#    point.

# 3. If you want a real challenge, try to rework this
#    program to support a 5x5 board rather than a 3x3 board.

# 4. If you're still not satisfied, try to rework this
#    program to take a parameter `board_size` and play a
#    game with a board of that size.

# This is getting really challenging now — and is entirely
# optional. Don't forget about your assessment!
def generate_groups_to_check(board_size):
  groups = []
  for row in range(0, board_size):
    row_group = []
    col_group = []
    for col in range(0, board_size):
      row_group.append((row, col))
      col_group.append((col, row))
    groups.append(row_group)
    groups.append(col_group)
  diag_fwd = []
  diag_bwd = []
  for i in range(0, board_size):
    diag_fwd.append((i, i))
    diag_bwd.append((i, board_size -i - 1))
  groups.append(diag_fwd)
  groups.append(diag_bwd)
  return groups
def play_game(board_size):
  board = make_blank_board(board_size)
  player = "X"
  while not is_game_over(board, board_size):
    print(print_board(board))
    print("It's " + player + "'s turn.")
    # `input` asks the user to type in a string
    # We then need to convert it to a number using `int`
    row = int(input("Enter a row: "))
    column = int(input("Enter a column: "))
    if not is_move_valid(board, row, column):
      print ("Invalid move!")
      continue
    board = make_move(board, row, column, player)
    if player == "X":
       player = "O"
    else:
      player = "X"
  print(print_board(board))
  print("Game over!")

def make_blank_board(board_size):
  grid = []
  for row in range(0, board_size):
    row = ["."] * board_size
    grid.append(row)
  return grid  
      
def is_move_valid(board, row, column):
  return board[row][column] == "."
  
def print_board(board):
  formatted_rows = []
  for row in board:
    formatted_rows.append(" ".join(row))
  grid = "\n".join(formatted_rows)
  return grid

def make_move(board, row, column, player):
  board[row][column] = player
  return board

def get_cells_by_list(board, coords):
  cells = []
  for coord in coords:
    cells.append(board[coord[0]][coord[1]])
  return cells

# This function will check if the group is fully placed
# with player marks, no empty spaces.
def is_group_complete(board, coords):
  cells = get_cells_by_list(board, coords)
  return "." not in cells

# This function will check if the group is all the same
# player mark: X X X or O O O
def are_all_cells_the_same(board, coords):
  cells = get_cells_by_list(board, coords)
  return cells[0] == cells[1] and cells[1] == cells[2]

# We'll make a list of groups to check:
def is_game_over(board, board_size):
  groups_to_check = generate_groups_to_check(board_size)
  if is_game_draw(board):
    return True
  # We go through our groups
  for group in groups_to_check:
    # If any of them are empty, they're clearly not a
    # winning row, so we skip them.
    if is_group_complete(board, group):
      if are_all_cells_the_same(board, group):
        return True # We found a winning row!
        # Note that return also stops the function
  return False # If we get here, we didn't find a winning row
def is_game_draw(board):
  for row in board:
    if "." in row:
      return False
  return True  
# And test it out:

print("Game time!")
play_game(4)
