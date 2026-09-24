#pip install image for "PIL" module

import pygame
import random


from tkinter import *
from tkinter import messagebox

import os
import time

from PIL import ImageTk, Image

print(os.getcwd())


import time
import math

import user_interface
import scoreboard

# pygame.locals for easier access to key coordinates

import random



from pygame.locals import (

    RLEACCEL, #The RLEACCEL constant is an optional parameter that helps pygame render more quickly
            # on non-accelerated displays
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE

)

Game_Finished = False


username="Benny"

bg_index=0

DIR =os.getcwd()+r"/Full_game"
backgrounds = [DIR+"/clear_blue_sky.jpg",DIR+"/colourful.jpg",DIR+"/sci.jpg"]

# parameters:    bg_index,username

########################################
#Initialization of User Interface


user_interface.TKbox()

username = user_interface.username
bg_index = user_interface.bg_index

########################################

#######################################
#Initialization of User Attributes
#Name,Score,Health,Time,Exp,Level,Distance

score_system = scoreboard.score_system([])
if score_system.read_key(username).empty:
    EXP = 0 # 2 exps per enemies
    Level = 0 #Level-up algorithms =>Level bar
    Distance = 50 #Time times velocity(50m/s) => meter
else:
    df = score_system.read_key(username)
    EXP = int(df.iloc[-1]["Exp"])
    Level = int(df.iloc[-1]["Level"])
    Distance = 50


#Read data from sorted data base







#######################################
screen_width = 1366 # 800x600
screen_height = 720


pygame.init()

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("SkyWar")

score = 0

attack_damage = 30  #Damage to exert to player

#Pygame only support frame image and not support gif format photo



####### Initialization of Sound Effects
bg_musics = [DIR+"/resources/FFbgMusic.mp3",DIR+"/resources/Flying_me_softly.mp3"]
pygame.mixer.init()

#Background music

pygame.mixer.music.load(bg_musics[1])
pygame.mixer.music.play(loops=-1)


explosion_sound = pygame.mixer.Sound(DIR+"/resources/explosion.wav")
explosion_sound.set_volume(50)
shoot_sound = pygame.mixer.Sound(DIR+"/resources/shoot.wav")
shoot_sound.set_volume(50)
plane_move_sound = pygame.mixer.Sound(DIR+"/resources/airplane.mp3")
plane_move_sound.set_volume(50)

########









class player_health(pygame.sprite.Sprite):
    #self.surf=> what you see on screen       ,self.rect=>where you see on screen
    def __init__(self):
        super(player_health,self).__init__()
        # self.surf = pygame.image.load(DIR+"\Red_bar.png").convert()
        # self.surf = pygame.transform.scale(self.surf,(60,10))

        #self.surf = pygame.Surface([60,10]) #red bar
        #self.surf.fill((255, 0, 0))
        self.surf = pygame.Surface([60, 10])  # green bar
        self.surf.fill((0, 255, 0))

        self.rect = self.surf.get_rect()
        self.rect = pygame.rect.Rect((0,0),(60,10))
        self.scale_x = 60
        self.scale_y = 10
        self.image = pygame.Surface([self.scale_x,self.scale_y])
        self.image.fill((0, 255, 0))  # Faster for color rendering
        #self.surf.blit(self.image,(self.rect.left,self.rect.bottom))
        self.color_rgb = (0,255,0)


    def update(self,x=0,y=0,health_scale_x=60) -> None:
        if health_scale_x<30:
            self.color_rgb = (255,0,0)
        elif health_scale_x<36:
            self.color_rgb = (255,69,0)
        self.rect.bottom = y
        self.rect.left = x
        self.scale_x = health_scale_x
        self.image = pygame.Surface([self.scale_x, self.scale_y])
        self.image.fill(self.color_rgb)  # Faster for color rendering
        # self.surf.blit(self.image, (0, self.rect.bottom))
        self.surf = self.image



