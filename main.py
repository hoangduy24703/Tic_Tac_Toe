import pygame
import os
import numpy as np

pygame.init()
#GENERAL DEFINATIONS
SIDE = 600
LINE_WIDTH = 15
CIRCLE_RADIUS = SIDE/10
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
SCREEN = pygame.display.set_mode((SIDE,SIDE))
pygame.display.set_caption('TIC TAC TOE')

#COLOR
FRAME_COLOR = (23, 145, 135) # LIGHT GREY
BACKGROUND_COLOR = (28, 170, 156) # CORAL_BLUE
CROSS_COLOR = (219, 201, 193) # SKIN
CIRCLE_COLOR = (61, 61, 61) # DARK GREY

#BOARD
board = np.zeros((3, 3))
def draw_window():
    SCREEN.fill(BACKGROUND_COLOR)

    pygame.draw.line(SCREEN, FRAME_COLOR, (0,200), (600, 200), LINE_WIDTH)
    pygame.draw.line(SCREEN, FRAME_COLOR, (0,400), (600, 400), LINE_WIDTH)
    pygame.draw.line(SCREEN, FRAME_COLOR, (200,0), (200, 600), LINE_WIDTH)
    pygame.draw.line(SCREEN, FRAME_COLOR, (400,0), (400, 600), LINE_WIDTH)

def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pygame.draw.line(SCREEN, CROSS_COLOR, (col * (SIDE//3) + SPACE, row * (SIDE//3) + (SIDE//3) - SPACE), (col * (SIDE//3) + (SIDE//3) - SPACE, row * (SIDE//3) + SPACE), CROSS_WIDTH )
                pygame.draw.line(SCREEN, CROSS_COLOR, (col * (SIDE//3) + SPACE, row * (SIDE//3) + SPACE), (col * (SIDE//3) + (SIDE//3) - SPACE, row * (SIDE//3) + (SIDE//3) - SPACE), CROSS_WIDTH )
            elif board[row][col] == 2:
                pygame.draw.circle(SCREEN, CIRCLE_COLOR, (col * (SIDE//3) + (SIDE//3)//2, row * (SIDE//3) + (SIDE//3)//2), CIRCLE_RADIUS, CIRCLE_WIDTH )

def marked_square(row, col, player):
    board[row][col] = player

def free_square(row, col): 
    return board[row][col] == 0

def is_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True

def is_winning(player):
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
        
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
        
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal_winning_line(player)
        return True
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal_winning_line(player)
        return True
    
    return False
def draw_vertical_winning_line(col, player):
    posX = col * (SIDE//3) + 100
    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR
    
    pygame.draw.line(SCREEN, color, (posX, 15), (posX, SIDE -15), 15)

def draw_horizontal_winning_line(row, player):
    posY = row * (SIDE//3) + 100
    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR
    
    pygame.draw.line(SCREEN, color, (15, posY), (SIDE - 15, posY), 15)
def draw_asc_diagonal_winning_line(player):
    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR
    
    pygame.draw.line(SCREEN, color, (15, SIDE - 15), (SIDE - 15, 15), 15)
def draw_desc_diagonal_winning_line(player):
    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR
    
    pygame.draw.line(SCREEN, color, (15, 15), (SIDE - 15, SIDE -15), 15)
def restart():
    draw_window()
    player = 1
    for row in range(3):
        for col in range(3):
            board[row][col] = 0

draw_window()

def main():
    player = 1
    game_over = False
    IS_RUNNING = True
    while IS_RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                IS_RUNNING = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = int(mouseY//200)
                clicked_col = int(mouseX//200)

                if free_square(clicked_row, clicked_col):
                    if player == 1:
                        marked_square(clicked_row, clicked_col, player)
                        if is_winning(player):
                            game_over = True
                        player = 2
                    elif player == 2:
                        marked_square(clicked_row, clicked_col, player)
                        if is_winning(player):
                            game_over = True
                        player = 1
                    print(board)
                    draw_figures()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    restart()
        pygame.display.update()

if __name__ == '__main__':
    main()
