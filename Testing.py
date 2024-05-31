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


green = (27, 99, 46)
white = (255,255,255)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750
pass_rect = pygame.Rect(820, 315, 100, 100)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
screen.fill(green)
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
import random
run = True
font = pygame.font.SysFont("ヒラキノ明朝pron", 60)
current_font = pygame.font.SysFont("plantagenetcherokee", 60)

pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.rect(screen, white, pass_rect)
    Render.draw_centered_Text("Current Text", current_font, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT//10))
    Render.draw_title_text("Current TEXT but titled", current_font, white, (600,375))
    Render.draw_centered_Text("New Text", font, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT//5))
    Render.draw_title_text("New Text but Titled", font, white, (600,505))
    for i in range(0,4):
        Render.draw_title_text("12345678", font, white, player_positions[i])
    screen.blit(text_surface, (0,0))
    pygame.display.update()
    clock.tick(60)



time.sleep(2)
pygame.quit()

#Better Title Text -> hoeflertext, plantagenetcherokee, ヒラキノ明朝pron
#Untitled Text -> bodoni72smallcapsbook
#Leadership Board Text -> silom

#Readable: applemyungjo, [times, courier, georgia,] kefa
#Thin Readable: euphemiacas, ヒラキノ角コシックw2, hiraginosansgb, sfnsmono, optima, palatino, sukhumvitset
#Fancy: hoeflertext, plantagenetcherokee, newyork (probably looks better without shadow), ヒラキノ明朝pron, bodoni72smallcapsbook, 
#Cursive/unreadable: brushscript, zapfino
#Bold and clear: arialblack, ヒラキノ角コシックw8, ヒラキノ角コシックw9, rockwell, silom
#Spooky