from pygame import *
from random import *
from math import *

#Screen------------------------------------
screen = display.set_mode((1001,700))
bgPic = image.load("images/bg.png")
screen.blit(bgPic,(0,0))

#Colours-----------------------------------
gold = ((200,149,45))
w = ((255,255,255))
y = ((255,213,70))

#Rects--------------------------------------
canvasRect = Rect(299,105,582,444)
paletteRect = Rect(13,518,161,169)
showcolourRect = Rect(184,496,96,101)

pencilRect = Rect(906,96,79,54)
eraserRect = Rect(906,157,79,53)
pickRect = Rect(906,217,79,54)
fillRect = Rect(906,277,79,54)

#Drawing Rects------------------------------
draw.rect(screen,w,canvasRect)
'''draw.rect(screen,c,showcolourRect)''' #MOVE AFTER COLOUR PICKER FOR PALETTE
draw.rect(screen,w,pencilRect)
draw.rect(screen,w,eraserRect)
draw.rect(screen,w,pickRect)
draw.rect(screen,w,fillRect)

#Image Loading------------------------------
canvasbPic = image.load("images/canvasborder.png")
palettePic = image.load("images/palette.png")
palettebPic = image.load("images/paletteborder.png")
sidePic = image.load("Images/sidepic.png")
titlePic = image.load("Images/title.png")
toolbPic = image.load("Images/toolborder.png")
tobPic = image.load("Images/tob.png")
stPic = image.load("Images/selectedtool.png")
overcolPic = image.load("Images/overcolourpick.png")


#Image Blits--------------------------------
screen.blit(canvasbPic,(0,0))
screen.blit(titlePic,(0,0))
screen.blit(sidePic,(0,0))
screen.blit(palettePic,(0,0))
screen.blit(palettebPic,(0,0))
screen.blit(toolbPic,(0,0))


mx,my = 0,0
start = 0,0
size = 10

#Music--------------------------------------
init()                                  
mixer.music.load("songs/Light.mp3")     
mixer.music.play()

#Event Loop---------------------------------
running =True
tool="pencil"
c=((0,0,0))
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            pic = screen.copy()
            if e.button == 1:
                start = e.pos
            if e.button == 4:
                size += 1
            if e.button == 5:
                size -= 1

    mb = mouse.get_pressed()    
    omx,omy=mx,my
    mx,my=mouse.get_pos()
    
#Palette Colour Picking-------------------
    if paletteRect.collidepoint(mx,my)and mb[0]==1:
        c = screen.get_at((mx,my))
    draw.rect(screen,c,showcolourRect)
    screen.blit(overcolPic,(184,496))        

#Button Selection-------------------------
    if pencilRect.collidepoint(mx,my):
        #draw.rect(screen,w,pencilRect)
        if mb[0]==1:
            #screen.blit(stPic,(906,96))
            tool="pencil"
        
    if eraserRect.collidepoint(mx,my):
        #draw.rect(screen,w,eraserRect)
        if mb[0]==1:
            tool="eraser"

    if pickRect.collidepoint(mx,my):
        #draw.rect(screen,w,fillRect)
        if mb[0]==1:
            tool="pick"
            
    if fillRect.collidepoint(mx,my):
        #draw.rect(screen,w,fillRect)
        if mb[0]==1:
            tool="fill"

#Drawing---------------------------------
    if canvasRect.collidepoint(mx,my) and mb[0]==1:
        screen.set_clip(canvasRect)
        if tool=="pick":            
            if canvasRect.collidepoint(mx,my)and mb[0]==1:
                c = screen.get_at((mx,my))
        if tool=="pencil":            
            draw.line(screen,c,(omx,omy),(mx,my),2)            
        if tool=="eraser":
            draw.circle(screen,w,(mx,my),size)
            #screen.blit(tobPic,(0,0))        
        if tool=="fill":
            draw.rect(screen,c,canvasRect)
            #screen.blit(tobPic,(0,0))           
        
   
    display.flip()
quit()
