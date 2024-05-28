import os, pygame, math, time
from BetSuit import BetSuit
from Suit import Suit
from BetButton import BetButton

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750
CARD_WIDTH = 100
CARD_HEIGHT = 145
HAND_Y = SCREEN_HEIGHT - (CARD_HEIGHT + 20)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

size_bet_rects = []
suit_bet_rects = []
pass_rect = pygame.Rect(820, 315, 100, 100)
submit_rect = pygame.Rect(730, 405, 190, 75)

#Colors
black = (0,0,0)
white = (255,255,255)
gray = (170,170,170)
green = (27, 99, 46)
light_green = (179,202,141)
dark_green = (27, 45, 46)
tan = (210, 180, 140)
dark_red = (156, 33, 61)
light_red = (200, 33, 61)
rich_black = (1, 22, 39)

icon = pygame.image.load("Misc_Images/poker-hand.png") #Lorc [https://lorcblog.blogspot.com/]
pygame.display.set_icon(icon)

pygame.mixer.init()
button_sound = pygame.mixer.Sound("Sounds/menu-button.mp3")
card_sound = pygame.mixer.Sound("Sounds/card.mp3")
vine_boom = pygame.mixer.Sound("Sounds/boom.mp3")
punch_sound = pygame.mixer.Sound("Sounds/Punch.wav")
list_of_songs = ("Jazzy Vibes #36 - Loop.mp3", "backup_plan.wav", "Casino Man.ogg", 
        "pixel_sprinter_loop.wav", "short_A New World Order!!.mp3")
#Zane Little Music = backup_plan, pixel_sprinter_loop
#Spring Spring = Casino Man
#Tri Tachyon = Jazzy Vibes #36 ("Music by Tri-Tachyon - https://soundcloud.com/tri-tachyon/albums".)
#SOUND AIRYLUVS by ISAo https://airyluvs.com/ = short_A_New World Order!! OGA License

DEFAULT_MUSIC_VOLUME = 0.1

def set_music(index: int) -> None:
    '''
    Plays music
    :para index: input to find and play song
    :return: None
    '''
    pygame.mixer.music.load(f"Music/{list_of_songs[index]}")
    pygame.mixer.music.play(-1) 
def set_music_vol(level: int) -> None:
    '''
    Sets the volume of the music
    :para level: used to set volume of music
    :return: None
    '''
    pygame.mixer.music.set_volume(level)
    

