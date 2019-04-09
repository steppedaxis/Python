def print_board(board): # THIS FUNCTION SIMPLY PRINTS THE BOARD
    index=0
    for x in board:
        print('|',end=" ")
        print(x,end=" ")
        print('|',end=" ")
        index+=1
        if index%3==0: # GO DOWN A ROW IF THE NUMBER DIVIDES WITH NO REMINDER WITH THE BOARD SIZE(IN THIS CASE 3)
            print(' ')

def player_input(input,index,board): # THIS FUNCTION RECIEVES THE BOARD,THE PLAYER INPUT(BOARD INDEX) AND MARK(X OR O) AND THEN REPLACES THE MATCHING NUMBER ON THE BOARD WITH X OR O
    for x in board:
       if input=='X':
          if x==index:
             board[x-1]='X'
       elif input=='O':
           if x==index:
             board[x-1]='O'
    print_board(board) # PRINT THE BOARD AFTER THE PLAYER CHOOSES THE INDEX HE WANTS TO CHANGE

def check_winner(playermarker,board,status): # THIS FUNCTION CHECKS THE WINNING CONDITIONS, IT TAKES THE PLAYER MARKER(X OR O),THE BOARD AND THE STATUS, AND RETURN THE STATUS AS TRUE IF ONE OF THE CODITIONS IS MET
    # THIS BLOCK CHECKS THE ROWS 
    if board[0]==board[1]==board[2]==playermarker:
            status=True
    if board[3]==board[4]==board[5]==playermarker:
            status=True
    if board[6]==board[7]==board[8]==playermarker:
            status=True
    
    # THIS BLOCK CHECKS THE COLUMNS
    if board[0]==board[3]==board[6]==playermarker:
        status=True
    if board[1]==board[4]==board[7]==playermarker:
        status=True
    if board[2]==board[5]==board[8]==playermarker:
        status=True

    # THIS BLOCK CHECKS THE DIAGONALS
    if board[0]==board[4]==board[8]==playermarker:
        status=True
    if board[6]==board[4]==board[2]==playermarker:
        status=True
    return status # IF ONE OF THE CONDITIONS IS MET, RETURN THE STATUS AS TRUE(MEANING SOMEONE WON)

board=[1,2,3,4,5,6,7,8,9]
draw_index=0 #THIS COUNTER COUNTS THE AVILABLE INDEXES ON THE BOARD, IF BY ANY CHANCE IT GETS TO 9 AND NO ONE HAS WON, THEN WE KNOW THAT THERE IS A TIE
print_board(board)
player1='X'
player2='O'
gamestatus=False # THE GAME STATUS IS FALSE AT FIRST, MEANING NO ONE HAS WON YET, THE FUNCTION check_winner WILL CHANGE IT TO TRUE IF SOMEONE HAVE WON THE GAME
new_game='' #THIS IS A STRING THAT RECIEVES THE PLAYER INPUT ABOUT PLAYING A NEW GAME

while(gamestatus==False):
     #---------------PLAYER 1 INPUT AND TURN--------------------#
    #take inputs from player 1
    player1input=int(input('player 1! please enter an index number of board\n'))
    while player1input>9 or player1input<0: # CHECK FOR VALID INPUT OF P1
        print('wrong input, try again!')
        player1input=int(input())
    player_input(player1,player1input,board)
    draw_index+=1 # INCREMENT DRAW INDEX BY 1 TILL IT GETS TO 9, THEN WE KNOW WE HAVE A DRAW SINCE THE BOARD IS FULL
    gamestatus_player1=check_winner(player1,board,gamestatus) # CHECK IF PLAYER 1 WINS
    if gamestatus_player1==True:
        print('player 1 wins!')
        print('would you like to play again? enter YES for a new game or NO to exit') # ASK THE PLAYERS IF THE WANT ANOTHER GO
        new_game=input()
        if new_game=='YES' or new_game=='yes': # IF THEY WRITE YES OR yes THEN I PRESENT THE INITIAL BOARD AGAIN,ZERO THE DRAW INDEX AND CONTINUE THE WHILE LOOP 
         board=[1,2,3,4,5,6,7,8,9]
         print_board(board)
         draw_index=0
         continue
        elif new_game=='NO' or new_game=='no': # IF THEY WRITE NO OR no THEN THE LOOP IS BROKEN AND THE GAME IS OVER 
            break
    if draw_index==9:  # CHECK THE DRAW INDEX, IF IT GETS TO 9 THEN WE HAVE A TIE
          print('its a draw!')
          print('would you like to play again? enter YES for a new game or NO to exit')
          new_game=input()
          if new_game=='YES' or new_game=='yes':
              board=[1,2,3,4,5,6,7,8,9]
              print_board(board)
              draw_index=0
              continue
          elif new_game=='NO' or new_game=='no':
            break
        
    #----------------PLAYER 2 INPUT AND TURN ------------------------#
    #take input from player 2
    player2input=int(input('player 2! please enter an index number of board\n'))
    while player2input>9 or player2input<0: # CHECK FOR VALID INPUT OF P1
        print('wrong input, try again!')
        player2input=int(input())
    player_input(player2,player2input,board)
    draw_index+=1  # INCREMENT DRAW INDEX BY 1 TILL IT GETS TO 9, THEN WE KNOW WE HAVE A DRAW SINCE THE BOARD IS FULL
    gamestatus_player2=check_winner(player2,board,gamestatus) # CHECK IF PLAYER 1 WINS
    if gamestatus_player2==True:
        print('player 2 wins!')
        print('would you like to play again? enter YES for a new game or NO to exit') # ASK THE PLAYERS IF THE WANT ANOTHER GO
        new_game=input()
        if new_game=='YES' or new_game=='yes': # IF THEY WRITE YES OR yes THEN I PRESENT THE INITIAL BOARD AGAIN,ZERO THE DRAW INDEX AND CONTINUE THE WHILE LOOP 
            print('\n'*100)
            board=[1,2,3,4,5,6,7,8,9]
            print_board(board)
            draw_index=0
            continue
        elif new_game=='NO' or new_game=='no': # IF THEY WRITE NO OR no THEN THE LOOP IS BROKEN AND THE GAME IS OVER 
            break
    if draw_index==9:  # CHECK THE DRAW INDEX, IF IT GETS TO 9 THEN WE HAVE A TIE
          print('its a draw!')
          print('would you like to play again? enter YES for a new game or NO to exit')
          new_game=input()
          if new_game=='YES' or new_game=='yes':
              print('\n'*100)
              board=[1,2,3,4,5,6,7,8,9]
              print_board(board)
              draw_index=0
              continue
          elif new_game=='NO' or new_game=='no':
            break
          
      
   

   
    
  
 



    
    



