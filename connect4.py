#MARK: - IMPORTS
from lib2to3 import pygram
from re import S
from xmlrpc.client import Boolean
import pygame
import numpy as np
import sys

#-----------------------------------------------------------------------------------------------------------------------------------------

#MARK: - CONSTANTS
ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (51,153,255)
BLACK = (0,0,0)
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

    #Diagonal Check (-)

    for r in range (3,ROW_COUNT):
        for c in range (3,COLUMN_COUNT-3):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2] == piece and board [r-3][c+3]== piece:
                return True

pygame.init()
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
            pygame.draw.circle(screen,BLACK,(c*SQUARESIZE+SQUARESIZE/2, r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2),RADIUS)
            

#------------------------------------------------------------------------------------------------------------------------------------------------

#MARK:- RUN
def run():
    board = create_board()
    game_over = False
    turn = 0
    draw_board(board)
    pygame.display.update()


    print(board)
    

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                pass
                # #Turno jugador 1
                # if turn == 0:
                #     col = int(input('Jugador 1 indique su jugada: '))
                #     if is_valid_location(board,col):
                #         row = get_next_open_row(board,col)
                #         drop_piece(board,row,col,1)
                #         if(winning_move(board,1)):
                #             print("jUGADOR 1 GANO")
                #             game_over = True

                #     print_board(board)
                #     turn +=1


                # #Turno jugador 2
                # else:
                #     col = int(input('Jugador 2 indique su jugada: '))

                #     if is_valid_location(board,col):
                #         row = get_next_open_row(board,col)
                #         drop_piece(board,row,col,2)
                #         if(winning_move(board,2)):
                #             print("jUGADOR 2 GANO")
                #             game_over = True
            
                #     print_board(board)
                #     turn +=1
                #     turn = turn %2
        
            

#-----------------------------------------------------------------------------------------------------------------------------------------


#MARK: ENTRY POINT
if __name__ == '__main__':
    run()