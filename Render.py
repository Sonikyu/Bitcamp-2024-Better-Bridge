import os, pygame, math, time
from Assets.Bet_Related.Bet import Bet
from Assets.Bet_Related.Bet import BetFactory
from Assets.Bet_Related.BetSuit import BetSuit
from Assets.Card_Related.Suit import Suit
from BetButton import BetButton

#todo Reduce the amount of pygame.update() and pygame.flip()s used. You can input the object's rect into update in order to only update that
#todo move some of the import statements to only where they would be needed for use (Lazy loading modules research)
#todo optimize your code (python profiling)
#todo try to avoid using multi-threading

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750
CARD_WIDTH = 100
CARD_HEIGHT = 145
HAND_Y =  SCREEN_HEIGHT - (CARD_HEIGHT//2)#SCREEN_HEIGHT - (CARD_HEIGHT + 20)

sizes = {"width" : 1200, "height" : 145}

flags =  pygame.RESIZABLE
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], flags,)
screen.set_alpha(None)
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.QUIT])

clock = pygame.time.Clock()
FRAMES_PER_SECOND = 60


size_bet_rects = []
suit_bet_rects = []
pass_rect = pygame.Rect(820, 315, 100, 100)
submit_rect = pygame.Rect(730, 405, 190, 75)

#Fonts
pygame.font.init()
DEFAULT_TITLE_TEXT_SIZE = 100
font_silom_80 = pygame.font.SysFont("silom", DEFAULT_TITLE_TEXT_SIZE)
font_silom_75 = pygame.font.SysFont("silom", 75) 
font_silom_60 = pygame.font.SysFont("silom", 60)
font_silom_40 = pygame.font.SysFont("silom", 40) 
font_silom_30 = pygame.font.SysFont("silom", 30)
#figure this out later
fonts = {
    100 : pygame.font.SysFont("silom", 100),
    75 : pygame.font.SysFont("silom", 75),
    60 : pygame.font.SysFont("silom", 60),
    40 : pygame.font.SysFont("silom", 40),
    30 : pygame.font.SysFont("silom", 30)
         }

#Colors
black = (0,0,0)
white = (255,255,255)
gray = (170,170,170)
green = (27, 99, 46)
light_green = (179,202,141)
dark_green = (27, 45, 46)
tan = (210, 180, 140)
dark_red = (156, 33, 61)
red = (200, 33, 61)
light_red = (240, 33, 61)
rich_black = (1, 22, 39)

icon = pygame.image.load("Misc_Images/poker-hand.png").convert() #Lorc [https://lorcblog.blogspot.com/]
pygame.display.set_icon(icon)

pygame.mixer.init()

button_sound = pygame.mixer.Sound("Sounds/click.5.ogg")
card_sound = pygame.mixer.Sound("Sounds/card.mp3")
vine_boom = pygame.mixer.Sound("Sounds/boom.mp3")
punch_sound = pygame.mixer.Sound("Sounds/Punch.wav")
stone_drop_sound = pygame.mixer.Sound("Sounds/stone-dropping.mp3")
coin_sound = pygame.mixer.Sound("Sounds/coin-dropped.mp3")
buzz_sound = pygame.mixer.Sound("Sounds/bzzzt.wav")
boing_sound = pygame.mixer.Sound("Sounds/boing.wav")
sound_list = (button_sound, card_sound, vine_boom, punch_sound, stone_drop_sound, coin_sound, buzz_sound)
list_of_songs = ("Jazzy Vibes #36 - Loop.mp3", "backup_plan.wav", "Casino Man.ogg", 
        "pixel_sprinter_loop.wav", "short_A New World Order!!.mp3")
#Zane Little Music = backup_plan, pixel_sprinter_loop
#Spring Spring = Casino Man
#Tri Tachyon = Jazzy Vibes #36 ("Music by Tri-Tachyon - https://soundcloud.com/tri-tachyon/albums".)
#SOUND AIRYLUVS by ISAo https://airyluvs.com/ = short_A_New World Order!! OGA License

DEFAULT_MUSIC_VOLUME = 0.1

