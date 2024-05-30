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

green = (27, 99, 46)
white = (255,255,255)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750
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
font = pygame.font.Font('freesansbold.ttf', 30)
for i in range(0,4):
    Render.draw_title_text("12345678", font, white, player_positions[i])
pygame.display.flip()
time.sleep(2)