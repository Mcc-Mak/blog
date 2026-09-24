"""SkyWar: a side-scrolling arcade shooter built with pygame.

The player picks a username and background in a tkinter UI, then shoots
incoming enemies while a live scoreboard is shown on exit.
"""
# pip install pillow  # provides the "PIL" module

import pygame
import random

from tkinter import *
from tkinter import messagebox

import os
import time

from PIL import ImageTk, Image

print(os.getcwd())

import math

import user_interface
import scoreboard

# pygame.locals for easier access to key coordinates

from pygame.locals import (
    RLEACCEL,  # optional flag that speeds up rendering on slow displays
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
)

Game_Finished = False  # True once the player loses all health

username = "Benny"  # default name until the UI overwrites it

bg_index = 0

DIR = os.getcwd()+r"/Full_game"
backgrounds = [DIR+"/clear_blue_sky.jpg", DIR+"/colourful.jpg", DIR+"/sci.jpg"]

# --- Initialization of the User Interface ---
# parameters: bg_index, username

user_interface.TKbox()

username = user_interface.username
bg_index = user_interface.bg_index

# --- Initialization of User Attributes ---
# Name, Score, Health, Time, Exp, Level, Distance

score_system = scoreboard.score_system([])
if score_system.read_key(username).empty:
    EXP = 0  # 2 exp per enemy shot down
    Level = 0  # level-up algorithms => level bar
    Distance = 50  # time x velocity(50m/s) => meters
else:
    df = score_system.read_key(username)
    EXP = int(df.iloc[-1]["Exp"])
    Level = int(df.iloc[-1]["Level"])
    Distance = 50

# --- Pygame setup (window and display) ---

screen_width = 1366  # 800x600
screen_height = 720

pygame.init()

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("SkyWar")

score = 0

attack_damage = 30  # damage dealt to the player per hit

# pygame only renders still images, not gif frames

# --- Sound Effects ---

bg_musics = [DIR+"/resources/FFbgMusic.mp3", DIR+"/resources/Flying_me_softly.mp3"]
pygame.mixer.init()

# Background music
pygame.mixer.music.load(bg_musics[1])
pygame.mixer.music.play(loops=-1)

explosion_sound = pygame.mixer.Sound(DIR+"/resources/explosion.wav")
explosion_sound.set_volume(50)
shoot_sound = pygame.mixer.Sound(DIR+"/resources/shoot.wav")
shoot_sound.set_volume(50)
plane_move_sound = pygame.mixer.Sound(DIR+"/resources/airplane.mp3")
plane_move_sound.set_volume(50)


# --- Sprite classes ---
# self.surf => what you see on screen, self.rect => where you see it on screen


class player_health(pygame.sprite.Sprite):
    """Green health bar rendered above the player's ship."""

    def __init__(self):
        super(player_health, self).__init__()
        # self.surf = pygame.image.load(DIR+"\Red_bar.png").convert()
        # self.surf = pygame.transform.scale(self.surf,(60,10))

        # self.surf = pygame.Surface([60,10])  # red bar
        # self.surf.fill((255, 0, 0))
        self.surf = pygame.Surface([60, 10])  # green bar
        self.surf.fill((0, 255, 0))

        self.rect = self.surf.get_rect()
        self.rect = pygame.rect.Rect((0, 0), (60, 10))
        self.scale_x = 60
        self.scale_y = 10
        self.image = pygame.Surface([self.scale_x, self.scale_y])
        self.image.fill((0, 255, 0))  # faster for color rendering
        # self.surf.blit(self.image,(self.rect.left,self.rect.bottom))
        self.color_rgb = (0, 255, 0)

    def update(self, x=0, y=0, health_scale_x=60) -> None:
        # Color shifts from green to orange/red as health drops
        if health_scale_x < 30:
            self.color_rgb = (255, 0, 0)
        elif health_scale_x < 36:
            self.color_rgb = (255, 69, 0)
        self.rect.bottom = y
        self.rect.left = x
        self.scale_x = health_scale_x
        self.image = pygame.Surface([self.scale_x, self.scale_y])
        self.image.fill(self.color_rgb)  # faster for color rendering
        # self.surf.blit(self.image, (0, self.rect.bottom))
        self.surf = self.image


