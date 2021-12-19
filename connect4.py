#connect 4
import numpy as np

class Board():
  rows, cols = (6, 7)
  col_counter = [5]*cols
  board = data = [[0]*7 for _ in range(6)]

  def print_board(self):
    print("\n  0   1   2   3   4   5   6  ")
    print("-----------------------------")
    for i in range(6):
      print("| ", end = "")
      for j in range(7):
        if self.board[i][j] == 0:
          print(" " + " | ", end = "")
        else:
          if self.board[i][j] == 1:
            print("x | ", end = "")
          else:
            print("o | ", end = "")

      print("\n-----------------------------")
    print()

  def board_full(self):
    if sum(x.count("o") for x in self.board) == 21:
      return True
    return False

  def add_input(self, col, player_num):
    complete = 0
    if player_num == 1:
      row = self.col_counter[col]
      self.board[row][col] = 1
      self.col_counter[col] -= 1
    if player_num == 2:
      self.board[self.col_counter[col]][col] = 2
      self.col_counter[col] -= 1

  def player_input(self, player_num):
    print("Player {} enter input: ".format(player_num), end="")
    complete = 0
    while complete != 1:
      col = int(input())
      if self.col_counter[col] < 0:
        print("Error! Column already full!")
      elif self.col_counter.count(-1) == self.rows:
        break
      else:
        self.add_input(col, player_num)
        complete = 1

  def check_winner(self):
    row_count1 = 1
    row_count2 = 1
    column_count1 = 1
    column_count2 = 1
    diag_count1 = 1
    diag_count2 = 1

    #check rows for winning combo
    for i in range(6):
      for j in range(1,7):
        if row_count1 < 4 and row_count2 < 4:
          if self.board[i][j-1] == self.board[i][j] and self.board[i][j] != 0:
            if self.board[i][j-1] == 1:
              row_count1 += 1
            else:
              row_count2 += 1
        elif row_count1 >= 4 or row_count2 >= 4:
          if row_count1 >= 4:
            return 1
          else:
            return 2
      row_count1 = 1
      row_count2 = 1

    #check columns for winning combo
    for i in range(7):
      for j in range(1,6):
        if column_count1 < 4 and column_count2 < 4:
          if self.board[j-1][i] == self.board[j][i] and self.board[j][i] != 0:
            if self.board[j-1][i] == 1:
              column_count1 += 1
            else:
              column_count2 += 1
        elif column_count1 >= 4 or column_count2 >= 4:
          if column_count1 >= 4:
            return 1
          else:
            return 2
      column_count1 = 1
      column_count2 = 1

    #check diagonals for winning combo
    a = np.array(self.board)

    diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
    diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))
    diag_list = [n.tolist() for n in diags]

    for diag in diag_list:
      for i in range(1, len(diag)):
        if diag[i-1] == diag[i] and diag[i] != 0:
          if diag[i] == 1:
            diag_count1 += 1
          else:
            diag_count1 += 1
        if diag_count1 == 4:
          return 1
        elif diag_count2 == 4:
          return 2
      diag_count1 = 1
      diag_count2 = 1

    #return 0

#Welcome message
print("\n   Welcome to Connect FOR!!\n")

four_board = Board()
four_board.print_board()

player_num = 1

while True:
  #Player 1 turn
  four_board.player_input(player_num)
  four_board.print_board()
  player_num += 1

  winner = four_board.check_winner()
  if winner == 1 or winner == 2:
    break

  #Player 2 turn
  four_board.player_input(player_num)
  four_board.print_board()
  player_num = 1

  #Check to see if there is a winner
  winner = four_board.check_winner()
  if winner == 1 or winner == 2:
    print("f")
    break

  #Check to see if board is full
  full = four_board.board_full()
  if full == True:
    print("g")
    break

  print()

if full == False:
  print("Player {} wins!!!\n".format(winner))
else:
  print("Board is full and Player 1 and Player 2 TIE\n")