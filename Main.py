from Board import Board
import pygame
import Render
pygame.init()
    
print("hello")
board = Board()
board.player1.printHand()
board.player2.printHand()
board.player3.printHand()
board.player4.printHand()


running = True
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    #Replace the array of Nones with board.pile!!
    Render.draw(board.player1.hand, [None, None, None, None])
pygame.quit()