import pygame
from State import Menu
import Render, os
from Board import Board

class Game:
    def __init__(self):
        #todo move pygame initializations to appropriate locations
        pygame.display.init()
        pygame.mixer.init()
        pygame.font.init()
        #Screen Related Variables
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1200, 750
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        #Game Related Variables
        self.current_state: GameState = None
        self.is_running = True
        self.is_playing = True
        #Game States
        self.all_states = {
            "MENU" : Menu(self), 
            }

        self.clock = pygame.time.Clock()
        self.FRAME_PER_SECOND = 60

        self.board: Board = Board()
        self.actions = {
            "down" : False,
            "up" : False, 
            "left" : False,
            "right" : False,
            "enter" : False,
            }
        self.keys = {
            "down" : pygame.K_s,
            "up" : pygame.K_w, 
            "left" : pygame.K_a,
            "right" : pygame.K_d,
            "enter" : pygame.K_RETURN
            }
        self.state_stack = []
        #User Settings to be checked
        self.user_name: str = None
        self.sound_volume: float = None
        self.music_volume: float = None
        #Checks information
        self.load_states()
        #self.check_user_information()    
    #todo make it so information is held like Setting volume
    #todo put this method into state
    def check_user_information(self) -> str:
        self.USER_FILE = 'User_Info/name.txt'
        name = ''
        try:
            if os.stat(self.USER_FILE).st_size == 0:
                os.remove(self.USER_FILE)
            with open(self.USER_FILE) as file:
                name = file.read()
        except FileNotFoundError:
            with open(self.USER_FILE, 'w') as file:
                self.current_state = GameState.PICK_A_NAME
                pygame.display.set_caption(self.current_state)
                name = Render.draw_get_name()
                file.write(name)
        self.user_name = name
    
    
    # def betting_loop(self):
        
    #     Render.create_moving_cards(self)
    #     #todo create board variable user player for whatever index the user picked
    #     while self.is_running and self.board.checkBetting() == False:
    #         is_betting_done = self.board.bettings_process()
    #         if is_betting_done:
    #             break

    #     pass

    def game_loop(self):
        while self.is_running:
            self.get_events()
            self.update()
            if self.is_running == False:
                break
            self.render()
            self.clock.tick(self.FRAME_PER_SECOND)
            pygame.display.flip()
        self.quit_modules()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                self.is_playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == self.keys["up"]:
                    self.actions["up"] = True
                elif event.key == self.keys["down"]:
                    self.actions["down"] = True
                elif event.key == self.keys["left"]:
                    self.actions["left"] = True
                elif event.key == self.keys["right"]:
                    self.actions["right"] = True
                elif event.key == self.keys["enter"]:
                    self.actions["enter"] = True
                elif event.key == pygame.K_ESCAPE:
                    self.is_running = False
                    self.is_playing = False
            elif event.type == pygame.KEYUP:
                if event.type == self.keys["up"]:
                    self.actions["up"] = False
                elif event.type == self.keys["down"]:
                    self.actions["down"] = False
                elif event.type == self.keys["left"]:
                    self.actions["left"] = False
                elif event.type == self.keys["right"]:
                    self.actions["right"] = False
                elif event.type == self.keys["enter"]:
                    self.actions["enter"] = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.state_stack[-1].handle_events()
    
    def update(self):
        self.state_stack[-1].update(self.actions)
    
    def render(self):
        self.state_stack[-1].render(Render.screen)

    def load_states(self):
        self.menu = Menu(self)
        self.state_stack.append(self.menu)

    def quit_modules(self):
        pygame.mixer.quit()
        pygame.display.quit()
        pygame.font.quit()
    def load_assets(self):
        pass

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False
            
        

