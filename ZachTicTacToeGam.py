grid = ["□" for i in range(9)]

def display():
    for i in range(9):
        if(i%3==0):
            print()
        print(grid[i],end="\t")
    print()

def getMove(symbol):
  while True:
    slot = int(input("Select a grid square [0-9]: "))

    if grid[slot] != "□":
      print("That square is already filled.")
      continue

    grid[slot] = symbol
    break

#main
display()
moves=0
symbols={"player1": "X", "player2": "O"}
while moves<9:
    if moves%2:
        print("PLAYER 2 ITS  UR TURN!!!")
        getMove(symbols["player2"])
    else:
        print("PLAYER 1 ITS  UR TURN!!!")
        getMove(symbols["player1"])

    display()
    moves += 1
