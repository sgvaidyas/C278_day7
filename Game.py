grid = [0 for i in range(9)]

def display():
    for i in range(len(grid)):
        if(i%3==0):
            print()
        print(grid[i],end="\t")
    print()

def getMove(symbol):
  while True:
    slot = int(input("Select a grid square [1-9]: "))



    if slot<1 or slot>9:
      print("Invalid positions! Try Lenscart!")
      continue
    elif  grid[slot-1] != 0 :
      print("That square is already filled.")
      continue
    slot-=1
    grid[slot] = symbol
    break

def checkMove(symbol):
    if ((grid[0] == grid[1] == grid[2]==symbol) or
        (grid[3] == symbol and grid[4] == symbol and grid[5]==symbol) or
        (grid[6] == symbol and grid[7] == symbol and grid[8]==symbol) or
        (grid[0] == symbol and grid[3] == symbol and grid[6]==symbol) or
        (grid[1] == symbol and grid[4] == symbol and grid[7]==symbol) or
        (grid[2] == symbol and grid[5] == symbol and grid[8]==symbol) or
        (grid[0] == symbol and grid[4] == symbol and grid[8]==symbol) or
        (grid[2] == symbol and grid[4] == symbol and grid[6]==symbol)):
        return symbol
    return -1



#main
display()
moves=1
symbols={"player1": "X", "player2": "P"}
while moves<=9:
    player=""
    if moves%2==1:
        print("PLAYER 1 ITS  UR TURN!!!")
        getMove(symbols["player1"])
        player=symbols["player1"]
    else:
        print("PLAYER 2 ITS  UR TURN!!!")
        getMove(symbols["player2"])
        player=symbols["player2"]
    display()
    if moves>=5:
        res = checkMove(player)
        if res=="X":
            print("PLAYER 1 WON THE GAME")
            break
        elif res=="P":
            print("PLAYER 2 WON THE GAME")
            break
    moves += 1
else:
    print("MATCH DRAW !!!")
