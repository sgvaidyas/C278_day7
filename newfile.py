l = [0 for i in range(9)]

def display(list):
    for i in range(len(list)):
        if(i%3==0):
            print()
        print(list[i],end="\t")

#main
# display()
def turn(player, list):

    display(l)
    if player == "player1":
        playerMark = "X"
    else:
        playerMark="O"

    move = int(input("Which element do you want to pick?\n0\t1\t2\n3\t4\t5\n6\t7\t8"))
    if l[move] == 0:
        l[move] = playerMark
    else:
        print("Pick another spot")
        turn(player,list)

def checkWin(list):
    X = "X"
    O = "O"
    if list[0] == list[1] and list[1] == list[2]:
        if list[0] == X:
            print("Player1 wins")
            return False
        elif list[0] == O:
            print("Player2 wins")
            return False
    if list[3] == list[4] and list[4] == list[5]:
        if list[3] == X:
            print("Player1 wins")
            return False
        elif list[3] == O:
            print("Player2 wins")
            return False
    if list[6] == list[7] and list[7] == list[8]:
        if list[6] == X:
            print("Player1 wins")
            return False
        elif list[6] == O:
            print("Player2 wins")
            return False
    if list[0] == list[3] and list[3] == list[6]:
        if list[0] == X:
            print("Player1 wins")
            return False
        elif list[0] == O:
            print("Player2 wins")
            return False
    if list[1] == list[4] and list[4] == list[7]:
        if list[1] == X:
            print("Player1 wins")
            return False
        elif list[1] == O:
            print("Player2 wins")
            return False
    if list[2] == list[5] and list[5] == list[8]:
        if list[2] == X:
            print("Player1 wins")
            return False
        elif list[2] == O:
            print("Player2 wins")
            return False
    if list[0] == list[4] and list[4] == list[8]:
        if list[0] == X:
            print("Player1 wins")
            return False
        elif list[0] == O:
            print("Player2 wins")
            return False
    if list[2] == list[4] and list[4] == list[6]:
        if list[2] == X:
            print("Player1 wins")
            return False
        elif list[2] == O:
            print("Player2 wins")
            return False
    return True

moves=1
noWinner = True
while moves<=9 and noWinner==True:
    if moves%2==1:
        player = "player1"
        print("PLAYER 1 ITS  UR TURN!!!\nCurrent Game:")
        turn(player, l)
        if moves>=5:
            noWinner = checkWin(l)
    else:
        player = "player2"
        print("PLAYER 2 ITS  UR TURN!!!")
        turn(player, l)
        if moves>=5:
            noWinner = checkWin(l)
    moves += 1
else:
    print("Match Draw")
