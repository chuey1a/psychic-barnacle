#connect 4

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
          print(str(self.board[i][j]) + " | ", end = "")
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
      self.board[row][col] = "x"
      self.col_counter[col] -= 1
    if player_num == 2:
      self.board[self.col_counter[col]][col] = "o"
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
            if self.board[i][j-1] == "x":
              row_count1 += 1
            else:
              row_count2 += 1
        elif row_count1 == 4 or row_count2 == 4:
          if row_count1 == 4:
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
            if self.board[j-1][i] == "x":
              column_count1 += 1
            else:
              column_count2 += 1
        elif column_count1 == 4 or column_count2 == 4:
          if column_count1 == 4:
            return 1
          else:
            return 2
      column_count1 = 1
      column_count2 = 1

    #check diagonals for winning combo
    #left to right:
    diag = []
    for j in range(7):
      diag.append([row[i+j] for i,row in enumerate(self.board) if 0 <= i+j < len(row)])

    for i in range(6):
      for j in range(1,7):
        if row_count1 < 4 and row_count2 < 4:
          if self.board[i][j-1] == self.board[i][j] and self.board[i][j] != 0:
            if self.board[i][j-1] == "x":
              row_count1 += 1
            else:
              row_count2 += 1
        elif row_count1 == 4 or row_count2 == 4:
          if row_count1 == 4:
            return 1
          else:
            return 2
      row_count1 = 1
      row_count2 = 1

    print(diag)

    return 0

#Welcome message
print("\n   Welcome to Connect FOR!!\n")

four_board = Board()
four_board.print_board()

game = 0
player_num = 1

while game != 1:
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
    break

  #Check to see if board is full
  full = four_board.board_full()
  if full == True:
    break

  print()

if full == False:
  print("Player {} wins!!!\n".format(winner))
else:
  print("Board is full and Player 1 and Player 2 TIE\n")