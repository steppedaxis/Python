def board_print(board): #function to print the board
    index=0
    for x in board:
        print('|{}|'.format(x),end=" ")
        index+=1
        if index%3==0: #each time a number divides in 3, go down a row
            print(' ')
def place_marker(marker,num,board): #function to place a player marker on the board
    for x in board:
        if marker.upper()=='X': 
            if num==x:
              board[x]='X'
              break
        elif marker.upper()=='O': 
            if num==x:
               board[x]='O'
               break
def X_or_O(): #function to set markers for player 1 and 2
    global player1 #taking the global player1 var 
    global player2 ##taking the global player2 var 
    player1=input('player 1 , X or O?: ')
    while True:
        if player1.upper()=='X':
            player2='O'
            break
        elif player1.upper()=='O':
            player2='X'
            break
        print("wrong selection, please choose only X or O") #i've set this code segment in a while loop to handle a case where player 1 inputs a number or anything that is not X or O 
        player1=input('player 1 , X or O?: ') 
def win_check(board,marker,game_status): #function to check winning condition
    # THIS BLOCK CHECKS THE ROWS 
    if board[0]==board[1]==board[2]==marker:
           game_status=True
    if board[3]==board[4]==board[5]==marker:
            game_status=True
    if board[6]==board[7]==board[8]==marker:
            game_status=True
    # THIS BLOCK CHECKS THE COLUMNS
    if board[0]==board[3]==board[6]==marker:
        game_status=True
    if board[1]==board[4]==board[7]==marker:
        game_status=True
    if board[2]==board[5]==board[8]==marker:
        game_status=True
    # THIS BLOCK CHECKS THE DIAGONALS
    if board[0]==board[4]==board[8]==marker:
       game_status=True
    if board[6]==board[4]==board[2]==marker:
       game_status=True
    
    return game_status # IF ONE OF THE CONDITIONS IS MET, RETURN THE STATUS AS TRUE(MEANING SOMEONE WON)
def new_game(): #function to set a new game if one of the winners enters `yes`
    print("want another go? enter yes or no")
    answer=input()
    if answer.lower()=='yes':
        global board  #take the board var from the global segment of the code
        global tie_marker #take the board var from the global segment of the code
        board=[0,1,2,3,4,5,6,7,8] #initialize board var
        tie_marker=0 #initialize tie marker var
        return 0
    elif answer.lower()=='no':
        print("Goodbye!")
        return 1
def check_index_existing_marker(board,marker,num): #this function checks if a given index is already taken, and if it is, then prompts the user for a new input
    while True:
        if board[num]=='X' or board[num]=='O': #check if the given index number has X or O
            new_marker=int(input("index taken,enter a new index number: ")) #ask the player for a new index number
            if board[new_marker]=='X' or board[new_marker]=='O': #check if the given new index number has X or O
                continue
            else: #else call the  place_marker function to put the given marker(X or O) in the given index
                place_marker(marker,new_marker,board)
                break
        else: # if the given index number does not contain an X or 0 then exit the while loop
            break


board=[0,1,2,3,4,5,6,7,8]
player1=''
player2=''
X_or_O()
gamestatus=False
tie_marker=0 #this variable handels the tie case in the game, if it gets to 9, then we know that every player had his turn already and the board is full
while(gamestatus==False):
    board_print(board)
    #----------PLAYER 1 TURN---------------#
    num_player1=int(input('player 1, please enter a board index: ')) #take player 1's index input
    check_index_existing_marker(board,player1,num_player1) #checks if a given index is already taken, and if it is, then prompts the user for a new input
    place_marker(player1,num_player1,board) #function to place a player marker on the board
    tie_marker+=1  #each time a player has inputed his desired index, the tie marker var will be incremented by 1, indicating that a place on the board has been taken
    board_print(board) #print the board after player selection
    gamestatus_player1=win_check(board,player1.upper(),gamestatus) #check winnig conditions after player input
    if gamestatus_player1==True: #if gamestatus_player1 var returns as true, it means that player 1 has won
        print('player 1 wins!')
        if new_game()==0: #checks if new_game var returns as 0, and if it does, start a new game, as board and tie_marker vars are reinitalized ,else the game exits
            continue
        else:
            break
    if tie_marker==9: #if tie_marker has made it to 9, it means that every player has filled an index in the board(meaning its now full)
        print('its a draw!')
        if new_game()==0:
            continue
        else:
            break
    
    #----------PLAYER 2 TURN---------------#
    num_player2=int(input('player 2, please enter a board index: ')) #take player 2's index input
    check_index_existing_marker(board,player2,num_player2)  #checks if a given index is already taken, and if it is, then prompts the user for a new input
    place_marker(player2,num_player2,board) #function to place a player marker on the board
    tie_marker+=1 #each time a player has inputed his desired index, the tie marker var will be incremented by 1, indicating that a place on the board has been taken
    gamestatus_player2=win_check(board,player2.upper(),gamestatus) #check winnig conditions after player input
    if gamestatus_player2==True: #if gamestatus_player1 var returns as true, it means that player 2 has won
        board_print(board)
        print('player 2 wins!')
        if new_game()==0: #checks if new_game var returns as 0, and if it does, start a new game, as board and tie_marker vars are reinitalized ,else the game exits
            continue
        else:
            break
    if tie_marker==9: #if tie_marker has made it to 9, it means that every player has filled an index in the board(meaning its now full)
        print('its a draw!')
        if new_game()==0:
            continue
        else:
            break
       
    









