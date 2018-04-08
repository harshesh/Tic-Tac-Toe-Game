#STEP 1
#Fun that print out borad.set up board as list.where each index 1-9 corresponds with a number on a number pad.
#so you get a 3 by 3 representation

from IPython.display import clear_output
def display_board(board):
    
    clear_output()
    print('   |   | ')
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   | ')

#STEP 2
#write a function that can take in a player input and assign their marker as 'X' and 'O' .
#Think about using while loops continually ask until you get a correct answer

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker=input('Player:1 Do you want to be x or o? ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#STEP 3
#write a function that takes , in the list object ,a marker ('X','O') and a desired position (number 1-9) and 
#assign it to board.

def place_maker(board, marker, position):
    board[position] = marker

#STEP 4
#write a function that takes in a board and a mark (X or O) and then check to see if that mark won .

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or #top row
            (board[4] == mark and board[5] == mark and board[6] == mark) or #second row
            (board[1] == mark and board[2] == mark and board[3] == mark) or #third row
            (board[1] == mark and board[4] == mark and board[7] == mark) or #first column
            (board[2] == mark and board[5] == mark and board[8] == mark) or #second column
            (board[3] == mark and board[6] == mark and board[9] == mark) or #third column
            (board[7] == mark and board[5] == mark and board[3] == mark) or #first diagonal
            (board[1] == mark and board[5] == mark and board[9] == mark))

#STEP 5
#write a function that uses the random module to randomly decide which player goes first . you may want to lookup 
#random.randint() return a string of which player went first

import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'player 1'
    else:
        return 'player 2'

#STEP 6
#write a function that return boolean indicating whether a space on board is freely available.

def space_check(board, position):
    return board[position] == ' '

#STEP 7
#write a function that checks if the board is full and return a boolean value true if full false otherwise

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#STEP 8
#write a function that ask player's next position (as a number 1-9) and then uses the function from step 6 to check if its free 
#position .If it is then return the position for later use.

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
        position = input("choose your next position 1-9")
    return int(position)

#STEP 9
#write a function that asks the player if they want to play again and return a boolean true if they want to play otherwise False

def replay():
    return input('Do you want to play again ? enter yes or no ').lower().startswith('y')

#STEP 10
#use while loops and functions you've made  to run the game

print('Welcome to Tic Tec Toe Game')
while True:
    theBoard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first!')
    
    game_on = True
    
    while game_on:
        
        if turn == 'player 1':
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_maker(theBoard,player1_marker,position)
            
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('congratulations, player 1, has won the game')
                game_on = False
                 
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("the game is  draw")
                    break
                     
                else:
                    turn = 'player 2'
        else:
            #player 2 turn 
            display_board(theBoard)
            position = player_choice(theBoard)
            place_maker(theBoard,player2_marker,position)
            
            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('congratulations, player 2, has won the game')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("the game is  draw")
                else:
                    turn = 'player 1'
    if not replay():
        break