class Player(pygame.sprite.Sprite): #The class of character
    def __init__(self):
        super(Player, self).__init__()  #Change the player object into the object of py
        # This class will be superior to be run first in inheritance of class
        #self.surf = pygame.Surface((75, 25)) #it has a fixed resolution and pixel format
        #self.surf.fill((255, 255, 255))

        self.surf = pygame.image.load(DIR+"/jetfighter.png").convert()
        self.surf = pygame.transform.scale(self.surf,(60,30))
        #To scale the size of the sprite

        self.surf.set_colorkey((0,0,0),RLEACCEL)

        #self.surf.set_alpha(128)
        self.rect = self.surf.get_rect()
        self.rect = pygame.rect.Rect((0,screen_height/2), (10, 20))
        self.player_speed = 8





    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-self.player_speed )
            plane_move_sound.play()
            plane_move_sound.fadeout(500)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,self.player_speed )
            plane_move_sound.play()
            plane_move_sound.fadeout(500)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.player_speed ,0)
            plane_move_sound.play()
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.player_speed ,0)
            plane_move_sound.play()

        if self.rect.left<0: #e.g rect.left: 725   =>the edge point of the rectangle
            self.rect.left = 0
        if self.rect.right>screen_width:
            self.rect.right = screen_width
        if self.rect.top<0:
            self.rect.top = 0
        if self.rect.bottom >screen_height:
            self.rect.bottom = screen_height


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.surf = pygame.image.load(DIR+"/missile.png").convert()

        self.surf = pygame.transform.scale(self.surf,(80,20))
        self.surf = pygame.transform.rotate(self.surf,180)

        self.surf.set_colorkey((255,255,255),RLEACCEL)
        #set_colorkey to set the background colour the same with the game objects


        #Set the transparent colorkey set_colorkey(Color, flags=0)
        #pygame.RLEACCEL to provide better performance on non accelerated displays


        #self.surf = pygame.Surface((20,10))
        #self.surf.fill((255,255,255))

        self.rect =self.surf.get_rect(
            center =(
                random.randint(screen_width+20,screen_width+100),
                random.randint(0,screen_height),
            )


        )

        self.speed = random.randint(10,16)
        #To change the speed of the enemy
        #random float number 0 to 1 => random.random()

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right<0:
            self.kill() #From stopping the enemy to further be processed in spirit group
            pass


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud,self).__init__()
        self.surf = pygame.image.load(DIR+"/bad_cloud.png")
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.rect  = self.surf.get_rect(center=(random.randint(screen_width+20,screen_width+100),
                                           random.randint(0,screen_height)),
                                  )
        #The method get_rect() returns a Rect object from an image.
        #Collider Box

        self.surf= pygame.transform.scale(self.surf,(100,50))

        self.speed =random.randint(1,5)


    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right<0:
            self.kill()

class Bullet(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super(Bullet,self).__init__()
        self.surf = pygame.image.load(DIR+"/bullet.png")
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (60, 20))
        self.speed = random.randint(20,24)
        self.rect = self.surf.get_rect(
            center=(x,y),
        )

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right>screen_width+20:
            self.kill()
        #if self.rect.right < 0:
        #    self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Explosion, self).__init__()
        self.surf = pygame.image.load(DIR + "/explosion.png")
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # if x or y:
        self.x = x
        self.y = y
        # else:
        #     self.x = 0
        #     self.y = 0
        self.rect = self.surf.get_rect(center=(x,y),)
        # The method get_rect() returns a Rect object from an image.
        # Collider Box

        self.surf = pygame.transform.scale(self.surf, (120 , 60))

        self.speed = random.randint(1, 2)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < self.x-20:
            self.kill()






#Sprites creation area




health_bar = player_health()

player1 = Player()  # initialization of player1 object



bullets = pygame.sprite.Group()

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
explosion = pygame.sprite.Group()





all_sprites = pygame.sprite.Group()
#A container class to hold and manage multiple Sprite objects.
all_sprites.add(player1)

#For rendering game objects








running = True

ADDENEMY = pygame.USEREVENT+1
#The last event pygame reserves is called USEREVENT
pygame.time.set_timer(ADDENEMY,500) # every 250ms the time will give out a signal to instaniate enemies






ADDCLOUD = pygame.USEREVENT +2
pygame.time.set_timer(ADDCLOUD,4000)


clock = pygame.time.Clock()
#Setup the clock for a decent frame rate of the game
#print(backgrounds[1])
background = pygame.image.load(backgrounds[bg_index]) #DIR+"/clear_blue_sky.jpg")
background = pygame.transform.scale(background,(screen_width,screen_height ))


life = 60 #Total life of character
init_var = False

def rank_title():
    text_color = (128,0,0)
    head_font = pygame.font.SysFont(None, 40)
    text_surface = head_font.render("Player Ranking", True, text_color)
    screen.blit(text_surface, (screen_width / 2 - 100, 40))


def rank_item(name,SCORE,pos,rank_number):
    border_color = (255,0,0)
    pygame.draw.rect(screen,border_color,[0,0,screen_width,screen_height],width=10)
    pygame.display.flip()
    text_color = (128,0,0)  #(255,0,0)-red ,(128,0,0)-maroon
    rank_font = pygame.font.SysFont(None, 40) #head_font can only be used for one time rendering
    #name1 = head_font.render(name, True, text_color)
    #score1 = head_font.render(str(score), True, text_color)
    string = "{0}.".format(str(rank_number))+name+ "                    "+ "Score:" +str(SCORE)
    print(string)
    rank_string = rank_font.render(string,True,text_color)
    screen.blit(rank_string, (screen_width / 2-140, pos))





###############################################################################################################################################################