class Player(pygame.sprite.Sprite):  # The player's fighter jet
    def __init__(self):
        super(Player, self).__init__()  # initialize the pygame sprite first
        # self.surf = pygame.Surface((75, 25))  # fixed resolution & pixel format
        # self.surf.fill((255, 255, 255))

        self.surf = pygame.image.load(DIR+"/jetfighter.png").convert()
        self.surf = pygame.transform.scale(self.surf, (60, 30))  # rescale the sprite
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        # self.surf.set_alpha(128)
        self.rect = self.surf.get_rect()
        self.rect = pygame.rect.Rect((0, screen_height / 2), (10, 20))
        self.player_speed = 8

    def update(self, pressed_keys):
        # Move in the pressed direction and play the engine sound
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.player_speed)
            plane_move_sound.play()
            plane_move_sound.fadeout(500)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.player_speed)
            plane_move_sound.play()
            plane_move_sound.fadeout(500)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.player_speed, 0)
            plane_move_sound.play()
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.player_speed, 0)
            plane_move_sound.play()

        # Keep the ship inside the screen edges
        if self.rect.left < 0:  # rect.left is the left edge of the rectangle
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(DIR+"/missile.png").convert()
        self.surf = pygame.transform.scale(self.surf, (80, 20))
        self.surf = pygame.transform.rotate(self.surf, 180)

        # set_colorkey makes the given background color transparent
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        # self.surf = pygame.Surface((20,10))
        # self.surf.fill((255,255,255))

        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen_width + 20, screen_width + 100),
                random.randint(0, screen_height),
            )
        )

        self.speed = random.randint(10, 16)  # random enemy speed
        # random.random() gives a float in [0, 1]

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()  # stop processing enemies that left the screen


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load(DIR+"/bad_cloud.png")
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=(random.randint(screen_width + 20, screen_width + 100),
                                               random.randint(0, screen_height)),
                                       )
        # get_rect() returns a Rect object from an image (the collision box)
        self.surf = pygame.transform.scale(self.surf, (100, 50))
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        self.surf = pygame.image.load(DIR+"/bullet.png")
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (60, 20))
        self.speed = random.randint(20, 24)
        self.rect = self.surf.get_rect(
            center=(x, y),
        )

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right > screen_width + 20:
            self.kill()
        # if self.rect.right < 0:
        #     self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Explosion, self).__init__()
        self.surf = pygame.image.load(DIR + "/explosion.png")
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect(center=(x, y),)
        # get_rect() returns a Rect object from an image (the collision box)
        self.surf = pygame.transform.scale(self.surf, (120, 60))
        self.speed = random.randint(1, 2)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < self.x - 20:
            self.kill()


# --- Sprites creation area ---

health_bar = player_health()

player1 = Player()  # initialization of the player1 object

bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
explosion = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
# A container class to hold and manage multiple Sprite objects.
all_sprites.add(player1)  # used for rendering all game objects
#For rendering game objects


# --- Timer events (spawn enemies and clouds) ---

running = True

ADDENEMY = pygame.USEREVENT + 1
# The last event pygame reserves is called USEREVENT
pygame.time.set_timer(ADDENEMY, 500)  # spawn a new enemy every 500ms

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 4000)  # spawn a new cloud every 4s

clock = pygame.time.Clock()
#Setup the clock for a decent frame rate of the game
background = pygame.image.load(backgrounds[bg_index])
background = pygame.transform.scale(background, (screen_width, screen_height))

life = 60  # total life of the character
init_var = False

# --- Rank display helpers (shown after the game ends) ---


def rank_title():
    text_color = (128, 0, 0)
    head_font = pygame.font.SysFont(None, 40)
    text_surface = head_font.render("Player Ranking", True, text_color)
    screen.blit(text_surface, (screen_width / 2 - 100, 40))


def rank_item(name, SCORE, pos, rank_number):
    border_color = (255, 0, 0)
    pygame.draw.rect(screen, border_color, [0, 0, screen_width, screen_height], width=10)
    pygame.display.flip()
    text_color = (128, 0, 0)  # (255,0,0)=red, (128,0,0)=maroon
    rank_font = pygame.font.SysFont(None, 40)  # a font object is rendered only once
    #name1 = head_font.render(name, True, text_color)
    #score1 = head_font.render(str(score), True, text_color)
    string = "{0}.".format(str(rank_number)) + name + "                    " + "Score:" + str(SCORE)
    print(string)
    rank_string = rank_font.render(string, True, text_color)
    screen.blit(rank_string, (screen_width / 2 - 140, pos))


# --- Main loop ---


