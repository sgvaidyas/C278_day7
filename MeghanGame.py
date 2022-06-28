l = [0 for i in range(9)]

def display():
    for i in range(len(l)):
        if(i%3==0):
            print()
        print(l[i],end="\t")
    print()

win_l = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]


#main
display()
moves=1
won = False
while moves<=9 and not won:
    if moves%2==1:
        valid_move = False
        print("PLAYER 1 ITS  UR TURN!!!")
        while not valid_move:
            cell = int(input("Enter a number between 0 and 8 to select a cell: "))
            if cell not in range(9):
                cell = print("Invalid move.")
            elif l[cell] != 0:
                cell = print("Cell already filled- please choose another.")
            else:
                l[cell] = 1
                valid_move = True
    else:
        valid_move = False
        print("PLAYER 2 ITS  UR TURN!!!")
        while not valid_move:
            cell = int(input("Enter a number between 0 and 8 to select a cell: "))
            if cell not in range(9):
                cell = print("Invalid move.")
            elif l[cell] != 0:
                cell = print("Cell already filled- please choose another.")
            else:
                l[cell] = 2
                valid_move = True
    moves += 1
    display()
    if moves >= 5:
        player1_moves = {cell for cell, player in enumerate(l) if player == 1}
        player2_moves = {cell for cell, player in enumerate(l) if player == 2}
        print("player1_moves = ",player1_moves)
        print("player2_moves = ",player2_moves)
        for win_move in win_l:
            if player1_moves.issuperset(win_move):
                print("Player 1 wins!")
                won = True
            if player2_moves.issuperset(win_move):
                print("Player 2 wins!")
                won = True
