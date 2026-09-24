# import pygame
# import sys
# from pygame.locals import QUIT
#
# username = "Benny"
# score = 20
#
#
#
#
# pygame.init()
# width = 1000
# height = 800
# screen = pygame.display.set_mode((width,height))
# pygame.display.set_caption("Game Board")
#
# screen.fill((0,255,0))
#
# text_color = (10,10,10)
#
# head_font = pygame.font.SysFont(None,40)
# text_surface  = head_font.render("Players Ranking",True,text_color) #RGB value
# screen.blit(text_surface,(width/2-80,10))
# name1 = head_font.render(username,True,text_color)
# screen.blit(name1,(width/2-120,60))
# score1 = head_font.render(str(score),True,text_color)
# screen.blit(score1,(width/2+120,60))
#
# #Frame
# surf = pygame.Surface((width-20,height-20),pygame.SRCALPHA)
# pygame.draw.rect(surf,text_color,(20,20,width-80,height-80))
# screen.blit(surf,(20,20))
#
#
#
#
# pygame.display.update()
# while True:
#     # 迭代整個事件迴圈，若有符合事件則對應處理
#     for event in pygame.event.get():
#         # 當使用者結束視窗，程式也結束
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()


number = str(5)
print(type("{}.".format(number)))