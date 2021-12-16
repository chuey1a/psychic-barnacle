#connect 4

def print_board(board):
  print("  0   1   2   3   4   5   6  ")
  print("-----------------------------")
  for i in range(6):
    print("| ", end = "")
    for j in range(7):
      if board[j][i] == 0:
        print(" " + " | ", end = "")
      else:
        print(str(board[j][i]) + " | ", end = "")

    print()
    print("-----------------------------")
  print()

def input_player1(col):
  if col > 7:
    return 0


board = []

rows, cols = (7, 6)
board = [[0]*cols]*rows

print_board(board)