#Betting position
player_positions = ((SCREEN_WIDTH//15, SCREEN_HEIGHT//2), (SCREEN_WIDTH//2, SCREEN_HEIGHT//25), 
                    (SCREEN_WIDTH//15 * 14, SCREEN_HEIGHT//2), (SCREEN_WIDTH//2, SCREEN_HEIGHT//25 * 20))

def set_music(index: int) -> None:
    '''
    Plays music
    :para index: input to find and play song
    :return: None
    '''
    pygame.mixer.music.load(f"Music/{list_of_songs[index]}")
    pygame.mixer.music.set_volume(-1)
    pygame.mixer.music.play(-1) 

def set_music_vol(change: int) -> None:
    '''
    Sets the volume of the music
    :para change: used to change volume of music
    :return: None
    '''
    volume = pygame.mixer.music.get_volume() + change
    if (volume < 0.05):
        volume = 0
    pygame.mixer.music.set_volume(volume)

def set_sound_vol(change: int):
    volume = button_sound.get_volume() + change
    if (volume < 0.05):
        volume = 0
    for sound in sound_list:
        sound.set_volume(volume)

def draw_setting(board) -> None:
    pygame.display.set_caption("Bridge Game [Settings]")
    run = True
    isMusicPlaying = True
    song_index = 0
    while run:
        screen.fill(rich_black)
        draw_centered_title_text("SETTINGS", font_silom_80, white, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 15))
        
        back_button = MenuButton("Back", font_silom_60, (SCREEN_WIDTH//3, SCREEN_HEIGHT//10 * 9), True)
        reset_name_button = MenuButton("Reset Name", font_silom_60, (SCREEN_WIDTH//3 * 2, SCREEN_HEIGHT//10 * 9), True)
        #Music Setting Buttons
        draw_left_aligned_title_text("Music:", font_silom_60, white, (SCREEN_WIDTH//30, SCREEN_HEIGHT//5))
        isMusicPlaying = pygame.mixer.music.get_busy()
        text = "Stop Music"  if isMusicPlaying else "Play Music"
        play_or_stop_button = MenuButton(text, font_silom_30, (SCREEN_WIDTH//10 * 3, SCREEN_HEIGHT // 5), True)
        draw_centered_title_text(f"Volume: {int(pygame.mixer.music.get_volume() * 100)}", font_silom_60, white, (SCREEN_WIDTH//10 * 7 - 50, SCREEN_HEIGHT // 5) )
        increase_music_volume_button = MenuButton("+", font_silom_30, (SCREEN_WIDTH//10 * 9 + 50, SCREEN_HEIGHT // 5), True)
        decrease_music_volume_button = MenuButton("-", font_silom_30, (SCREEN_WIDTH//10 * 9 - 50, SCREEN_HEIGHT // 5), True)
        #Sound Settinig Buttons
        draw_left_aligned_title_text("Sound Effects:", font_silom_60, white, (SCREEN_WIDTH//30, SCREEN_HEIGHT//10 * 4 - 50))
        draw_centered_title_text(f"Volume: {int(button_sound.get_volume() * 100)}", font_silom_60, white, (SCREEN_WIDTH//10 * 7 - 50, SCREEN_HEIGHT // 10 * 4 - 50))
        increase_sound_volume_button = MenuButton("+", font_silom_30, (SCREEN_WIDTH//10 * 9 + 50, SCREEN_HEIGHT // 10 * 4 - 50), True)
        decrease_sound_volume_button = MenuButton("-", font_silom_30, (SCREEN_WIDTH//10 * 9 - 50, SCREEN_HEIGHT // 10 * 4 - 50), True)
        #Loading Songs Settings
        draw_left_aligned_title_text("Load Songs:", font_silom_60, white, (SCREEN_WIDTH//30, SCREEN_HEIGHT//10 * 4 + 50))
        song_button_list = []
        for index in range(1, 6):
            song_button = MenuButton(str(index), font_silom_30, (SCREEN_WIDTH//10 * (4 + index) - 50, SCREEN_HEIGHT // 10 * 4 + 50), True)
            song_button_list.append(song_button)
        draw_centered_title_text(f"Current Song: {list_of_songs[song_index]}", font_silom_30, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT//10 * 6))
        draw_centered_title_text(f"Your Name Is: {board.name}", font_silom_60, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT // 10 * 8 - 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                board.getType = "QUIT"
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
            elif increase_music_volume_button.check_click():
                set_music_vol(0.05)
            elif decrease_music_volume_button.check_click():
                set_music_vol(-0.05)
            elif increase_sound_volume_button.check_click():
                set_sound_vol(0.05)
            elif decrease_sound_volume_button.check_click():
                set_sound_vol(-0.05)
            else:
                for index, song_button in enumerate(song_button_list):
                    if song_button.check_click():
                        song_index = index
                        set_music(song_index)
        pygame.display.flip()

def draw_get_name() -> str:
    text_box_x = SCREEN_WIDTH//2
    text_box_y = SCREEN_HEIGHT//2 * 1.5
    user_name = ''
    input_rectangle = pygame.Rect(0,0, 90, 90)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                isBackSpace = event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE
                isReturn = event.key == pygame.K_RETURN
                isWithinRange = len(user_name) < 8
                if isBackSpace:
                    user_name = user_name[0:-1]
                if isReturn:
                    run = False
                if isWithinRange and not isBackSpace and not isReturn:
                    user_name += event.unicode
        
        screen.fill(green)
        draw_centered_title_text("Input a Profile Name", font_silom_80, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT // 10))
        draw_centered_title_text("Requirements:", font_silom_60, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT // 5 + 50))
        draw_centered_Text("- Less than or equal to 8 characters", font_silom_30, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT // 5 + 130))
        input_rectangle.center = (text_box_x,text_box_y)
        text_surface = font_silom_80.render(user_name, True, white)
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
        draw_centered_title_text('Better Bridge Game!', font_silom_80, white, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 10))

        multi_button = MenuButton("MULTIPLAYER", font_silom_75, (SCREEN_WIDTH//2, SCREEN_HEIGHT//3), True)
        single_button = MenuButton("SINGLE PLAYER", font_silom_75, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), True)
        setting_button = MenuButton("SETTINGS", font_silom_75, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + SCREEN_HEIGHT//6), True)
        quit_button = MenuButton("QUIT", font_silom_75, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + SCREEN_HEIGHT//3), True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or quit_button.check_click():
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
                draw_setting(board)
            pygame.display.flip()
    if board.getState == "QUIT":
        print("pygame quitted")
        pygame.display.quit()
        pygame.quit()
    print("MENU CLOSED")

gravity_time = 20
update_gravity = pygame.event.custom_type() + 1
def create_moving_cards(board):

    pygame.time.set_timer(update_gravity, gravity_time)

    hand_offset = (SCREEN_WIDTH - ((len(board.player1.hand) + 1) * (CARD_WIDTH * 2/3))) / 2
    loc_offset = 0
    for card in board.player1.hand:
        card.rect.x = (hand_offset + loc_offset*CARD_WIDTH * 2/3)
        card.rect = card.rect.inflate(0, HAND_Y)
        loc_offset += 1
def check_if_cards_move(event, board):
    for card in board.player1.hand:  
        if event.type == update_gravity:
            card.gravity_update()

def draw_gameplay(board):
    #Draw the background
    screen.fill(green)
    #Draw the player hand
    hand_offset = (SCREEN_WIDTH - ((len(board.player1.hand) + 1) * (CARD_WIDTH * 2 / 3))) / 2
    loc_offset = 0
    for card in board.player1.hand:       
        card.rect = screen.blit(card.image, (hand_offset + loc_offset*CARD_WIDTH * 2/3, HAND_Y))
        loc_offset += 1
    create_moving_cards(board)
    #Draw the pile
    draw_pile(screen, board.currentTrick)
    #Draw the trump suit
    draw_trump(screen, board.trumpSuit)
    #Draw the score (rounds won)
    if board.getState == "PLAYING":
        pygame.display.set_caption("Bridge Game [Playing...]")
        draw_scores(screen, board.teamOneScore, board.teamTwoScore, board.team_1_to_win, board.team_2_to_win)
        draw_your_turn(board.yourTurn)
    #Draw betting UI, if applicable
    elif board.getState == "BETTING":
        pygame.display.set_caption("Bridge Game [Betting...]")
        draw_bets(screen, board)
        update_betting_board(board)
        draw_your_turn(board.yourTurn)
    elif board.getState == "GAME_OVER":
        pygame.display.set_caption("Bridge Game [LeaderBoard]")
        draw_game_over_screen(board)
    elif board.gameMode == "MULTI" and board.getState != "QUIT":
        pygame.display.set_caption("Bridge Game [Setting Team...]")
        #SETUP TEAM IN BOARD
    elif board.gameMode == "SINGLE" and board.getState != "QUIT":
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
    img = pygame.image.load(glyph_path).convert_alpha()
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
    draw_centered_Text(f"Trump:", font_silom_30, black, (105, 20))
    #Glyph
    if (suit != BetSuit.LOW and suit != BetSuit.HIGH):
        img = get_glyph_from_suit(suit)
        draw_centered_Element(img, (105, 80))
    else:
        draw_centered_Text(f"{suit.name}", font_silom_40, black, (105, 80))
        
# todo increase border size so that team 1 and 2 can fit inside
def draw_scores(screen, score_1, score_2, team_1_to_win, team_2_to_win):
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
    draw_centered_Text(f"{str(score_1)} / {str(team_1_to_win)}" , font_silom_30, black, (272, 60)) #Text1
    draw_centered_Text(f"{str(score_2)} / {str(team_2_to_win)}", font_silom_30, black, (378, 60)) #Text2
    draw_centered_Text("Team 1", font_silom_30, black, (272, 20)) #Text1
    draw_centered_Text("Team 2", font_silom_30, black, (378, 20)) #Text2

def draw_game_over_screen(board):
   screen.fill(dark_red)
   font = font_silom_80
   font.set_underline(True)
   draw_centered_title_text("Game Over", font, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT//14))
   draw_centered_title_text(f"Team {str(board.winningTeam)} Wins!", font_silom_75, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT//5))
 
   font = font_silom_60
   font.set_underline(True)

   draw_centered_title_text("LeaderBoard:", font, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT//3))
   font.set_underline(False)
   leaderboard = sorted(board.players,key=lambda x: x.wins, reverse=True)
   time.sleep(0.5)
   buffer:int = 80
   for index, player in enumerate(leaderboard):
       draw_left_aligned_title_text(f"{str(index + 1)}. Team {1 if index % 2 == 0 else 2} - {str(player)}, SCORE: {str(player.wins)}", font_silom_40, white, (SCREEN_WIDTH//10 * 3, SCREEN_HEIGHT//3 + buffer))
       punch_sound.play()
       pygame.display.update()
       buffer += 80
       time.sleep(0.2)
   running = True
   while running:
       try_again_button = MenuButton("TRY AGAIN", font_silom_60, (SCREEN_WIDTH//3, SCREEN_HEIGHT-80), True)
       menu_button = MenuButton("MENU", font_silom_60, (SCREEN_WIDTH//3 * 2, SCREEN_HEIGHT-80), True)
       pygame.display.update()
       for event in pygame.event.get():
            if try_again_button.check_click():
                print("TRY AGAIN PRESSED")
                running = False
            elif menu_button.check_click():
                print("MENU CLICKED")
                board.getState = "MENU"
                running = False
            elif event.type == pygame.QUIT:
                board.getState = "QUIT"
                print("QUIT")
                running = False
#todo ensure that the indicator isn't updating when it doesn't need to
def draw_your_turn(isYourTurn: bool):
    """
    Draws a message on the screen indicating whether it's the player's turn or they are waiting.

    Args:
        isYourTurn (bool): True if it's the player's turn, False otherwise.
    """

    text = "Your Turn!" if isYourTurn else "Waiting..."
    draw_centered_title_text(text, font_silom_30, white, (SCREEN_WIDTH-115, 30))
    pygame.display.update()  # Update the entire display to show the new text

def update_betting_board(board):
    draw_current_bet(board.currentBetID)
    # todo Add other player's bet choices later

def draw_current_bet(currentBetID):
    betFactory = BetFactory()
    if currentBetID == -1:
        currentBet = None
    else:
        currentBet = betFactory.getBet(currentBetID)

    draw_centered_title_text(f"Current Bet: {currentBet}", font_silom_30, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT//20 * 5))
    pygame.display.flip()
    #player_positions = ((SCREEN_WIDTH//10, SCREEN_HEIGHT//2))
    #for player in board.players:


def user_choose_bets(board):
    print("User Choose ")
    betFactory = BetFactory()
    if board.currentBetID == -1:
        active_bet = Bet(BetSuit.LOW, 0)
    else:
        active_bet = betFactory.getBet(board.currentBetID)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                board.getState = "QUIT"
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #logic for handling player betting
                #Player clicks on a button corresponding to some bet
                #Then that bet is added using board.addBet
                #addBet checks for validity
                for button in size_bet_rects:
                    if button.rect.collidepoint(event.pos):
                        coin_sound.play()
                        print("Size Button Clicked")
                        new_bet = Bet(active_bet.suit, button.value)
                        active_bet = new_bet
                        print(active_bet)
                for button in suit_bet_rects:
                    if button.rect.collidepoint(event.pos):
                        coin_sound.play()
                        print("Suit Button Clicked")
                        new_bet = Bet(button.betsuit, active_bet.level)
                        active_bet = new_bet
                        print(active_bet)
                if submit_rect.collidepoint(event.pos):
                    success = board.addBet(active_bet)
                    if success:
                        print("Yippee")
                        running = False
                    else:
                        print("womp womp")
                        boing_sound.play()

                if pass_rect.collidepoint(event.pos):
                    if board.currentBetID != -1:
                        running = False
                        print("Passed")
                        board.addBet(Bet(None, None))
                    else:
                        boing_sound.play()
        draw_gameplay(board)
    print("USER STATE AFTER while loop for CHOOSING", board.getState)
#todo make a box class so that when the mouse clicks on one it gets hight
def draw_bets(screen, board):
    print("Draw bets called")
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
    draw_centered_Text("PASS", font_silom_30, black, (870,365))
    #Draw submit button
    border = submit_rect
    bgnd = pygame.Rect(740, 415, 170, 55)
    pygame.draw.rect(screen, black, border)
    pygame.draw.rect(screen, dark_red, bgnd)
    #Text
    draw_centered_Text("SUBMIT", font_silom_30, black, (825,442.5))

def draw_size_bet_box(screen, size, x, y):
    #Background
    border = pygame.Rect(x, y, 100, 100)
    bgnd = pygame.Rect(x + 10, y + 10, 80, 80)
    pygame.draw.rect(screen, black, border)
    pygame.draw.rect(screen, gray, bgnd)
    #Text
    draw_centered_Text(str(size), font_silom_30, black, (x+50,y+50))
    return BetButton(border, size, None)

def draw_suit_bet_box(screen, betsuit, x, y):
    #Background
    border = pygame.Rect(x, y, 100, 100)
    bgnd = pygame.Rect(x + 10, y + 10, 80, 80)
    pygame.draw.rect(screen, black, border)
    pygame.draw.rect(screen, gray, bgnd)
    #Contents
    if betsuit.value == 0:
        draw_centered_Text("LOW", font_silom_30, black, (x+50,y+50))
    elif betsuit.value == 5:
        draw_centered_Text("HIGH", font_silom_30, black,(x+50,y+50))
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
                board.getState = "QUIT"
                running = False
                tempCard = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if board.getState == "PLAYING":
                for card in board.players[0].hand:
                    card_rect = pygame.Rect(card.x, HAND_Y, CARD_WIDTH *2 / 3, CARD_HEIGHT)
                    if card_rect.collidepoint(event.pos) and not board.player1.isValidCardMove(card, board):
                        buzz_sound.play()
                    if card_rect.collidepoint(event.pos) and board.player1.isValidCardMove(card, board):
                        print(f"Clicked on  {str(card)}")
                        #self.player1.playCard(card, self)
                        tempCard = card
                        running = False
        if board.getState != "QUIT":
            draw_gameplay(board)
            board.yourTurn = False
    return tempCard
#Helper Functions
def create_centered_text(text: str, font, text_col: tuple, center: tuple):
    img = font.render(text, True, text_col)
    img_rect = img.get_rect(center = center)
    return (img, img_rect)
def draw_centered_Text(text: str, font, text_col: tuple, center: tuple):
    img = font.render(text, True, text_col)
    img_rect = img.get_rect(center = center)
    screen.blit(img, img_rect)

def draw_centered_Element(img, center: tuple):
    img_rect = img.get_rect(center= center)
    screen.blit(img, img_rect)

def draw_left_aligned_text(text: str, font, text_col: tuple, left: tuple):
    img = font.render(text, True, text_col)
    img_rect = img.get_rect(midleft = left)
    screen.blit(img, img_rect)

def draw_centered_title_text(text: str, font, text_col: tuple, center: tuple):
    draw_centered_Text(text, font, black, (center[0] + 4, center[1] + 4))
    draw_centered_Text(text, font, gray, (center[0] + 2, center[1] + 2))
    draw_centered_Text(text, font, text_col, center)

def draw_left_aligned_title_text(text: str, font, text_col: tuple, left: tuple):
    draw_left_aligned_text(text, font, black, (left[0] + 4, left[1] + 4))
    draw_left_aligned_text(text, font, gray, (left[0] + 2, left[1] + 2))
    draw_left_aligned_text(text, font, text_col, left)

class Text:
    def __init__(self, text: str, size: int, color: tuple, location: tuple, isCenter: bool = True) -> None:
        '''
        If isCenter is false, text will be aligned left
        '''
        self.text = str(text)
        self.color = color
        self.font = fonts[size]
        self.output = self.font.render(self.text, True, self.color)
        self.output_rect = self.output.get_rect(center = location) if isCenter else self.output.get_rect(midleft = location)
    def draw(self):
        screen.blit(self.output, self.output_rect)
class Title_Text:
    def __init__(self, text: str, size: int, location: tuple, isCenter: bool = True):
        self.text = text
        self.location = location
        self.font = fonts[size]

        self.main = self.font.render(self.text, True, white)
        self.shade = self.font.render(self.text, True, gray)
        self.shadow = self.font.render(self.text, True, black)

        self.surf = pygame.Surface(fonts[size].size(self.text), pygame.SRCALPHA, 32).convert_alpha()
        self.surf.blits([(self.shadow, (4, 4)),(self.shade, (2, 2)),(self.main, (0,0))], False)
        self.rect = self.surf.get_rect(center = location) if isCenter else self.surf.get_rect(midleft = location)
        
    def draw(self):
        screen.blit(self.surf, self.rect)
        

#todo Have it so that when players click on an illegal move. The outline appears with the sound effect
def draw_error_outline(image_rect: tuple, isInner: bool):
    pygame.draw.rect(screen, red, image_rect, 1)
class Button:
    def __init__(self, text: str, size: int, center: tuple,) -> None:
        self.text = text
        self.center = center
        self.text_img = Title_Text(text, size, center).surf
        self.size = self.text_img.get_size()
        self.outer = pygame.Surface((self.size[0] + 20, self.size[1] + 5))
        self.inner = pygame.Surface((self.size[0] + 10, self.size[1]))
        self.inner.set_colorkey(black)
        self.outer.set_colorkey(black)
        self.border = pygame.Surface((self.size[0] + 22, self.size[1] + 6))
        self.is_highlighted = False

        self.button_surf = pygame.Surface((self.size[0] + 50, self.size[1] + 50), pygame.SRCALPHA).convert_alpha()
        self.rect = self.button_surf.get_rect(center = self.center)
        self.button_rect = pygame.draw.rect(self.button_surf, pygame.SRCALPHA, self.button_surf.get_rect(center = self.center), 0, 15)
        self.is_clicked = False
        #self.button_rect = self.button_surf.get_rect(center = center)
        #self.button_surf.blits(self.text_image.)
    def draw(self):
        if self.is_highlighted:
            inner_color = light_red
        elif self.is_clicked:
            inner_color = dark_red
            self.is_clicked = False
        else:
            inner_color = red
        self.inner_rect = pygame.draw.rect(self.inner, inner_color, self.inner.get_rect(), 0, 15)
        self.outer_rect = pygame.draw.rect(self.outer, dark_red, self.outer.get_rect(), 0, 15)
        pygame.draw.rect(self.button_surf, black, self.border.get_rect(), 2, 15)
        self.button_surf.blits([(self.outer, self.outer_rect), (self.inner, self.inner_rect), (self.text_img, (5,5))] , False)
        screen.blit(self.button_surf, self.rect)
    def check_for_clicks(self):
        '''
        Call method after checking if mouse has been pressed down
        '''
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.is_clicked = True
            button_sound.play()
            return True
        return False
class MenuButton:
    def __init__(self, text: str, font, center: tuple, enabled: bool) -> None:
        self.text = text
        self.font = font
        self.center = center
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
            pygame.draw.rect(screen, red, self.shade_button, 0, 15, 15, 15, 15, 15)
        pygame.draw.rect(screen, black, self.outline, 2, 15, 15, 15, 15, 15)
        draw_centered_title_text(self.text, self.font, white, self.center)
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        buttonrect = self.outline
        if left_click and buttonrect.collidepoint(mouse_pos):
            self.draw(True)
            button_sound.play()
            time.sleep(0.8)
            return True
        else:
            self.draw(False)
            return False
        