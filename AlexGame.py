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
    pass
moves=1
while moves<=9:
    if moves%2==1:
        player = "player1"
        print("PLAYER 1 ITS  UR TURN!!!\nCurrent Game:")
        turn(player, l)
    else:
        player = "player2"
        print("PLAYER 2 ITS  UR TURN!!!")
        turn(player, l)
    moves += 1
