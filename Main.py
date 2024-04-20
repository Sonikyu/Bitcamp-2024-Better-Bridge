from Board import Board
from Bet import BetFactory
import pygame
import Render
pygame.init()


# betFactory = BetFactory()
# print(betFactory.asIDs())
# print(betFactory)
    
print("hello")
board = Board()
board.player1.printHand()
board.player2.printHand()
board.player3.printHand()
board.player4.printHand()

board.player1.update_card_positions()
running = True
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                 for card in board.player1.hand:
                      card_rect = pygame.Rect(card.x, Render.HAND_Y, Render.CARD_WIDTH *2 / 3, Render.CARD_HEIGHT)
                      if card_rect.collidepoint(event.pos):
                           print("Clicked on " + str(card))
                           board.player1.playCard(card)
                           break
    Render.draw(board)
pygame.quit()