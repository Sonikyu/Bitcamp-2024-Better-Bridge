import pygame
import Render
from Render import Button, Title_Text, Text
class State:
    def __init__(self, game) -> None:
        self.game = game
        self.prev_state = None
    def handle_events(self, event):
        pass
    def update(self):
        pass
    def render(self, surface):
        pass
    def enter_state(self):
        if (self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)
    def exit_state(self):
        self.game.state_stack.pop()

class Menu(State):
    def __init__(self, game):
        self.game = game
        super(Menu, self).__init__(game)
        pygame.display.set_caption("Bridge Game [Main Menu]")
        half_width = Render.SCREEN_WIDTH//2
        height = Render.SCREEN_HEIGHT
        self.title = Render.Title_Text('Better Bridge Game!', 100, (half_width, height// 10))
        self.multiplayer_button = Render.Button("MULTIPLAYER", 75, (half_width, height//3))
        self.single_button = Render.Button("SINGLE", 75, (half_width, height//2))
        self.setting_button = Render.Button("SETTINGS", 75, (half_width, height//2 + height//6))
        self.quit_button = Render.Button("QUIT", 75, (half_width, height//2 + height//3))
        self.drawables = [self.title, self.multiplayer_button, self.single_button, self.setting_button, self.quit_button]
        
        self.index = 0
        self.menu_options = {
            0 : "MULTIPLAYER",
            1 : "SINGLE",
            2 : "SETTINGS",
            3 : "QUIT"
            }
        self.buttons = {
            0 : self.multiplayer_button,
            1 : self.single_button,
            2 : self.setting_button,
            3 : self.quit_button
        }

    
    def handle_events(self):
        for index in self.buttons:
            self.check_mouse_pos()
            if self.buttons[index].check_for_clicks():
                self.index = index
                self.transition_state()

    def update(self, actions):
        self.update_cursor(actions)
        self.check_mouse_pos()
        if actions["enter"]:
            self.transition_state()
        self.game.reset_keys()
    def update_cursor(self, actions):
        if actions["up"]:
            self.index = (self.index - 1) % len(self.menu_options)
        elif actions["down"]:
            self.index = (self.index + 1) % len(self.menu_options)
        self.highlight_text()
    
    def check_mouse_pos(self):
        for index in self.buttons:
            #print(self.buttons[index].text)
            if self.buttons[index].rect.collidepoint(pygame.mouse.get_pos()):
                self.index = index
                self.highlight_text()
    def highlight_text(self):
        for button in self.buttons.values():
            button.is_highlighted = False
        self.buttons[self.index].is_highlighted = True
    
    def transition_state(self):
        print("Transition States Activated")
        if self.menu_options[self.index] == "MULTIPLAYER":
            raise NotImplementedError
        elif self.menu_options[self.index] == "SINGLE":
            raise NotImplementedError
        elif self.menu_options[self.index] == "SETTINGS":
           raise NotImplementedError 
        elif self.menu_options[self.index] == "QUIT":
            self.game.is_running = False
            super().exit_state()
        
    def render(self, display):
        display.fill(Render.green)
        for item in self.drawables:
            item.draw()
class Setting(State):
    def __init__(self, game) -> None:
        self.game = game
        super(Setting, self).__init__(game)
        pygame.display.set_caption("Bridge Game [Settings]")
        half_width = Render.SCREEN_WIDTH//2
        height = Render.SCREEN_HEIGHT
        self.title = Render.Title_Text('SETTINGS', 100, (half_width, height// 15))
        self.music_text = Render.Title_Text('Music:', 60, (Render.SCREEN_WIDTH//10 * 3, height// 5), False)
        
        self.back_button = Render.Button("Back", 60, (Render.SCREEN_WIDTH//3, height//3))
        self.reset_name_button = Render.Button("SINGLE", 75, (half_width, height//2))
        self._button = Render.Button("SETTINGS", 75, (half_width, height//2 + height//6))
        self.quit_button = Render.Button("QUIT", 75, (half_width, height//2 + height//3))
        self.drawables = [self.title, self.multiplayer_button, self.single_button, self.setting_button, self.quit_button]
        
        self.index = 0
        self.menu_options = {
            0 : {0 : "STOP/PLAY_MUSIC", 1 : "MUSIC_VOLUME_PLUS", 2 : "MUSIC_VOLUME_MINUS"},
            1 : {0 : ""},
            2 : {},
            3 : {}
            }
        self.buttons = {
            0 : self.multiplayer_button,
            1 : self.single_button,
            2 : self.setting_button,
            3 : self.quit_button
            }

    def handle_events(self, event):
        pass
    def update(self):
        pass
    def render(self, surface):
        pass