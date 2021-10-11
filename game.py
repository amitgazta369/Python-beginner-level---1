import random  # for genrandom num for gen pipes in gme
import sys  # we will us sys.exit to exit the program
import pygame
from pygame.locals import *  # basic py game imports

# global var for the game

FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = ' D:\PROGRAMMING TUT\flappy bird game\gallery\sprites\kisspng-flappy-bird-tap-bird-2d-flying-bird-5ace9dc0275663.8987914515234902401611'
BACKGROUND = 'D:\PROGRAMMING TUT\flappy bird game\gallery\sprites\bg.png'
PIPE = 'D:\PROGRAMMING TUT\flappy bird game\gallery\spritespngkey.com-flappy-bird-pipe-png-1831473'

if __name__ == "__main__":
    # this will main point where game will start
    pygame.init()  # initilaize py gme modules
    FPSCLOCK = pygame.time.clock()
    pygame.display.set_caption('FLAPPY BIRD BY AMIT GAZTA')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('D:\PROGRAMMING TUT\flappy bird game\gallery\sprites\0-Number-PNG').convert_alpha(),
        pygame.image.load('D:\PROGRAMMING TUT\flappy bird game\gallery\sprites\1-Number-PNG').convert_alpha(),
        pygame.image.load('D:\PROGRAMMING TUT\flappy bird game\gallery\sprites\2-Number-PNG').convert_alpha(),
        pygame.image.load('D:\PROGRAMMING TUT\flappy bird game\gallery\sprites\3-Number-PNG').convert_alpha(),
        pygame.image.load('D:\PROGRAMMING TUT\flappy bird game\gallery\sprites\4-Number-PNG').convert_alpha(),
        pygame.image.load('D:\PROGRAMMING TUT\flappy bird game\gallery\sprites\5-Number-PNG').convert_alpha(),
        pygame.image.load('D:\PROGRAMMING TUT\flappy bird game\gallery\sprites\6-Number-PNG').convert_alpha(),
        pygame.image.load('D:\PROGRAMMING TUT\flappy bird game\gallery\sprites\7-Number-PNG').convert_alpha(),
        pygame.image.load('D:\PROGRAMMING TUT\flappy bird game\gallery\sprites\8-Number-PNG').convert_alpha(),
        pygame.image.load('D:\PROGRAMMING TUT\flappy bird game\gallery\sprites\9-Number-PNG').convert_alpha(),
    )
    GAME_SPRITES['player'] = pygame.image.load(
        'D:\PROGRAMMING TUT\flappy bird game\gallery\sprites\kisspng-flappy-bird-tap-bird-2d-flying-bird-5ace9dc0275663.8987914515234902401611').convert_alpha(),
    GAME_SPRITES['background'] = pygame.image.load(
        'D:\PROGRAMMING TUT\flappy bird game\gallery\sprites\bg.png').convert_alpha(),
    GAME_SPRITES['message'] = pygame.image.load(
        'D:\PROGRAMMING TUT\flappy bird game\gallery\sprites\gtredy').convert_alpha(),
    GAME_SPRITES['base'] = pygame.image.load(
        'D:\PROGRAMMING TUT\flappy bird game\gallery\sprites\base').convert_alpha(),
    GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                            pygame.image.load(PIPE).convert_alpha(),
                            )

    # game sounds
    GAME_SOUNDS['die'] = pygame.mixer.sound('D:\PROGRAMMING TUT\flappy bird game\gallery\audio\sfx_die')
    GAME_SOUNDS['hit'] = pygame.mixer.sound('D:\PROGRAMMING TUT\flappy bird game\gallery\audio\sfx_hit')
    GAME_SOUNDS['point'] = pygame.mixer.sound('D:\PROGRAMMING TUT\flappy bird game\gallery\audio\sfx_point')
    GAME_SOUNDS['swoosh'] = pygame.mixer.sound('D:\PROGRAMMING TUT\flappy bird game\gallery\audio\sfx_swooshing')
    GAME_SOUNDS['wing'] = pygame.mixer.sound('D:\PROGRAMMING TUT\flappy bird game\gallery\audio\sfx_wing')

    while true:
        welcomeScreen()  # shows the welcome screen to user until he presses a button
        maingame()  # this is the main game function












