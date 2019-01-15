#balloon test
from pygame import *

screen = display.set_mode((1024,768))
balloonStamp=image.load("images/balloonfull.png")
screen.fill((255,255,255))
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type==MOUSEBUTTONDOWN:
            back=screen.copy()
            screen.blit(back,(0,0))
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()

    if mb[0]==1:
        screen.blit(back,(0,0))
        screen.blit(balloonStamp, (mx,my))
    display.flip()

quit()