while running:

    Distance+=1
    print(Distance)
    font = pygame.font.SysFont("arial", 30, True)
    text = font.render("Score: " +str(score), 1, (0, 0, 0))
    # Arguments are: text, anti-aliasing, color => It is a surface object for blit
    user_text = font.render(username,1,(0,0,0))

    # pygame control the time message through event list
    # Joysticks will send events
    # after initialization of display module in pygame
    # and set display mode
    #screen.fill((135, 206, 250))  # (R,G,B) Backgroud

    screen.blit(background, (0, 0))

    ##Render the text Position
    screen.blit(user_text, (screen_width - 200, screen_height - 190))
    screen.blit(text, (screen_width - 200, screen_height - 150))

    if init_var:
        print("Welcome to Sky War.")
        init_var = False

    for event in pygame.event.get():
        # handling event queue => event handler
        # loc_x = screen_width / 2 + val_x
        # loc_y = screen_height / 2 + val_y

        if event.type == KEYDOWN:
            print("key down")
            if event.key == K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                bullet = Bullet(player1.rect.left, player1.rect.top)
                if bullet not in bullets:
                    bullets.add(bullet)
                    #all_sprites.add(bullet)
                    shoot_sound.set_volume(50)
                    shoot_sound.play()
                    shoot_sound.fadeout(1500) #In milliseconds
                    print("bullet")




        elif event.type == pygame.QUIT:
            # Event list
            running = False

        elif event.type == ADDENEMY:  #The signal to system for adding an enemy
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type ==ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)


    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)





    for bullet in bullets:
        screen.blit(bullet.surf, bullet.rect)
        for new_enemy in enemies:
            if pygame.sprite.spritecollideany(new_enemy, bullets):
                score +=1
                exp = Explosion(new_enemy.rect.right,new_enemy.rect.top)
                explosion.add(exp)
                explosion_sound.play()
                explosion_sound.fadeout(500)
                all_sprites.add(exp)
                new_enemy.kill()
                bullet.kill()
    for new_enemy in enemies:
        if pygame.sprite.collide_rect(player1,new_enemy): #Collide between two sprites
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

                Tk().wm_withdraw()  # To hide the main window
                messagebox.showinfo('Game Over', 'OK')
                running = False
                Game_Finished = True

    # if pygame.sprite.spritecollideany(player1,enemies): #Collide with enemies sprites group
    #     life-=1
    #     print(life)
    #     if life == 0:
    #         player1.kill()
    #         Tk().wm_withdraw() #To hide the main window
    #         messagebox.showinfo('Game Over','OK')
    #         running = False


    #screen.fill((0, 0, 0))
    screen.blit(player1.surf, player1.rect)
    # draw a surface on the background surface =>futures(low level callback asynchronious I/O)

    screen.blit(health_bar.surf,health_bar.rect)
    pressed_keys = pygame.key.get_pressed()


    player1.update(pressed_keys)

    health_bar.update(player1.rect.left,player1.rect.top,life) #Health_bar updates

    enemies.update()
    clouds.update()
    #If the player
    bullets.update()
    explosion.update()


    pygame.display.flip()
    clock.tick(40) #Maintain the speed of game at 40 frames per second


    #flip() =>update the whole display     vs update() => can update the specific area with argument


#######################################################
#Scoring System OUTPUT


#Name,Score,Health,Time,Exp,Level,Distance
#username,score,life,T,EXP,Level,Distance

T = time.asctime(time.localtime(time.time()))
if Game_Finished== True:#Only Game is finished but not closed, EXP will be added on to player
    EXP+=random.randint(1,26) #1 to 25 exp.
else:
    EXP+=0
score_system.write([username,score,life,T,EXP,Level,Distance,bg_index])
#Scoreboard
rank_number = 1

rank_title()
DF =  score_system.read_database()
rank_info = []
pos = 80


for j in DF.nlargest(10, "Score")[["Name", "Score"]].values:
    #For record
    rank_info.append([j[0],j[1]]) #[player_name,player_score]
    rank_item(str(j[0]), j[1], pos, rank_number)
    rank_number+=1
    pos+=60
    pre_string = str(j[0])
#rank_item(username,score,80,rank_number)
print(username)
print(score)
pygame.display.update()




######################################################



while True:
    for event in pygame.event.get():
        if event.type == QUIT or event.type == K_ESCAPE:
            print("Exit!")
            pygame.quit()
            sys.exit()






#Collision detection checks if the spirit object .rect collides with .rect of another object


#all_sprites =>add player1,enemies and clouds for rendering and instantiation
"""
player1 => player object and function
enemies =>enemies collision detection and positioning
clouds => positioning



"""


"""
Rendering is done using all_sprites.
Position updates are done using clouds and enemies.
Collision detection is done using enemies.

"""