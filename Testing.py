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

player_positions = ((SCREEN_WIDTH//15, SCREEN_HEIGHT//2), (SCREEN_WIDTH//2, SCREEN_HEIGHT//25), 
                    (SCREEN_WIDTH//15 * 14, SCREEN_HEIGHT//2), (SCREEN_WIDTH//2, SCREEN_HEIGHT//25 * 20))
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

pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.QUIT])
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
gravity_time = 20
update_gravity = pygame.event.custom_type() + 1
def create_moving_cards():

    pygame.time.set_timer(update_gravity, gravity_time)

    hand_offset = (SCREEN_WIDTH - ((len(board.player1.hand) + 1) * (CARD_WIDTH * 2/3))) / 2
    loc_offset = 0
    for card in board.player1.hand:
        card.rect.x = (hand_offset + loc_offset*CARD_WIDTH * 2/3)
        card.rect = card.rect.inflate(0, HAND_Y)
        loc_offset += 1
def check_if_cards_move(event):
    for card in board.player1.hand:  
            if event.type == update_gravity:
                card.gravity_update()
create_moving_cards()

while run:
    screen.fill(green)
    for card in board.player1.hand:
        screen.blit(card.image, card.rect)

    Render.draw_centered_Text("Testing Text", font, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT//5))
    for i in range(0,4):
        Render.draw_centered_title_text(f"Player {i+1}", font, white, player_positions[i])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        check_if_cards_move(event)
        # for card in board.player1.hand:  
        #     if event.type == update_gravity:
        #         card.gravity_update()
       
    pygame.display.update()
    clock.tick(frame_rate_per_second)


pygame.quit()


#Better Title Text -> hoeflertext, plantagenetcherokee, ヒラキノ明朝pron
#Untitled Text -> bodoni72smallcapsbook
#Leadership Board Text -> silom

#Readable: applemyungjo, [times, courier, georgia,] kefa
#Thin Readable: euphemiacas, ヒラキノ角コシックw2, hiraginosansgb, sfnsmono, optima, palatino, sukhumvitset
#Fancy: hoeflertext, plantagenetcherokee, newyork (probably looks better without shadow), ヒラキノ明朝pron, bodoni72smallcapsbook, 
#Cursive/unreadable: brushscript, zapfino
#Bold and clear: arialblack, ヒラキノ角コシックw8, ヒラキノ角コシックw9, rockwell, silom