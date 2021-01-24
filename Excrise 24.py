def horiz_line():
    print(" ---" * board_size)

def vert_line():
    print("|   " * (board_size + 1))

if __name__ == "__main__":
    board_size = int(input("What size of game board? "))

    for i in range(board_size):
      horiz_line()
      vert_line()
    horiz_line()