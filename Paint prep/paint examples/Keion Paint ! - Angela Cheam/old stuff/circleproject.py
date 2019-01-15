#circleProject
from pygame import *
screen=display.set_mode((1024,768))
running=True
colour=(0,255,0)

while running:
    for evt in event.get():
        omx,omy=(0,0)
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        omx,omy=mx,my
        omb=(0,0,0)
        if evt.type==QUIT:
            running=False
        if mb[0]==1 and omb[0]==1:
            draw.line(screen,colour,(omx,omy),(mx,my))
    display.flip()
quit()
