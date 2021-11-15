board=[" "]*10
#print(board)
def display(board):

        print(board[7] +"|"+board[8]+"|"+board[9])
        print(board[0]+"|"+board[0]+"|"+board[0])
        print(board[4] +"|"+board[5]+"|"+board[6])
        print(board[0]+"|"+board[0]+"|"+board[0])
        print(board[1] +"|"+board[2]+"|"+board[3])
        print(board[0]+"|"+board[0]+"|"+board[0])
        return board
def XorO():
        player1="w"
        player2=""
        while player1 not in ["X","O"]:
                player1=input("Player1: What do you want to choose X or O ").upper()
                if player1 not in ["X","O"]:
                        print("Wrong Input")

        if player1=="X":
                player2="O"
        else:
                player2="X"        
        return (player1,player2)

def choosethegaps():
        while True:
                
                pos=input("Enter your choice between 1-9 ")
                if pos in["1","2","3","4","5","6","7","8","9"] and space_check(board,int(pos)) :
                        break
                else:
                        print("Wrong choice already filled ")
                        
        return int(pos)
       
from random import randint
def choose():
        a=randint(0,1)
        if a==1:
                return "Player1"
        else :
                return "Player2"
        
def fillthegaps(board,player1,position):
        board[position]=player1
        return board
        
def win_check(board,mark):
       return ((board[7] == mark and board[8] == mark and board[9] == mark) or # top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or #side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
def space_check(board,pos):
       return board[pos]==" "
def fullboard():
        for i in range(1,10):
                if space_check(board,i)== True:
                        
                        return False
        return True
def cont():
        while True:
                a=input('Do you want to play again? Enter Yes or No: ').upper()
                if a in ["YES","NO"]:
                        break
                else:
                        print("wrong choice")
        if a=="YES":
                return True
        else :
                return False
        
print("Welcome to tic tac toe ")
print("Choose the corresponding number to fill your choice")
print("7" +"|"+"8"+"|"+"9")
print(board[0]+"|"+board[0]+"|"+board[0])
print("4" +"|"+"5"+"|"+"6")
print(board[0]+"|"+board[0]+"|"+board[0])
print("1" +"|"+"2"+"|"+"3")
print(board[0]+"|"+board[0]+"|"+board[0])
gameon=True       
while gameon:
        display(board)
        #print("\n"*100)
        player1,player2=XorO()
        # count=0
        turn=choose()
        print(turn+" will go first")
        while True:
                if turn=="Player1":
                        #print("Player 1")
                        position=choosethegaps()
                        board=fillthegaps(board,player1,position)
                        display(board)
                        if win_check(board,player1) == True:
                                print("Player1 has won the game")
                                break
                        else:
                                if fullboard()==True:
                                        
                                        print("The game has tied")
                                        break
                                else:
                                        turn="Player2"
                #print("Player 2")
                else:
                        position=choosethegaps()
                        board=fillthegaps(board,player2,position)
                        display(board)
                        if win_check(board,player2) == True:
                                print("Player2 has won the game")
                                break
                        else:
                                if fullboard()==True:
                                        
                                        print("The game has tied")
                                        break
                                else:
                                        turn="Player1"
        if cont()==False:
               
                break
                
        board=[" "]*10        
                
        
        
