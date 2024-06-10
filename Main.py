#from Bet import BetFactory
import pygame, Render
# from Bet import Bet
# from BetSuit import BetSuit
from Board import Board
from Game import Game

def main() -> None:
    """Main function to initialize the game, handle events, and manage the game loop."""
    pygame.init()  # Initialize the Pygame library

    # Set initial audio settings
    Render.set_music_vol(Render.DEFAULT_MUSIC_VOLUME)
    Render.set_music(0)  

    board = Board()  # Create the main game board objectss

    board.check_profile_name()  # Validate or set up the player's profile

    # Main Game Loop
    while board.getState != "QUIT":  
        # Event Handling
        for event in pygame.event.get():  # Get all events from Pygame's event queue
            if event.type == pygame.QUIT:  # Check for a quit event (window close, etc.)
                board.getState = "QUIT"  # Set the game state to quit

            # State-Based Logic (within the event loop)
            if board.getState == "MENU":
                Render.draw_menu_screen(board)  # Draw the menu screen
                print("Exited menu")  # Debugging output - could be removed later

            if (board.gameMode in ["SINGLE", "MULTI"] and board.getState != "QUIT"):
                board.reset_values()  
                board.startBetting()  

            if board.getState == "PLAYING":
                board.startPlayerGame()  
                print("Try AGAIN?")  # Debugging output - could be removed later
                print(f"{board.getState}")  # Debugging output - could be removed later
        Render.clock.tick(Render.FRAMES_PER_SECOND)
    # Clean Up (after the game loop)
    pygame.display.quit()  # Uninitialize the display module
    pygame.quit()  # Uninitialize Pygame completely
    print("You quit")
if __name__ == '__main__':
    game = Game()
    game.game_loop()
   #main()

