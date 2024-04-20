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
            if event.type == pygame.MOUSEBUTTONDOWN:
                 loc_offset = 0
                 for card in board.player1.hand:
                      card_x = ((Render.SCREEN_WIDTH - ((len(board.player1.hand) + 1) * (Render.CARD_WIDTH * 2 / 3))) / 2) + loc_offset*Render.CARD_WIDTH * 2/3
                      card_rect = pygame.Rect(card_x, Render.HAND_Y, Render.CARD_WIDTH *2 / 3, Render.CARD_HEIGHT)
                      if card_rect.collidepoint(event.pos):
                           print("Clicked on " + str(card))
                           board.player1.playCard(card)
                           break
                      loc_offset += 1
    #Replace the array of Nones with board.pile!!
    Render.draw(board.player1.hand, board.currentTrick)
pygame.quit()