while running:

    Distance += 1
    print(Distance)
    font = pygame.font.SysFont("arial", 30, True)
    text = font.render("Score: " + str(score), 1, (0, 0, 0))
    # font.render arguments: text, anti-aliasing, color => a surface for blit
    user_text = font.render(username, 1, (0, 0, 0))

    # pygame manages timing through the event list; joysticks also post events
    # after the display module is initialized and the display mode is set
    # screen.fill((135, 206, 250))  # (R,G,B) background

    screen.blit(background, (0, 0))

    # Render the text positions
    screen.blit(user_text, (screen_width - 200, screen_height - 190))
    screen.blit(text, (screen_width - 200, screen_height - 150))

    if init_var:
        print("Welcome to Sky War.")
        init_var = False

    for event in pygame.event.get():
        # Handling the event queue => event handler
        if event.type == KEYDOWN:
            print("key down")
            if event.key == K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                bullet = Bullet(player1.rect.left, player1.rect.top)
                if bullet not in bullets:
                    bullets.add(bullet)
                    # all_sprites.add(bullet)
                    shoot_sound.set_volume(50)
                    shoot_sound.play()
                    shoot_sound.fadeout(1500)  # fade out over 1.5s
                    print("bullet")

        elif event.type == pygame.QUIT:
            running = False

        elif event.type == ADDENEMY:  # signal to spawn a new enemy
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # Draw every sprite in the world
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Bullet vs enemy collisions => +1 score and an explosion effect
    for bullet in bullets:
        screen.blit(bullet.surf, bullet.rect)
        for new_enemy in enemies:
            if pygame.sprite.spritecollideany(new_enemy, bullets):
                score += 1
                exp = Explosion(new_enemy.rect.right, new_enemy.rect.top)
                explosion.add(exp)
                explosion_sound.play()
                explosion_sound.fadeout(500)
                all_sprites.add(exp)
                new_enemy.kill()
                bullet.kill()

    # Player vs enemy collisions => lose health; game over at zero life
    for new_enemy in enemies:
        if pygame.sprite.collide_rect(player1, new_enemy):
            explosion_sound.play()
            exp = Explosion(new_enemy.rect.right, new_enemy.rect.top)
            explosion.add(exp)
            all_sprites.add(exp)
            new_enemy.kill()
            life -= attack_damage
            print(life)
            if life == 0:
                player1.kill()
                pygame.mixer.music.stop()
                pygame.mixer.quit()

                Tk().wm_withdraw()  # hide the main window
                messagebox.showinfo('Game Over', 'OK')
                running = False
                Game_Finished = True

    # screen.fill((0, 0, 0))
    screen.blit(player1.surf, player1.rect)
    screen.blit(health_bar.surf, health_bar.rect)
    pressed_keys = pygame.key.get_pressed()

    player1.update(pressed_keys)
    health_bar.update(player1.rect.left, player1.rect.top, life)  # health bar follows the ship

    enemies.update()
    clouds.update()
    bullets.update()
    explosion.update()

    pygame.display.flip()
    clock.tick(40)  # maintain the game at 40 frames per second

    # flip() updates the whole display; update() refreshes a specific area

# --- Scoring system output (write the result + show the leaderboard) ---
# columns: Name, Score, Health, Time, Exp, Level, Distance

T = time.asctime(time.localtime(time.time()))
if Game_Finished == True:  # EXP only grows when a game is finished
    EXP += random.randint(1, 26)  # 1 to 25 exp.
else:
    EXP += 0
score_system.write([username, score, life, T, EXP, Level, Distance, bg_index])

# Show the top-10 leaderboard
rank_number = 1
rank_title()
DF = score_system.read_database()
rank_info = []
pos = 80

for j in DF.nlargest(10, "Score")[["Name", "Score"]].values:
    rank_info.append([j[0], j[1]])  # [player_name, player_score]
    rank_item(str(j[0]), j[1], pos, rank_number)
    rank_number += 1
    pos += 60
    pre_string = str(j[0])
print(username)
print(score)
pygame.display.update()

# --- Idle loop: wait for the user to close the ranking window ---

while True:
    for event in pygame.event.get():
        if event.type == QUIT or event.type == K_ESCAPE:
            print("Exit!")
            pygame.quit()
            sys.exit()


# Collision detection checks whether one sprite's .rect overlaps another's.
#
# all_sprites => renders and manages player1, enemies and clouds
# player1     => player object and functions
# enemies     => collision detection and positioning
# clouds      => positioning

"""
Rendering is done using all_sprites.
Position updates are done using clouds and enemies.
Collision detection is done using enemies.
"""