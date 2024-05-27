from Bet import BetFactory
import pygame
import Render
from Bet import Bet
from BetSuit import BetSuit
from Board import Board
def main() -> None:
    pygame.init()
    board = Board()
    run = True
    while run:
     for event in pygame.event.get():
          if board.getState == "MENU":
               Render.draw_menu_screen(board)
          if board.getState == "BETTING":
               board.reset_values()
               board.startBetting()
               board.startPlayerGame()
          if board.getState == "QUIT" or event.type == pygame.QUIT:
               run = False
               board.getState = "QUIT"
          #pygame.display.flip()
    pygame.display.quit()
    pygame.quit()
if __name__ == '__main__':
   main()
'''
board.startGame()

betFactory = BetFactory()
print(betFactory.asIDs())
print(betFactory)

board = Board()
board.player1.printHand()
board.player2.printHand()
board.player3.printHand()
board.player4.printHand()
'''
"""
board.player1.sortHand()
board.player1.update_card_positions()
running = True
active_bet = Bet(BetSuit.LOW, 0)

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board.getState == "PLAYING":
                  for card in board.player1.hand:
                       card_rect = pygame.Rect(card.x, Render.HAND_Y, Render.CARD_WIDTH *2 / 3, Render.CARD_HEIGHT)
                       if card_rect.collidepoint(event.pos):
                            print("Clicked on " + str(card))
                            board.player1.playCard(card, board)
                            break
                elif board.getState == "BETTING":
                     #logic for handling player betting
                     #Player clicks on a button corresponding to some bet
                     #Then that bet is added using board.addBet
                     #addBet checks for validity
                     for button in Render.size_bet_rects:
                          if button.rect.collidepoint(event.pos):
                               new_bet = Bet(active_bet.suit, button.value)
                               active_bet = new_bet
                               print(active_bet)
                     for button in Render.suit_bet_rects:
                          if button.rect.collidepoint(event.pos):
                               new_bet = Bet(button.betsuit, active_bet.level)
                               active_bet = new_bet
                               print(active_bet)
                     if Render.submit_rect.collidepoint(event.pos):
                          success = board.addBet(active_bet)
                          if success:
                               print("Yippee")
                          else:
                               print("womp womp")
                     if Render.pass_rect.collidepoint(event.pos):
                          print("Passed")
                          board.addBet(Bet(None, None))
                            
    Render.draw(board)
pygame.quit()
"""
