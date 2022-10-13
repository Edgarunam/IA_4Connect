#MARK: - IMPORTS
from xmlrpc.client import Boolean
import pygame
import numpy as np
import math
import sys
import random
import time
#-----------------------------------------------------------------------------------------------------------------------------------------

#MARK: - CONSTANTS
ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (51,153,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
RED = (255,0,0)

PLAYER:int =0
AI:int = 1
EMPTY:int = 0
PLAYER_PIECE:int = 1
AI_PIECE:int = 2
WINDOW_LENGTH:int = 4
#------------------------------------------------------------------------------------------------------------------------------------------

#MARK: FUNCITIONS
def Welcome():
    print('El clásico juego conecta 4')
    print('-'*30)

def drop_piece(board:np.matrix,row:int,col:int,piece:int):
    board[row][col] = piece

def is_valid_location(board:np.matrix,col:int) -> Boolean:
    return board[ROW_COUNT-1][col] == 0 #Return True if de Column is available

def get_next_open_row(board:np.matrix,col:int) -> int:
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board:np.matrix):
    flip_matrix = np.flip(board,0)
    print(flip_matrix)


def create_board():
    tablero= np.zeros((ROW_COUNT,COLUMN_COUNT))
    return tablero
    

def winning_move(board,piece):
    #Horizontal checl
    for c in range (COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1]==piece and board[r][c+2]== piece and board[r][c+3]== piece:
                return True

    #Vertical Check

    for r in range (ROW_COUNT-3):
        for c in range (COLUMN_COUNT):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c] == piece and board [r+3][c]== piece:
                return True

    #Diagonal Check (+)

    for r in range (ROW_COUNT-3):
        for c in range (COLUMN_COUNT-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2] == piece and board [r+3][c+3]== piece:
                return True

    #Diagonal Check (-) #Horizontal checl
    for c in range (COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1]==piece and board[r][c+2]== piece and board[r][c+3]== piece:
                return True

    #Vertical Check

    for r in range (ROW_COUNT-3):
        for c in range (COLUMN_COUNT):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c] == piece and board [r+3][c]== piece:
                return True

    #Diagonal Check (+)

    for r in range (ROW_COUNT-3):
        for c in range (COLUMN_COUNT-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2] == piece and board [r+3][c+3]== piece:
                return True

    #Diagonal Check (-)

    for r in range (3,ROW_COUNT):
        for c in range (3,COLUMN_COUNT-3):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2] == piece and board [r-3][c+3]== piece:
                return True

    for r in range (3,ROW_COUNT):
        for c in range (3,COLUMN_COUNT-3):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2] == piece and board [r-3][c+3]== piece:
                return True


###HEURISTC FUNCTION###

def score_position(board,piece):
    score = 0
    #Horizontal Score
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(COLUMN_COUNT-3):
            window = row_array[c:c+WINDOW_LENGTH]
            if window.count(piece) == 4:
                score += 100
            elif window.count(piece) == 3 and window.count(EMPTY)==1:
                score += 10
                                           
            
    return score
def get_valid_locations(board):
    valid_locations = []
    for c in range(COLUMN_COUNT-1):
        if is_valid_location(board,c):
            valid_locations.append(c)
    return valid_locations


def pick_best_move(board,piece):
    valid_locations = get_valid_locations(board)
    best_score = 0
    best_col = random.choice(valid_locations)
    
    #ITERATION FOR LOOKING THE BEST COL 
    for col in valid_locations:
        row = get_next_open_row(board,col)
        temp_board = board.copy()
        drop_piece(temp_board,row,col,piece)
        score = score_position(temp_board,piece)
        if score > best_score:
            best_score = score
            best_col = col
    return best_col


        




pygame.init()
myfont = pygame.font.SysFont("monospace",75)
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width,height)
RADIUS = int(SQUARESIZE/2 -5)
screen = pygame.display.set_mode(size)

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,BLUE,(c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen,BLACK,(int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen,RED,(int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)),RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen,YELLOW,(int(c*SQUARESIZE+SQUARESIZE/2),height-int(r*SQUARESIZE+SQUARESIZE/2)),RADIUS)
    pygame.display.update()
            

#------------------------------------------------------------------------------------------------------------------------------------------------

#MARK:- RUN
def run():
    SQUARESIZE = 100
    width = COLUMN_COUNT * SQUARESIZE
    board = create_board()
    game_over = False
    turn = random.randint(PLAYER,AI)
    draw_board(board)
    pygame.display.update()


    print(board)
    

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen,BLACK,(0,0, width,SQUARESIZE))
                posX= event.pos[0]

                if turn == 0:
                    pygame.draw.circle(screen,RED,(posX,int(SQUARESIZE/2)),RADIUS)
                    pygame.display.update()
                else:
                    pygame.draw.circle(screen,YELLOW,(posX,int(SQUARESIZE/2)),RADIUS)
                    pygame.display.update()


            if event.type == pygame.MOUSEBUTTONDOWN:
                
                #Turno jugador 1
                if turn == PLAYER:
                    posX = event.pos[0]

                    col = int(math.floor(posX/SQUARESIZE))
                    if is_valid_location(board,col):
                        row = get_next_open_row(board,col)
                        drop_piece(board,row,col,PLAYER_PIECE)
                        

                        if(winning_move(board,PLAYER_PIECE)):
                            pygame.draw.rect(screen,BLACK,(0,0, width,SQUARESIZE))
                            label = myfont.render("YOU WIN",1,RED)
                            screen.blit(label,(40,10))
                            game_over = True
                    print("*"*8)
                    print_board(board)
                    draw_board(board)                  
                    turn +=1
                    if game_over:
                        pygame.time.wait(3000)


                        


                #Turno jugador 2
        if turn ==AI and not game_over:

                    
            #col = random.randint(0,COLUMN_COUNT-1)
            col = pick_best_move(board,AI_PIECE)
            time.sleep(0.2)

            if is_valid_location(board,col):
                row = get_next_open_row(board,col)
                drop_piece(board,row,col,AI_PIECE)
                        
                if(winning_move(board,AI_PIECE)):
                    pygame.draw.rect(screen,BLACK,(0,0, width,SQUARESIZE))
                    label = myfont.render("IA WON",1,YELLOW)
                    screen.blit(label,(40,10))
                    game_over = True
                            
                            
            
            print_board(board)
            draw_board(board)
            turn +=1
            turn = turn %2
            if game_over:
                pygame.time.wait(3000)
                

                    
        
            

#-----------------------------------------------------------------------------------------------------------------------------------------


#MARK: ENTRY POINT
if __name__ == '__main__':
    run()