from pygame import *
from random import *
from math import *
    
pencilRect = Rect(20,80,40,40)
eraserRect = Rect(67,80,40,40)
bucketRect = Rect(20,127,40,40)
rectRect = Rect(67,127,40,40)
lineRect = Rect(20,174,40,40)
paletteRect = Rect(129,570,200,200)
canvasRect = Rect(130,80,740,480)
                        #630
#Stamps-------------------------------------                      
jackRect = Rect(791,570,70,200)
bunnyRect = Rect(411,570,70,200)
sandRect = Rect(487,570,70,200)
toothRect = Rect(563,570,70,200)
northRect = Rect(639,570,70,200)
pitchRect = Rect(715,570,70,200)
#-------------------------------------------                      

screen = display.set_mode((1000,780))
#screen.fill((20,20,100))
w=((255,255,255))
g=((190,190,190))

pencilPic = image.load("images/pencil.png")
eraserPic = image.load("images/eraser.png")
rotgBG = image.load("images/Rotg Flakes.jpg")
#rotgfooter = image.load("images/rotgfooter.png")
palettePic = image.load("images/palette2.png")

#Chara Pics---------------------------------
jackPic = image.load("images/jack3.png")
bunnyPic = image.load("images/bunny2.png")
sandPic = image.load("images/sandman2.png")
toothPic = image.load("images/tooth2.png")
northPic = image.load("images/north2.png")
pitchPic = image.load("images/pitch2.png")
#-------------------------------------------

screen.blit(rotgBG,(0,0))
#screen.blit(rotgfooter,(420,570))
screen.blit(palettePic,(129,570))

mx,my = 0,0
draw.rect(screen,w,canvasRect)
start = 0,0
size = 28
#Music--------------------------------------
init()                                  
mixer.music.load("songs/Wind.mp3")     
mixer.music.play() 
#-------------------------------------------
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
    #draw.rect(screen,(0,0,0),(0,0,70,70))
    '''if paletteRect.collidepoint(mx,my):
        c = screen.get_at((mx,my))
    draw.rect(screen,c,(335,570,70,70))'''
    if paletteRect.collidepoint(mx,my)and mb[0]==1:
        c = screen.get_at((mx,my))
    draw.rect(screen,c,(335,570,70,70))
#Stamps-----------------------------------
    draw.rect(screen,w,jackRect)
    draw.rect(screen,w,bunnyRect)
    draw.rect(screen,w,sandRect)
    draw.rect(screen,w,toothRect)
    draw.rect(screen,w,northRect)
    draw.rect(screen,w,pitchRect)
#Tools------------------------------------
    draw.rect(screen,w,pencilRect)
    screen.blit(pencilPic,(24,80))    
    draw.rect(screen,w,eraserRect)
    screen.blit(eraserPic,(67,84))    
    draw.rect(screen,w,bucketRect)                
    draw.rect(screen,w,rectRect)
    draw.rect(screen,w,lineRect)
    
#Outlines---------------------------------    
    draw.rect(screen,g,pencilRect,2)
    draw.rect(screen,g,eraserRect,2)    
    draw.rect(screen,g,bucketRect,2)
    draw.rect(screen,g,rectRect,2)
    draw.rect(screen,g,lineRect,2)

    draw.rect(screen,g,jackRect,2)
    draw.rect(screen,g,bunnyRect,2)
    draw.rect(screen,g,sandRect,2)
    draw.rect(screen,g,toothRect,2)
    draw.rect(screen,g,northRect,2)
    draw.rect(screen,g,pitchRect,2)
#Button Selection-------------------------
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,w,pencilRect)
        if mb[0]==1:
            tool="pencil"
        
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,w,eraserRect)
        if mb[0]==1:
            tool="eraser"
            
    if bucketRect.collidepoint(mx,my):
        draw.rect(screen,w,bucketRect)
        if mb[0]==1:
            tool="bucket"
            
    if rectRect.collidepoint(mx,my):
        draw.rect(screen,w,rectRect)
        if mb[0]==1:
            tool="rect"

    if lineRect.collidepoint(mx,my):
        draw.rect(screen,w,lineRect)
        if mb[0]==1:
            tool="line"
#Stamp Selection-------------------------
    if jackRect.collidepoint(mx,my):
        draw.rect(screen,w,jackRect)
        if mb[0]==1:
            tool="jack"
    if bunnyRect.collidepoint(mx,my):
        draw.rect(screen,w,bunnyRect)
        if mb[0]==1:
            tool="bunny"
    if sandRect.collidepoint(mx,my):
        draw.rect(screen,w,sandRect)
        if mb[0]==1:
            tool="sand"
    if toothRect.collidepoint(mx,my):
        draw.rect(screen,w,toothRect)
        if mb[0]==1:
            tool="tooth"
    if northRect.collidepoint(mx,my):
        draw.rect(screen,w,northRect)
        if mb[0]==1:
            tool="north"
    if pitchRect.collidepoint(mx,my):
        draw.rect(screen,w,pitchRect)
        if mb[0]==1:
            tool="pitch"
#Drawing---------------------------------
    #if paletteRect.collidepoint(mx,my) and mb[0]==1:
        #c = screen.get_at((mx,my))
        
    if canvasRect.collidepoint(mx,my) and mb[0]==1:
        screen.set_clip(canvasRect)
        if tool=="pencil":
            draw.line(screen,c,(omx,omy),(mx,my),2)
        if tool=="eraser":
            draw.circle(screen,w,(mx,my),size)
        #if tool=="bucket":
            #fill.canvasRect(w)
        if tool=="rect":
            #if e.type == MOUSEBUTTONDOWN:
            draw.polygon(screen,c,[[omx,omy],[mx,omy],[mx,my],[omx,my]],2)
        '''if mb[2]==1:
            screen.fill(1,1,1) ----> "invalid recstyle object"'''
        if tool=="line":
            #have to have some type of screen fill
            draw.line(screen,c, start,(mx,my), size)
            
        if tool=="jack":
            screen.blit(pic,(0,0))
            screen.blit(jackPic,(mx-60,my-105))
        if tool=="bunny":
            screen.blit(pic,(0,0))
            screen.blit(bunnyPic,(mx-62,my-117))
        if tool=="sand":
            screen.blit(pic,(0,0))
            screen.blit(sandPic,(mx-107,my-107))
        if tool=="tooth":
            screen.blit(pic,(0,0))
            screen.blit(toothPic,(mx-115,my-115))
        if tool=="north":
            screen.blit(pic,(0,0))
            screen.blit(northPic,(mx-82,my-120))
        if tool=="pitch":
            screen.blit(pic,(0,0))
            screen.blit(pitchPic,(mx-92,my-123))
                    
        screen.set_clip(None)
#----------------------
        
    display.flip()


quit()
