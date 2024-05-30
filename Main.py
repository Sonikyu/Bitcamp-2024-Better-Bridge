from Bet import BetFactory
import pygame, Render
from Bet import Bet
from BetSuit import BetSuit
from Board import Board

def main() -> None:
    pygame.init()
    Render.set_music_vol(Render.DEFAULT_MUSIC_VOLUME)
    Render.set_music(0) 
    board = Board()

    board.check_profile_name()
    while board.getState != "QUIT":
     for event in pygame.event.get():
          if board.getState == "MENU":
               Render.draw_menu_screen(board)
               print("Exited menu")
          if board.getState == "QUIT" or event.type == pygame.QUIT:
               board.getState = "QUIT"
          if ((board.gameMode == "SINGLE" or board.gameMode == "MULTI") and board.getState != "QUIT"):
               board.reset_values()
               board.startBetting()
          if board.getState == "PLAYING": 
               board.startPlayerGame()
               print("Try AGAIN?")
               print(f"{board.getState}")
    pygame.display.quit()
    pygame.quit()
    print("You quit")
if __name__ == '__main__':
   main()


# board.startGame()

# betFactory = BetFactory()
# print(betFactory.asIDs())
# print(betFactory)

# board = Board()
# board.player1.printHand()
# board.player2.printHand()
# board.player3.printHand()
# board.player4.printHand()



# pygame.init()
# print("GAME STARTED")
# board = Board()
# board.check_profile_name()
# board.gameMode = "SINGLE"
# board.reset_values()
# board.player1.sortHand()
# board.player1.update_card_positions()
# board.startBetting()

# running = True
# betFactory = BetFactory()
# if board.currentBetID == -1:
#      active_bet = Bet(BetSuit.LOW, 0)
# else:
#      active_bet = betFactory.getBet(board.currentBetID)
# print(active_bet)
# while running:
#     for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if board.getState == "PLAYING":
#                   for card in board.player1.hand:
#                        card_rect = pygame.Rect(card.x, Render.HAND_Y, Render.CARD_WIDTH *2 / 3, Render.CARD_HEIGHT)
#                        if card_rect.collidepoint(event.pos):
#                             print("Clicked on " + str(card))
#                             board.player1.playCard(card, board)
#                             break
#                 elif board.getState == "BETTING":
#                      #logic for handling player betting
#                      #Player clicks on a button corresponding to some bet
#                      #Then that bet is added using board.addBet
#                      #addBet checks for validity
#                      for button in Render.size_bet_rects:
#                           if button.rect.collidepoint(event.pos):
#                                print()
#                                new_bet = Bet(active_bet.suit, button.value)
#                                active_bet = new_bet
#                                print(active_bet)
#                      for button in Render.suit_bet_rects:
#                           if button.rect.collidepoint(event.pos):
#                                new_bet = Bet(button.betsuit, active_bet.level)
#                                active_bet = new_bet
#                                print(active_bet)
#                      if Render.submit_rect.collidepoint(event.pos):
#                           success = board.addBet(active_bet)
#                           if success:
#                                print("Yippee")
#                           else:
#                                print("womp womp")
#                      if Render.pass_rect.collidepoint(event.pos):
#                           print("Passed")
#                           board.addBet(Bet(None, None))
                            
#     Render.draw_gameplay(board)
# pygame.quit()


