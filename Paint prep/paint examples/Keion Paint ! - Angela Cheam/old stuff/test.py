#neater
from pygame import*
screen=display.set_mode((1024,768))
lukaBackground=image.load("images/k-onPaint.png") 
screen.blit(lukaBackground,(0,0))

music=True
if music==True:
    init()                                  # need init to initialize the mixer
    mixer.music.load("songs/nothankyou.mp3")       # load a MUSIC object
    mixer.music.play()
play=0

canvasRect=Rect(312,94,694,570) #Canvas
musicRect=Rect(275,525,40,40)
colourRect=Rect(10,594,218,162)

#tools
pencilRect=Rect(310,690,60,60)
tool2Rect=Rect(380,690,60,60)
tool3Rect=Rect(450,690,60,60)
fillRect=Rect(520,690,60,60)
tool5Rect=Rect(590,690,60,60)
tool6Rect=Rect(660,690,60,60)
tool7Rect=Rect(730,690,60,60)
tool8Rect=Rect(800,690,60,60)
tool9Rect=Rect(870,690,60,60)
tool10Rect=Rect(940,690,60,60)

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
    
    pencilPic=image.load("toolimages/pencilbutton.png")
    screen.blit(pencilPic,(310,690))
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
        pencilhoverPic=image.load("toolimages/pencilbuttonhover.png")
        screen.blit(pencilhoverPic,(310,690))
        if mb[0]==1:
            pencilpressedPic=image.load("toolimages/pencilbuttonpressed.png")
            screen.blit(pencilpressedPic,(310,690))
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

    if mb[0]==1:
        back=screen.copy()
        if mx>329 and mx<1006:
            if my>100 and my<672:
                if curtool=="pencil":
                    #pencilselectPic=image.load("toolimages/pencilbuttonselect.png")
                    #screen.blit(pencilselectPic,(310,690))
                    screen.blit(back,(0,0))
                    draw.line(screen,drawColour,(omx,omy),(mx,my),1)
                    
                elif curtool=="brush":
                    if mb[0]==1 and omb[0]==1:
                        screen.blit(back,(0,0))
                        draw.line(screen,drawColour,(omx,omy),(mx,my),10)
                 
                elif curtool=="eraser":
                    if mb[0]==1 and omb[0]==1:
                        screen.blit(back,(0,0))
                        draw.line(screen,(255,255,255),(omx,omy),(mx,my),20)
        
                elif curtool=="fill":
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
            back=screen.copy()
        if mb[0]==1 and omb[0]==1:
            if mx>329 and mx<1006:
               if my>100 and my<672:
                   draw.line(screen,drawColour,(omx,omy),(my,mx))
                    
                    

 
    display.flip()
quit()
