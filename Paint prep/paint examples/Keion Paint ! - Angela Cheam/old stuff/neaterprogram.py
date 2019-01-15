#neater
from pygame import*
screen=display.set_mode((1024,768))
lukaBackground=image.load("images/jbflukabg.png") 
screen.blit(lukaBackground,(0,0))

music=True
if music==True:
    init()                                  # need init to initialize the mixer
    mixer.music.load("songs/jbfmusicbox.mp3")       # load a MUSIC object
    mixer.music.play()
play=0

canvasRect=Rect(329,100,677,572) #Canvas
musicRect=Rect(275,525,40,40)
colourRect=Rect(7,598,253,164)

#tools
pencilRect=Rect(330,690,60,60)
tool2Rect=Rect(400,690,60,60)
tool3Rect=Rect(470,690,60,60)
fillRect=Rect(540,690,60,60)
tool5Rect=Rect(610,690,60,60)
tool6Rect=Rect(680,690,60,60)
tool7Rect=Rect(750,690,60,60)
tool8Rect=Rect(820,690,60,60)
tool9Rect=Rect(890,690,60,60)
tool10Rect=Rect(960,690,60,60)

#default colour
drawColour=(0,0,0)

curtool="" #current tool

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
    
    draw.rect(screen,(255,0,0),pencilRect,2)
    draw.rect(screen,(255,0,0),tool2Rect,2)
    draw.rect(screen,(255,0,0),tool3Rect,2)
    draw.rect(screen,(255,0,0),fillRect,2)
    draw.rect(screen,(255,0,0),tool5Rect,2)
    draw.rect(screen,(255,0,0),tool6Rect,2)
    draw.rect(screen,(255,0,0),tool7Rect,2)
    draw.rect(screen,(255,0,0),tool8Rect,2)
    draw.rect(screen,(255,0,0),tool9Rect,2)
    draw.rect(screen,(255,0,0),tool10Rect,2)

    if colourRect.collidepoint(mx,my):
        if mb[0]==1:
            drawColour=screen.get_at((mx,my))
            draw.rect(screen,drawColour,(0,0,50,50))
            
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),pencilRect,2)
        if mb[0]==1:
            curtool="pencil"    
    if tool2Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),tool2Rect,2)
        if mb[0]==1:
            curtool="brush"
    if tool3Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),tool3Rect,2)
        if mb[0]==1:
            curtool="eraser"
    if fillRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),fillRect,2)
        if mb[0]==1:
            curtool="fill"
    if tool5Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),tool5Rect,2)
        if mb[0]==1:
            curtool="rect"
    if tool6Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),tool6Rect,2)
        if mb[0]==1:
            curtool="rectfilled"
    if tool7Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),tool7Rect,2)
        if mb[0]==1:
            curtool="circle"
    if tool8Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),tool8Rect,2)
        if mb[0]==1:
            curtool="circlefilled"
    if tool9Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),tool9Rect,2)
        if mb[0]==1:
            curtool="line"
    if tool10Rect.collidepoint(mx,my):
        draw.rect(screen,(0,0,255),tool10Rect,2)
        if mb[0]==1:
            curtool="spray"

    if curtool=="pencil":
        if mb[0]==1:
            copy=screen.copy()
            display.flip()
        if mb[0]==1 and omb[0]==1:
            if mx>329 and mx<1006:
                if my>100 and my<672:
                    screen.blit(copy,(0,0))
                    draw.line(screen,drawColour,(omx,omy),(mx,my),1)
        
    elif curtool=="brush":
        if mb[0]==1:
            copy=screen.copy()
            display.flip()
        if mb[0]==1 and omb[0]==1:
            if mx>329 and mx<1006:
                if my>100 and my<672:
                    screen.blit(copy,(0,0))
                    draw.line(screen,drawColour,(omx,omy),(mx,my),10)
                 
    elif curtool=="eraser":
        if mb[0]==1:
            copy=screen.copy()
            display.flip()
        if mb[0]==1 and omb[0]==1:
            if mx>329 and mx<1006:
                if my>100 and my<672:
                    screen.blit(copy,(0,0))
                    draw.line(screen,(255,255,255),(omx,omy),(mx,my),20)
        
    elif curtool=="fill":
        if mb[0]==1:
            if mx>329 and mx<1006:
                if my>100 and my<672:
                    draw.rect(screen,drawColour,canvasRect)

    #elif curtool=="rect":
        #if mb[0]==1:
         #   copy=screen.copy()
         #   display.flip()
        #if mb[0]==1 and omb[0]==1:
            #if mx>329 and mx<1006:
               # if my>100 and my<672:

    elif curtool=="line":
        if mb[0]==1:
            copy=screen.copy()
        if mb[0]==1 and omb[0]==1:
            if mx>329 and mx<1006:
               if my>100 and my<672:
                   draw.line(screen,drawColour,(omx,omy),(my,mx))
                    
                    

 
    display.flip()
quit()
