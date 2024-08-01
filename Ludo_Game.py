import pygame
import random

pygame.init()

running = True
screen = pygame.display.set_mode((550, 550))
pygame.display.set_caption("Ludo Game")
icon = pygame.image.load("PYGAME_Assignment\\project.png")
pygame.display.set_icon(icon)

floor = pygame.image.load("PYGAME_Assignment\\ludo_board.gif")
piece_yellow = pygame.image.load("PYGAME_Assignment\\yellow.png")
piece_blue = pygame.image.load("PYGAME_Assignment\\blue.png")
piece_red = pygame.image.load("PYGAME_Assignment\\red.png")
dice_list = [pygame.image.load(f"PYGAME_Assignment\\Dice_{i}.jpg") for i in range(1, 7)]

piece_listy = [(135, 450), (227, 470), (227, 435), (227, 400), (227, 365), (227, 330), (192, 295), (157, 295),
               (122, 295), (87, 295), (52, 295), (17, 295), (17, 260), (17, 225), (52, 225), (87, 225), (122, 225),
               (157, 225), (192, 225), (227, 190), (227, 155), (227, 120), (227, 85), (227, 50), (227, 15), (262, 15),
               (297, 15), (297, 50), (297, 85), (297, 120), (297, 155), (297, 190), (332, 225), (367, 225), (402, 225),
               (437, 225), (472, 225), (507, 225), (507, 260), (507, 295), (472, 295), (437, 295), (402, 295), (367, 295),
               (332, 295), (297, 330), (297, 365), (297, 400), (297, 435), (297, 470), (297, 505), (262, 505), (262, 470),
               (262, 435), (262, 400), (262, 365), (262, 330), (262, 295)]
piece_listb = [(75, 130), (52, 225), (87, 225), (122, 225), (157, 225), (192, 225), (227, 190), (227, 155), (227, 120),
               (227, 85), (227, 50), (227, 15), (262, 15), (297, 15), (297, 50), (297, 85), (297, 120), (297, 155),
               (297, 190), (332, 225), (367, 225), (402, 225), (437, 225), (472, 225), (507, 225), (507, 260), (507, 295),
               (472, 295), (437, 295), (402, 295), (367, 295), (332, 295), (297, 330), (297, 365), (297, 400), (297, 435),
               (297, 470), (297, 505), (262, 505), (227, 505), (227, 470), (227, 435), (227, 400), (227, 365), (227, 330),
               (192, 295), (157, 295), (122, 295), (87, 295), (52, 295), (17, 295), (17, 260), (52, 260), (87, 260),
               (122, 260), (157, 260), (192, 260), (227, 260)]
piece_listr = [(392, 70), (297, 50), (297, 85), (297, 120), (297, 155), (297, 190), (332, 225), (367, 225), (402, 225),
               (437, 225), (472, 225), (507, 225), (507, 260), (507, 295), (472, 295), (437, 295), (402, 295), (367, 295),
               (332, 295), (297, 330), (297, 365), (297, 400), (297, 435), (297, 470), (297, 505), (262, 505), (227, 505),
               (227, 470), (227, 435), (227, 400), (227, 365), (227, 330), (192, 295), (157, 295), (122, 295), (87, 295),
               (52, 295), (17, 295), (17, 260), (17, 225), (52, 225), (87, 225), (122, 225), (157, 225), (192, 225),
               (227, 190), (227, 155), (227, 120), (227, 85), (227, 50), (227, 15), (262, 15), (262, 50), (262, 85),
               (262, 120), (262, 155), (262, 190), (262, 225)]

turn = "Yellow Turn"
font = pygame.font.Font("freesansbold.ttf", 24)
over_font = pygame.font.Font("freesansbold.ttf", 64)
blastimg = pygame.image.load("PYGAME_Assignment\\flame.png")
last_turn = " "

pieces = {
    "yellow": {"state": "in", "position": 0, "initial": (135, 450)},
    "blue": {"state": "in", "position": 0, "initial": (75, 130)},
    "red": {"state": "in", "position": 0, "initial": (392, 70)},
}

def background(x, y):
    screen.blit(floor, (x, y))

def dice(a):
    screen.blit(dice_list[a - 1], (245, 245))

def show_piece(color, pos):
    piece_images = {"yellow": piece_yellow, "blue": piece_blue, "red": piece_red}
    coords = {"yellow": piece_listy, "blue": piece_listb, "red": piece_listr}
    screen.blit(piece_images[color], coords[color][pos])

def show_turn(text):
    turn_text = font.render(text, True, (255, 255, 255))
    screen.blit(turn_text, (40, 15))

def move_piece(color, roll):
    piece_data = pieces[color]
    if piece_data["state"] == "in":
        if roll == 6:
            piece_data["state"] = "out"
            piece_data["position"] = 0
    else:
        piece_data["position"] += roll
        if piece_data["position"] > len(piece_listy) - 1:
            piece_data["position"] = len(piece_listy) - 1
        
        # Check for collisions
        for other_color, other_data in pieces.items():
            if other_color != color and other_data["state"] == "out" and other_data["position"] == piece_data["position"]:
                
                other_data["state"] = "in"
                other_data["position"] = 0

def iscollision(color, pos):
    piece_data = pieces[color]
    for other_color, other_data in pieces.items():
        if other_color != color and other_data["state"] == "out" and other_data["position"] == pos:
            return True
    return False

def game_over():
    if pieces["yellow"]["position"] == len(piece_listy) - 1 or \
       pieces["blue"]["position"] == len(piece_listb) - 1 or \
       pieces["red"]["position"] == len(piece_listr) - 1:
        game_over_text = over_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over_text, (80, 250))
        return True
    return False

def handle_turn():
    global turn
    if turn == "Yellow Turn":
        move_piece("yellow", roll)
        turn = "Blue Turn" if roll != 6 else "Yellow Turn"
    elif turn == "Blue Turn":
        move_piece("blue", roll)
        turn = "Red Turn" if roll != 6 else "Blue Turn"
    elif turn == "Red Turn":
        move_piece("red", roll)
        turn = "Yellow Turn" if roll != 6 else "Red Turn"

roll = 0
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                roll = random.randint(1, 6)
                last_turn = turn
                handle_turn()

    background(0, 0)
    screen.blit(blastimg, (84, 295))
    screen.blit(blastimg, (294, 435))
    screen.blit(blastimg, (224, 82))
    screen.blit(blastimg, (437, 225))

    show_turn(turn)
    if roll != 0:
        dice(roll)

    for color, data in pieces.items():
        show_piece(color, data["position"])

    if game_over():
        turn = "No Turn"

    pygame.display.update()

pygame.quit()