def draw_setting(board) -> None:
    run = True
    isMusicPlaying = True
    while run:
        screen.fill(rich_black)
        font = pygame.font.Font('freesansbold.ttf', 80)
        font.set_underline(True)
        draw_title_text("SETTINGS", font, white, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 10))
        font = pygame.font.Font('freesansbold.ttf', 50)
        draw_title_text("Music", font, white, (SCREEN_WIDTH//10, SCREEN_HEIGHT//5))
        
        back_button = MenuButton("Back", font, (SCREEN_WIDTH//3, SCREEN_HEIGHT//10 * 9), True)
        reset_name_button = MenuButton("Reset Name", font, (SCREEN_WIDTH//3 * 2, SCREEN_HEIGHT//10 * 9), True)
        isMusicPlaying = pygame.mixer.music.get_busy()
        text = "Stop Music"  if isMusicPlaying else "Play Music"
        play_or_stop_button = MenuButton(text, font, (SCREEN_WIDTH//10 * 3 - 50, SCREEN_HEIGHT // 5 + 70 ), True)
        
        draw_title_text("Load Songs:", font, white, (SCREEN_WIDTH//10 * 2 - 50, SCREEN_HEIGHT//5 * 2))

        song1_button = MenuButton("1", font, (SCREEN_WIDTH//10 * 2 - 50, SCREEN_HEIGHT // 5 * 3 ), True)
        song2_button = MenuButton("2", font, (SCREEN_WIDTH//10 * 3 - 50, SCREEN_HEIGHT // 5 * 3 ), True)
        song3_button = MenuButton("3", font, (SCREEN_WIDTH//10 * 4 - 50, SCREEN_HEIGHT // 5 * 3 ), True)
        song4_button = MenuButton("4", font, (SCREEN_WIDTH//10 * 5 - 50, SCREEN_HEIGHT // 5 * 3 ), True)
        song5_button = MenuButton("5", font, (SCREEN_WIDTH//10 * 6 - 50, SCREEN_HEIGHT // 5 * 3 ), True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                board.getType = "QUIT"
                pygame.quit()
                run = False
            elif back_button.check_click():
                run = False
            elif reset_name_button.check_click():
                os.remove(board.NAME_FILE)
                board.check_profile_name()
                time.sleep(1)
                screen.fill(rich_black)
            elif play_or_stop_button.check_click():
                if isMusicPlaying:
                    pygame.mixer.music.fadeout(1000)
                else:
                    pygame.mixer.music.play(-1)
            elif song1_button.check_click():
                set_music(0)
            elif song2_button.check_click():
                set_music(1)
            elif song3_button.check_click():
                set_music(2)
            elif song4_button.check_click():
                set_music(3)
            elif song5_button.check_click():
                set_music(4)


        pygame.display.flip()

def draw_get_name() -> str:
    text_box_x = SCREEN_WIDTH//2
    text_box_y = SCREEN_HEIGHT//2 * 1.5
    color_active = white
    color_passive = black
    color = color_passive
    active = False
    user_name = ''
    input_rectangle = pygame.Rect(0,0, 90, 90)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rectangle.collidepoint(event.pos):
                    active = True
                    color = color_active
                else:
                    active = False
                    color = color_passive
            if event.type == pygame.KEYDOWN and not event.key == pygame.K_SPACE and active:
                isBackSpace = event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE
                isReturn = event.key == pygame.K_RETURN
                isWithinRange = len(user_name) <= 8
                if isBackSpace:
                    user_name = user_name[0:-1]
                if isReturn:
                    run = False
                if isWithinRange and not isBackSpace and not isReturn:
                    user_name += event.unicode
        
        screen.fill(green)
        font = pygame.font.Font('freesansbold.ttf', 100)
        font.set_underline(True)
        draw_title_text("Input a Profile Name", font, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT // 10))
        font = pygame.font.Font('freesansbold.ttf', 80)
        draw_title_text("Requirements:", font, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT // 5 + 50))
        font = pygame.font.Font('freesansbold.ttf', 50)
        draw_centered_Text("- Less than or equal to 8 characters", font, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT // 5 + 130))
        draw_centered_Text("- No Spaces", font, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT // 5 + 180))
        font = pygame.font.Font('freesansbold.ttf', 100)
        input_rectangle.center = (text_box_x,text_box_y)
        text_surface = font.render(user_name, True, white)
        pygame.draw.rect(screen, color, input_rectangle, 2)
        input_rectangle.w = text_surface.get_width() + 5
 
        screen.blit(text_surface, input_rectangle)
        pygame.display.flip()
    return user_name



def draw_menu_screen(board) -> None:
    """
    Creates a menu window with a MULTIPLAYER, SINGLEPLAYER, SETTING, & QUIT buttons
    Each button changes the board's getState
    :param board: used to change board's state
    :return: None
    """
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.Font('freesansbold.ttf', 100)
        font.set_underline(True)
        #draw_centered_Text('Better Bridge Game!', font, white, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 10))
        draw_title_text('Better Bridge Game!', font, white, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 10))
        border = submit_rect        
        #Text
        font = pygame.font.Font('freesansbold.ttf', 80)
        #draw_menu_button("MULTIPLAYER", font, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT//3))
        multi_button = MenuButton("MULTIPLAYER", font, (SCREEN_WIDTH//2, SCREEN_HEIGHT//3), True)
        #draw_menu_button("SINGLE PLAYER", font, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        single_button = MenuButton("SINGLE PLAYER", font, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), True)
        #draw_menu_button("SETTINGS", font, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + SCREEN_HEIGHT//6))
        setting_button = MenuButton("SETTINGS", font, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + SCREEN_HEIGHT//6), True)
        #draw_menu_button("QUIT", font, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + SCREEN_HEIGHT//3))
        quit_button = MenuButton("QUIT", font, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + SCREEN_HEIGHT//3), True)
        mouse_Pos = pygame.mouse.get_pos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT")
                board.getState = "QUIT"
                run = False
            elif multi_button.check_click():
                print("MULTIPLAYER CLICKED")
                #board.getState = "MULTIPLAYER"
                raise NotImplementedError()
            elif single_button.check_click():
                print("SINGLE PLAYER CLICKED")
                board.gameMode = "SINGLE"
                board.getState = None
                print(f"{board.getState}")
                run = False
            elif setting_button.check_click():
                print("SETTINGS CLICKED")
                pygame.display.set_caption("Bridge Game [Settings]")
                draw_setting(board)
            elif quit_button.check_click():
                print("QUIT CLICKED")
                board.getState = "QUIT"
                run = False
            pygame.display.flip()
    if board.getState == "QUIT":
        print("pygame quitted")
        pygame.display.quit()
        pygame.quit()
    print("MENU CLOSED")

#Might delete
def draw_out_of_game(board):
    screen.fill(green)
    if board.getState == "MENU":
        draw_menu_screen()

def draw_gameplay(board):
    #Draw the background
    screen.fill(green)
    #Draw the player hand
    hand_offset = (SCREEN_WIDTH - ((len(board.player1.hand) + 1) * (CARD_WIDTH * 2 / 3))) / 2
    loc_offset = 0
    for card in board.player1.hand:       
        screen.blit(card.image, (hand_offset + loc_offset*CARD_WIDTH * 2/3, HAND_Y))
        loc_offset += 1
    #Draw the pile
    draw_pile(screen, board.currentTrick)
    #Draw the trump suit
    draw_trump(screen, board.trumpSuit)
    #Draw the score (rounds won)
    
    if board.getState == "PLAYING":
        pygame.display.set_caption("Bridge Game [Playing...]")
        draw_scores(screen, board.teamOneScore, board.teamTwoScore, board.gamesToWin)
        draw_your_turn(board.yourTurn)
    #Draw betting UI, if applicable
    elif board.getState == "BETTING":
        pygame.display.set_caption("Bridge Game [Betting...]")
        draw_bets(screen, board)
    elif board.getState == "GAME_OVER":
        pygame.display.set_caption("Bridge Game [LeaderBoard]")
        draw_game_over_screen(board)
    elif board.gameMode == "MULTI":
        pygame.display.set_caption("Bridge Game [Setting Team...]")
        #SETUP TEAM IN BOARD
    elif board.gameMode == "SINGLE":
        board.set_up_players()
    pygame.display.flip()

#Returns the path to the image associated with card
def get_png_from_card(card):
    output = ""
    rank_val = card.rank.value
    if rank_val >= 11:
        output += card.rank.name.lower()
    else:
        output += str(rank_val)
    output += "_of_"
    output += card.suit.name.lower()
    output += ".png"
    return os.path.join("Cards", output)

#Draws the pile in the center of the screen, pile MUST be length 4 with None for any position not yet filled
def draw_pile(screen, pile):
    #SOUTH
    if pile[0] != None:
        screen.blit(pile[0].image, (SCREEN_WIDTH / 2 - CARD_WIDTH / 2, SCREEN_HEIGHT /2))
    #WEST
    if pile[1] != None:
        screen.blit(pile[1].image, (SCREEN_WIDTH / 2 - CARD_WIDTH * 1.5, SCREEN_HEIGHT /2 - CARD_HEIGHT * .75))
    #NORTH
    if pile[2] != None:
        screen.blit(pile[2].image, (SCREEN_WIDTH / 2 - CARD_WIDTH / 2, SCREEN_HEIGHT /2 - CARD_HEIGHT * 1.5))
    #EAST
    if pile[3] != None:
        screen.blit(pile[3].image, (SCREEN_WIDTH / 2 + CARD_WIDTH * .5, SCREEN_HEIGHT /2 - CARD_HEIGHT * .75))

def get_glyph_from_suit(suit):
    glyph_name = suit.name.lower() + "_glyph.png"
    glyph_path = os.path.join("Cards", glyph_name)
    img = pygame.image.load(glyph_path)
    return img

def draw_trump(screen, suit):
    if suit == None:
        return
    #Background
    bgnd = pygame.Rect(0, 0, 210, 120)
    border_r = pygame.Rect(210, 0, 10, 130)
    border_b = pygame.Rect(0, 120, 210, 10)
    pygame.draw.rect(screen, gray, bgnd)
    pygame.draw.rect(screen, black, border_r)
    pygame.draw.rect(screen, black, border_b)
    #Text
    font = pygame.font.Font('freesansbold.ttf', 20)
    draw_centered_Text(f"Trump: {suit.name}", font, black, (105, 30))
    #Glyph
    if (suit != BetSuit.LOW and suit != BetSuit.HIGH):
        img = get_glyph_from_suit(suit)
        draw_centered_Element(img, (105, 80))
        

def draw_scores(screen, score_1, score_2, team_1_to_win):
    if team_1_to_win == 13:
        team_2_to_win = 1
    elif team_1_to_win == 0:
        team_1_to_win = 1
        team_2_to_win = 13
    else:
        team_2_to_win = 13 - team_1_to_win + 1
    #Background
    bgnd = pygame.Rect(220, 0, 210, 120)
    border_r = pygame.Rect(430, 0, 10, 130)
    border_b = pygame.Rect(220, 120, 210, 10)
    border_m = pygame.Rect(320, 0, 10, 130)
    pygame.draw.rect(screen, gray, bgnd)
    pygame.draw.rect(screen, black, border_r)
    pygame.draw.rect(screen, black, border_b, 5)
    pygame.draw.rect(screen, black, border_m, 5)
    #Text
    font = pygame.font.Font('freesansbold.ttf', 30)
    draw_centered_Text(f"{str(score_1)} / {str(team_1_to_win)}" , font, black, (272, 60)) #Text1
    draw_centered_Text(f"{str(score_2)} / {str(team_2_to_win)}", font, black, (378, 60)) #Text2

def draw_game_over_screen(board):
   screen.fill(dark_red)
   font = pygame.font.SysFont('georgia', 100)
   font.set_underline(True)
   #draw_centered_Text("Game Over", font, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT//14))
   draw_title_text("Game Over", font, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT//14))
   font = pygame.font.SysFont('georgia', 70)
   #draw_centered_Text(f"Team {str(board.winningTeam)} Wins!", font, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT//5))
   draw_title_text(f"Team {str(board.winningTeam)} Wins!", font, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT//5))
   font = pygame.font.SysFont('georgia', 60)
   font.set_underline(True)
   #draw_centered_Text("LeaderBoard:", font, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT//3))
   draw_title_text("LeaderBoard:", font, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT//3))
   font = pygame.font.SysFont('georgia', 50)
   leaderboard = sorted(board.players,key=lambda x: x.wins, reverse=True)
   time.sleep(0.5)
   space:int = 80
   num = 1
   for player in leaderboard:
       #draw_centered_Text(f"{str(num)}. {str(player)}, SCORE: {str(player.wins)}", font, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT//3 + space))
       draw_title_text(f"{str(num)}. {str(player)}, SCORE: {str(player.wins)}", font, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT//3 + space))
       punch_sound.play()
       pygame.display.update()
       space += 80
       num += 1
       time.sleep(0.2)
   running = True
   while running:
       try_again_button = MenuButton("TRY AGAIN", font, (SCREEN_WIDTH-160, SCREEN_HEIGHT-170), True)
       menu_button = MenuButton("MENU", font, (SCREEN_WIDTH-160, SCREEN_HEIGHT-80), True)
       pygame.display.update()
       for event in pygame.event.get():
            if try_again_button.check_click():
                print("TRY AGAIN PRESSED")
                #board.reset_values()
                running = False
            elif menu_button.check_click():
                print("MENU CLICKED")
                board.getState = "MENU"
                running = False
            elif event == pygame.QUIT:
                #Problem where it doesn't quit when you press the X button
                board.getState = "QUIT"
                print("QUIT")
                running = False

def draw_your_turn(isYourTurn: bool):
    font = pygame.font.SysFont('georgia', 40)
    if isYourTurn:
         draw_title_text("Your Turn!", font, white, (SCREEN_WIDTH-115, 30))
    else:
         draw_title_text("Waiting...", font, white, (SCREEN_WIDTH-115, 30))

def draw_bets(screen, board):
    global size_bet_rects
    global suit_bet_rects
    size_bet_rects = []
    suit_bet_rects = []
    #Calculate how many numbers are valid
    bet_id = board.currentBetID
    lowest_bet_size = math.floor(math.fabs(bet_id) / 6) + 7
    #Draw size boxes
    for i in range(lowest_bet_size, 14):
        rect = draw_size_bet_box(screen, i, 280 + 90*(i - lowest_bet_size), 225)
        size_bet_rects.append(rect)
    #Draw suit boxes
    for betsuit in BetSuit:
        rect = draw_suit_bet_box(screen, betsuit, 280 + 90*(betsuit.value), 315)
        suit_bet_rects.append(rect)
    #Draw pass button
    border = pass_rect
    bgnd = pygame.Rect(830, 325, 80, 80)
    pygame.draw.rect(screen, black, border)
    pygame.draw.rect(screen, light_green, bgnd)
    #Text
    font = pygame.font.Font('freesansbold.ttf', 30)
    draw_centered_Text("PASS", font, black, (870,365))
    #Draw submit button
    border = submit_rect
    bgnd = pygame.Rect(740, 415, 170, 55)
    pygame.draw.rect(screen, black, border)
    pygame.draw.rect(screen, dark_red, bgnd)
    #Text
    font = pygame.font.Font('freesansbold.ttf', 30)
    draw_centered_Text("SUBMIT", font, black, (825,442.5))

def draw_size_bet_box(screen, size, x, y):
    #Background
    border = pygame.Rect(x, y, 100, 100)
    bgnd = pygame.Rect(x + 10, y + 10, 80, 80)
    pygame.draw.rect(screen, black, border)
    pygame.draw.rect(screen, gray, bgnd)
    #Text
    font = pygame.font.Font('freesansbold.ttf', 40)
    draw_centered_Text(str(size), font, black, (x+50,y+50))
    return BetButton(border, size, None)

def draw_suit_bet_box(screen, betsuit, x, y):
    #Background
    border = pygame.Rect(x, y, 100, 100)
    bgnd = pygame.Rect(x + 10, y + 10, 80, 80)
    pygame.draw.rect(screen, black, border)
    pygame.draw.rect(screen, gray, bgnd)
    #Contents
    font = pygame.font.Font('freesansbold.ttf', 30)
    if betsuit.value == 0:
        draw_centered_Text("LOW", font, black, (x+50,y+50))
    elif betsuit.value == 5:
        draw_centered_Text("HIGH", font, black,(x+50,y+50))
    else:
        img = get_glyph_from_suit(Suit(betsuit.value))
        draw_centered_Element(img, (x+50, y+50))
    return BetButton(border, None, betsuit)
def player_choosing_cards(board):
    running = True
    while running:
        board.yourTurn = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if board.getState == "PLAYING":
                for card in board.players[0].hand:
                    card_rect = pygame.Rect(card.x, HAND_Y, CARD_WIDTH *2 / 3, CARD_HEIGHT)
                    if card_rect.collidepoint(event.pos) and board.player1.isValidCardMove(card, board):
                        print(f"Clicked on  {str(card)}")
                        #self.player1.playCard(card, self)
                        tempCard = card
                        running = False  
        draw_gameplay(board)
        board.yourTurn = False
    return tempCard
#Helper Functions
def draw_centered_Text(text: str, font, text_col: tuple, center: tuple):
    img = font.render(text, True, text_col)
    img_rect = img.get_rect()
    img_rect.center = center
    screen.blit(img, img_rect)
def draw_centered_Element(img, center: tuple):
    img_rect = img.get_rect()
    img_rect.center = center
    screen.blit(img, img_rect)
def draw_title_text(text: str, font, text_col: tuple, center: tuple):
    draw_centered_Text(text, font, black, (center[0] + 4, center[1] + 4))
    draw_centered_Text(text, font, gray, (center[0] + 2, center[1] + 2))
    draw_centered_Text(text, font, text_col, center)
'''
def draw_menu_button(text: str, font, text_col: tuple, center: tuple):
    (width, height) = font.size(text)
    inner_button = pygame.Rect(0,0, width + 20, height + 20)
    shade_button = pygame.Rect(0, 0, width + 10, height + 10)
    outline = pygame.Rect(0,0, width + 22, height + 22)
    inner_button.center = center
    outline.center = center
    shade_button.center = center
    #shading background
    backgrnd_shade = pygame.Rect(0, 0, width + 22, height + 22)
    (x,y) = center
    backgrnd_shade.center = (x+5, y+ 5)
    pygame.draw.rect(screen, dark_green, backgrnd_shade, 0, 15, 15, 15, 15, 15)
    pygame.draw.rect(screen, dark_red, inner_button, 0, 15, 15, 15, 15, 15)
    pygame.draw.rect(screen, light_red, shade_button, 0, 15, 15, 15, 15, 15)
    pygame.draw.rect(screen, black, outline, 2, 15, 15, 15, 15, 15)
    draw_centered_Text(text, font, text_col, center)
'''
class MenuButton:
    def __init__(self, text: str, font, center: tuple, enabled: bool) -> None:
        self.text = text
        self.font = font
        self.center = center
        self.enabled = enabled
        self.rect = self.draw(False)
    def draw(self, clicked: bool):
        (width, height) = self.font.size(self.text)
        self.inner_button = pygame.Rect(0,0, width + 20, height + 20)
        self.shade_button = pygame.Rect(0, 0, width + 10, height + 10)
        self.outline = pygame.Rect(0,0, width + 22, height + 22)
        self.inner_button.center = self.center
        self.outline.center = self.center
        (self.xpos, self.ypos) = self.outline.topleft
        self.shade_button.center = self.center
        #shading background
        backgrnd_shade = pygame.Rect(0, 0, width + 22, height + 22)
        (x,y) = self.center
        backgrnd_shade.center = (x+5, y+ 5)
        pygame.draw.rect(screen, dark_green, backgrnd_shade, 0, 15, 15, 15, 15, 15)
        pygame.draw.rect(screen, dark_red, self.inner_button, 0, 15, 15, 15, 15, 15)
        if not clicked:
            pygame.draw.rect(screen, light_red, self.shade_button, 0, 15, 15, 15, 15, 15)
        pygame.draw.rect(screen, black, self.outline, 2, 15, 15, 15, 15, 15)
        draw_title_text(self.text, self.font, white, self.center)
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos
        left_click = pygame.mouse.get_pressed()[0]
        buttonrect = self.outline
        if left_click and buttonrect.collidepoint(mouse_pos()[0], mouse_pos()[1]) and self.enabled:
            self.draw(True)
            button_sound.play()
            time.sleep(1)
            return True
        else:
            self.draw(False)
            return False
        