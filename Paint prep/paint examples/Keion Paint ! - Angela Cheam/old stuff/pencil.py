from pygame import *
screen=display.set_mode((1024,768))
init()                                  # need init to initialize the mixer
mixer.music.load("songs/sweetholiday.mp3")       # load a MUSIC object
mixer.music.play()
running=True
omb=mb=(0,0,0)
mx,my=0,0
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    omx,omy=mx,my
    mx,my=mouse.get_pos()
    omb=mb
    mb=mouse.get_pressed()
    if mb[0]==1:
        draw.circle(screen,(0,255,0),(mx,my),0)
        copy=screen.copy()
    if mb[0]==1 and omb[0]==1:
        screen.blit(copy,(0,0))
        draw.line(screen,(0,255,0),(omx,omy),(mx,my))
    display.flip()
quit()
