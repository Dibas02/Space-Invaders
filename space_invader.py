import pygame
import math
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLIDING_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background_image = pygame.image.load('Space Invader Img.jpg')

icon = pygame.image.load('UFO Img.png')
pygame.display.set_caption("Space Invaders")

pygame.display.set_icon(icon)


player_x= = PLAYER_START_X
player_y = PLAYER_START_Y+
player_x_change = 0
enemy_Img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_of_enemy = 6
for i in range(number_of_enemy):
    enemy_Img.append(pygame.image.load('Alien2.png')
    enemy_x.append(random.randint(0, SCREEN_WIDTH - 64))
    enemy_y.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemy_x.append(ENEMY_SPEED_X)
    enemy_y.append(ENEMY_SPEED_Y)


bullet_Img = pygame.image.load('Bullet2.png')
bullet_x = 0
bullet_y = PLAYER_START_Y
bullet_x_change = 0
bullet_y_change = BULLET_SPEED_Y
bullet_state = 'ready'



score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10                     
text_y = 10
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True(255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over.font.render("GAME OVER")