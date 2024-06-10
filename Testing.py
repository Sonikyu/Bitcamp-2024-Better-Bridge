import tkinter as tk
import tkinter.filedialog

'''
root = tk.Tk("Input Image")
root.withdraw()


filename = tkinter.filedialog.askopenfilename()

print(filename)
'''
import pygame
import Render, time
pygame.init()

clock = pygame.time.Clock()
frame_rate_per_second = 60


green = (27, 99, 46)
white = (255,255,255)
black = (0,0,0)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750
#SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_window_size()
pass_rect = pygame.Rect(820, 315, 100, 100)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

player_positions = ((SCREEN_WIDTH//20 * 2, SCREEN_HEIGHT//2), (SCREEN_WIDTH//2, SCREEN_HEIGHT//25), 
                    (SCREEN_WIDTH//20 * 18, SCREEN_HEIGHT//2), (SCREEN_WIDTH//2, SCREEN_HEIGHT//25 * 20))
player_bets = {
    0 : None,
    1 : None,
    2 : None,
    3 : None
}
text_surface = pygame.Surface((30,30))
text_surface.fill('Red')
run = True
from Board import Board 

CARD_WIDTH = 100
CARD_HEIGHT = 145
HAND_Y = SCREEN_HEIGHT - (CARD_HEIGHT//2)



run = True

pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.QUIT, pygame.K_ESCAPE])
font = pygame.font.SysFont("silom", 40)
board = Board()
board.name = "Cool"
board.gameMode = "SINGLE"
board.reset_values()
pygame.display.flip()

# gravity_time = 20
# update_gravity = pygame.event.custom_type() + 1

# pygame.time.set_timer(update_gravity, gravity_time)

screen.fill(green)
# hand_offset = (SCREEN_WIDTH - ((len(board.player1.hand) + 1) * (CARD_WIDTH * 2/3))) / 2
# loc_offset = 0
# for card in board.player1.hand:
#     card.rect.x = (hand_offset + loc_offset*CARD_WIDTH * 2/3)
#     card.rect = card.rect.inflate(0, HAND_Y)
#     loc_offset += 1
import random
gravity_time = 20
update_gravity = pygame.event.custom_type() + 1
particles = []
toUpdate = []
def create_moving_cards():

    pygame.time.set_timer(update_gravity, gravity_time)

    hand_offset = (SCREEN_WIDTH - ((len(board.player1.hand) + 1) * (CARD_WIDTH * 2/3))) / 2
    loc_offset = 0
    for card in board.player1.hand:
        card.rect.x = (hand_offset + loc_offset*CARD_WIDTH * 2/3)
        card.rect = card.rect.inflate(0, HAND_Y)
        rect = screen.blit(card.image, card.rect)
        loc_offset += 1
        toUpdate.append(rect)
def check_if_cards_move(event):
    for card in board.player1.hand:  
        if event.type == update_gravity:
            card.gravity_update()
create_moving_cards()

screen_shake = 0
x, y = 20, 20


button = Render.Button("TEST", 100, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))

text_to_draw = [button]
for i in range(0,4):
        player_text = Render.Title_Text(f"Player {i+1}", 40, player_positions[i])
        text_to_draw.append(player_text)
text_to_draw.append(Render.Text("Testing Text", 40, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT//5)))
#title_text = Render.Title_Text("TITLE TEXT", 100, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
while run:
    screen.fill(green)
    for card in board.player1.hand:
        screen.blit(card.image, card.rect)

    # particles.append([[SCREEN_WIDTH//2, SCREEN_HEIGHT//2], [random.randint(0,20)/10 -1, -2], random.randint(0, 5)])
    # for particle in particles:
    #     particle[0][0] += particle[1][0]
    #     particle[0][1] += particle[1][1]
    #     particle[2] -= 0.1
    #     pygame.draw.circle(screen, white, particle[0], particle[2])
    #     if particle[2] <= 0:
    #         particles.remove(particle)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        
        pygame.event.pump()
        check_if_cards_move(event)
        for card in board.player1.hand:  
            if event.type == update_gravity:
                card.gravity_update()
    for text in text_to_draw:
        text.draw()
    clock.tick(frame_rate_per_second)
    pygame.display.flip()

pygame.quit()

class Particle:
    def __init__(self, x_pos, y_pos, radius, time_limit):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius_limit = radius
        self.time_limit = time_limit
    # def update():
    #     self.x_limit += 
        
