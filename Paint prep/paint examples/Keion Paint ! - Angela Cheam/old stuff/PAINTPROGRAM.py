#PAINTCODEORDER! er. <pseudocode>
from pygame import*
screen=display.set_mode((1024,768))
lukaBackground=image.load("images/jbflukabg.png") 
screen.blit(lukaBackground,(0,0))

init()                                  # need init to initialize the mixer
mixer.music.load("songs/jbfmusicbox.mp3")       # load a MUSIC object
mixer.music.play()

canvasRect=Rect(329,100,677,572) #Canvas
#tools
musicRect=Rect(275,525,40,40)
pencilRect=Rect(330,690,60,60)
ballRect=Rect(550,10,40,40)
colourRect=Rect(7,598,253,164)
curtool="" #current tool
#if Pen
            #draw.circle(screen,(0,255,0),(mx,my),0)
            #copy=screen.copy()
        #if mb[0]==1 and omb[0]==1:
            #screen.blit(copy,(0,0))
            #draw.line(screen,(0,255,0),(omx,omy),(mx,my))
running=True
omb=mb=(0,0,0) 
mx,my=0,0
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
        if e.type==MOUSEBUTTONDOWN:
            back=screen.copy()
            screen.blit(back,(0,0))
            
    omx,omy=mx,my
    mx,my=mouse.get_pos()
    omb=mb
    mb=mouse.get_pressed()

    draw.rect(screen,(0,255,0),ballRect,2)
    musicPic=image.load("toolimages/play button.png")
    screen.blit(musicPic,(275,525))
    ballStamp=image.load("images/balloon.png")
    screen.blit(ballStamp,(550,10))

    draw.rect(screen,(255,0,0),pencilRect,2)
    if colourRect.collidepoint(mx,my):
        if mb[0]==1:
            drawColour=screen.get_at((mx,my))
            draw.rect(screen,drawColour,(0,0,50,50))
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),pencilRect,2)
    if ballRect.collidepoint(mx,my):
        if mb[0]==1:
            curStamp=balloon
            if curStamp=="balloon":
                if mb[0]==1:
                    balloonStamp=image.load("images/balloonfull.png")
                    screen.blit(balloonStamp,(mx,my))
    if musicRect.collidepoint(mx,my):
        musichoverPic=image.load("toolimages/play button hover.png")
        screen.blit(musichoverPic,(275,525))
        if mb[0]==1:
            musicpressedPic=image.load("toolimages/play button pressed.png")
            screen.blit(musicpressedPic,(275,525))

 
    display.flip()
quit()
