from pygame import *

screen = display.set_mode((800,600))
forestPic = image.load("images/forest.jpg") 
screen.blit(forestPic,(0,0))
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
   
    mx,my = mouse.get_pos()
    c = screen.get_at((mx,my))
    draw.rect(screen,c,(0,0,50,50))
    display.flip()

quit()
