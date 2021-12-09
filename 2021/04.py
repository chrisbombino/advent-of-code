from utils import *


class Board:
    def __init__(self, board) -> None:
        self.board = board
        self.size = 5
        self.score = 0
    
    def __repr__(self) -> str:
        return str(self.board)
    
    def mark(self, val):
        for i, row in enumerate(self.board):
            for j, num in enumerate(row):
                if val == num:
                    self.board[i][j] = True

    def win(self):
        marked = 0

        for row in self.board:
            for val in row:
                if val == True:
                    marked += 1
            if marked == self.size:
                self.sum()
                return True
                
            marked = 0

        for col in range(self.size):
            for row in range(self.size):
                val = self.board[row][col]
                if val == True:
                    marked += 1
                if marked == self.size:
                    self.sum()
                    return True
            
            marked = 0
    
    def sum(self):
        sum = 0
        for row in self.board:
            for val in row:
                if isinstance(val, str):
                    sum += int(val)
        self.score = sum


# part 1
data = read_aoc_data(4).splitlines()

drawn_numbers = data[0].split(",")
boards = []
board = []

for line in data[2:]:
    row = line.split()
     
    if not row: # end of current board
        boards.append(Board(board))
        board = []
        continue
    
    board.append(row)

def part1():
    for num in drawn_numbers:
        for board in boards:
            board.mark(num)
            
            if board.win():
                print(f"Part 1: {board.score * int(num)}")
                return


part1()

# part 2
boards = []
board = []
total_wins = 0
winners = []

for line in data[2:]:
    row = line.split()
     
    if not row: # end of current board
        boards.append(Board(board))
        winners.append(False)
        board = []
        continue
    
    board.append(row)

for num in drawn_numbers:
    for idx, board in enumerate(boards):
        board.mark(num)

        if board.win() and not winners[idx]:
            total_wins += 1
            winners[idx] = True
            if total_wins == len(boards):
                print(f"Part 2: {board.score * int(num)}")