
theboard = {'1':' ','2':' ','3':' ',
            '4':' ','5':' ','6':' ',
            '7':' ','8':' ','9':' '
            }

boardkeys = []

for key in theboard:
    boardkeys.append(key)

def PrintBoard(board):
    print(board['1']+'|'+board['2']+'|'+board['3'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['7']+'|'+board['8']+'|'+board['9'])
    
# PrintBoard(theboard)

def game():
    turn = 'X'
    count = 0
    
    for i in range(10):
        PrintBoard(theboard)
        print("It is the turn of "+turn+" Specify the place you want to go")

        move = input()

        if(theboard[move]==' '):
            theboard[move] = turn
            count +=1
        else:
            print("Sorry this cell location is filled. Please choose another position")
            continue
        if(count>=5):
            if(theboard['7']==theboard['8']==theboard['9']!=' '):
                PrintBoard(theboard)
                print("\nGame Over\n")
                print("Player "+turn+" won the game")
                break
            if(theboard['4']==theboard['5']==theboard['6']!=' '):
                PrintBoard(theboard)
                print("\nGame Over\n")
                print("Player "+turn+" won the game")
                break
            if(theboard['1']==theboard['2']==theboard['3']!=' '):
                PrintBoard(theboard)
                print("\nGame Over\n")
                print("Player "+turn+" won the game")
                break
            if(theboard['1']==theboard['4']==theboard['7']!=' '):
                PrintBoard(theboard)
                print("\nGame Over\n")
                print("Player "+turn+" won the game")
                break
            if(theboard['2']==theboard['5']==theboard['8']!=' '):
                PrintBoard(theboard)
                print("\nGame Over\n")
                print("Player "+turn+" won the game")
                break
            if(theboard['3']==theboard['6']==theboard['9']!=' '):
                PrintBoard(theboard)
                print("\nGame Over\n")
                print("Player "+turn+" won the game")
                break
            if(theboard['1']==theboard['5']==theboard['9']!=' '):
                PrintBoard(theboard)
                print("\nGame Over\n")
                print("Player "+turn+" won the game")
                break
            if(theboard['3']==theboard['5']==theboard['7']!=' '):
                PrintBoard(theboard)
                print("\nGame Over\n")
                print("Player "+turn+" won the game")
                break

        if(count==9):
            print("\nGame Over\n")
            print("The game is Tie!")

        if turn == "X":
            turn ="O"
        else:
            turn = "X"
        
    restart = input("Do you want to restart the game?(y/n) ")

    if(restart =='y'):
        for key in boardkeys:
            theboard[key]=' '
        game()

if __name__ == "__main__":
    game()
            