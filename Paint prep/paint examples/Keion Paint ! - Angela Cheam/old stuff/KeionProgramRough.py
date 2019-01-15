#Keion Program -- Rough Stuffs.

#get the goods from the package +downloaded, variable for the surface
from pygame import*
from random import*
from glob import *
screen=display.set_mode((1024,768))
#Try.

display.set_caption(".:Keion Paint:.")


def getName():
    ans = ""                    # final answer will be built one letter at a time.
    arialFont = font.SysFont("Times New Roman", 16)
    back = screen.copy()        # copy screen so we can replace it when done
    textArea = Rect(5,5,200,25) # make changes here.
    
    pics = glob("*.bmp")+glob("*.jpg")+glob("*.png")
    n = len(pics)
    choiceArea = Rect(textArea.x,textArea.y+textArea.height,textArea.width,n*textArea.height)
    draw.rect(screen,(220,220,220),choiceArea)        # draw the text window and the text.
    draw.rect(screen,(0,0,0),choiceArea,1)        # draw the text window and the text.
    for i in range(n):
        txtPic = arialFont.render(pics[i], True, (0,111,0))   #
        screen.blit(txtPic,(textArea.x+3,textArea.height*i+choiceArea.y))
        
    typing = True
    while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:    # remove last letter
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                elif e.key < 256:
                    ans += e.unicode       # add character to ans
                    
        txtPic = arialFont.render(ans, True, (0,0,0))   #
        draw.rect(screen,(220,255,220),textArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),textArea,2)            #
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))
        
        display.flip()
        
    screen.blit(back,(0,0))
    return ans
       


display.set_caption("Right Click to type")
font.init()                                 # must have this in your program for my font to work

comicFont = font.SysFont("Comic Sans MS", 20)

screen.fill((222,222,222))

#Load BG and palette~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
keionBackground=image.load("images/k-onPaint1.png")
palette=image.load("images/colourpalette.png")
screen.blit(keionBackground,(0,0))
screen.blit(palette,(10,564))
picLoad=image.load("images/k-on.jpg")

#Area assigned for the canvas, music button, and palette cmd tools~~~~~~~~~~~~~~~~~~~~~~~~
canvasRect=Rect(343,97,647,525) 
colourRect=Rect(10,594,187,196)

newRect=Rect(204,633,60,60)
openRect=Rect(271,633,60,60)
saveRect=Rect(204,700,60,60)
playRect=Rect(271,700,60,60)

#area assigned for size buttons
size1Rect=Rect(567,633,27,27)
size2Rect=Rect(567,665,27,27)
size3Rect=Rect(567,697,27,27)
size4Rect=Rect(567,729,27,27)

#area assigned for the tools~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pencilRect=Rect(600,633,60,60)
brushRect=Rect(600,700,60,60)
eraserRect=Rect(667,633,60,60)
fillRect=Rect(667,700,60,60)
rectRect=Rect(734,633,60,60)
rectfillRect=Rect(734,700,60,60)
ellipseRect=Rect(801,633,60,60)
ellipsefillRect=Rect(801,700,60,60)
starRect=Rect(868,633,60,60)
noteRect=Rect(868,700,60,60)
lineRect=Rect(935,633,60,60)
sprayRect=Rect(935,700,60,60)

#area assigned for stamps~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mioRect=Rect(350,5,80,80)
ritsuRect=Rect(442,5,80,80)
mugiRect=Rect(534,5,80,80)
azusaRect=Rect(626,5,80,80)
yuiRect=Rect(718,5,80,80)
nodokaRect=Rect(810,5,80,80)
uiRect=Rect(902,5,80,80)

#Tool images~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#starting images~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
newPic=image.load("toolimages/newbutton.png")
openPic=image.load("toolimages/openbutton.png")
savePic=image.load("toolimages/savebutton.png")
playPic=image.load("toolimages/playbutton.png")

pencilPic=image.load("toolimages/pencilbutton.png")
brushPic=image.load("toolimages/brushbutton.png")
eraserPic=image.load("toolimages/eraserbutton.png")
fillPic=image.load("toolimages/fillbutton.png")
rectPic=image.load("toolimages/rectbutton.png")
rectfillPic=image.load("toolimages/rectfillbutton.png")
ellipsePic=image.load("toolimages/ellipsebutton.png")
ellipsefillPic=image.load("toolimages/ellipsefillbutton.png")
starPic=image.load("toolimages/starbutton.png")
notePic=image.load("toolimages/notebutton.png")
linePic=image.load("toolimages/linebutton.png")
sprayPic=image.load("toolimages/spraybutton.png")

size1Pic=image.load("toolimages/size1button.png")
size2Pic=image.load("toolimages/size2button.png")
size3Pic=image.load("toolimages/size3button.png")
size4Pic=image.load("toolimages/size4button.png")

#Hover images~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
newhoverPic=image.load("toolimages/newbuttonhover.png")
openhoverPic=image.load("toolimages/openbuttonhover.png")
savehoverPic=image.load("toolimages/savebuttonhover.png")
playhoverPic=image.load("toolimages/playbuttonhover.png")

pencilhoverPic=image.load("toolimages/pencilbuttonhover.png")
brushhoverPic=image.load("toolimages/brushbuttonhover.png")
eraserhoverPic=image.load("toolimages/eraserbuttonhover.png")
fillhoverPic=image.load("toolimages/fillbuttonhover.png")
recthoverPic=image.load("toolimages/rectbuttonhover.png")
rectfillhoverPic=image.load("toolimages/rectfillbuttonhover.png")
ellipsehoverPic=image.load("toolimages/ellipsebuttonhover.png")
ellipsefillhoverPic=image.load("toolimages/ellipsefillbuttonhover.png")
starhoverPic=image.load("toolimages/starbuttonhover.png")
notehoverPic=image.load("toolimages/notebuttonhover.png")
linehoverPic=image.load("toolimages/linebuttonhover.png")
sprayhoverPic=image.load("toolimages/spraybuttonhover.png")

#pressed/selected images~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

newselectPic=image.load("toolimages/newbuttonselect.png")
openselectPic=image.load("toolimages/openbuttonselect.png")
saveselectPic=image.load("toolimages/savebuttonselect.png")
playselectPic=image.load("toolimages/playbuttonselect.png")

pencilpressedPic=image.load("toolimages/pencilbuttonpressed.png")
pencilselectPic=image.load("toolimages/pencilbuttonselect.png")
brushselectPic=image.load("toolimages/brushbuttonselect.png")
eraserselectPic=image.load("toolimages/eraserbuttonselect.png")
fillselectPic=image.load("toolimages/fillbuttonselect.png")
rectselectPic=image.load("toolimages/rectbuttonselect.png")
rectfillselectPic=image.load("toolimages/rectfillbuttonselect.png")
ellipseselectPic=image.load("toolimages/ellipsebuttonselect.png")
ellipsefillselectPic=image.load("toolimages/ellipsefillbuttonselect.png")
starselectPic=image.load("toolimages/starbuttonselect.png")
noteselectPic=image.load("toolimages/notebuttonselect.png")
lineselectPic=image.load("toolimages/linebuttonselect.png")
sprayselectPic=image.load("toolimages/spraybuttonselect.png")

#Stamp images~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#starting stamp images~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mioPic=image.load("images/mio.png")
ritsuPic=image.load("images/ritsu.png")
mugiPic=image.load("images/mugi.png")
azusaPic=image.load("images/azusa.png")
yuiPic=image.load("images/yui.png")
nodokaPic=image.load("images/nodoka.png")
uiPic=image.load("images/ui.png")


#hover images and select images~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
miohoverPic=image.load("images/miohover.png")
mioselectPic=image.load("images/mioselect.png")
ritsuhoverPic=image.load("images/ritsuhover.png")
ritsuselectPic=image.load("images/ritsuselect.png")
mugihoverPic=image.load("images/mugihover.png")
mugiselectPic=image.load("images/mugiselect.png")
azusahoverPic=image.load("images/azusahover.png")
azusaselectPic=image.load("images/azusaselect.png")
yuihoverPic=image.load("images/yuihover.png")
yuiselectPic=image.load("images/yuiselect.png")
nodokahoverPic=image.load("images/nodokahover.png")
nodokaselectPic=image.load("images/nodokaselect.png")
uihoverPic=image.load("images/uihover.png")
uiselectPic=image.load("images/uiselect.png")

#full images~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                                                                                                                                                              
mioStamp=image.load("images/miofull.png")
ritsuStamp=image.load("images/ritsufull.png")
mugiStamp=image.load("images/mugifull.png")
azusaStamp=image.load("images/azusafull.png")
yuiStamp=image.load("images/yuifull.png")
nodokaStamp=image.load("images/nodokafull.png")
uiStamp=image.load("images/uifull.png")

#descriptions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#descpencil=image.load("images/dpencil.png")
#descbrush=image.load("images/dbrush.png")
desceraser=image.load("toolimages/deraser.png")
#descfill=image.load("images/dfill.png")
#descrect=image.load("images/drect.png")
#descrectfill=image.load("images/drectfill.png")
#descellipse=image.load("images/dellipse.png")
#descellipsefill=image.load("images/dellipsefill.png")
#descstar=image.load("images/dstar.png")
#descnote=image.load("images/dnote.png")
#descline=image.load("images/dline.png")
#descspray=image.load("images/dspray.png")
#defaults; colour, tool ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
drawColour=(0,0,0) #current colour
drawColour2=(255,255,255)
curTool="pencil" #current tool
size=2
cirsize=0


#no buttons being pressed, pos of mouse
omb=mb=(0,0,0) 
mx,my=0,0


#init()
#mixer.music.load("songs/nothankyou.mp3")

#THE LOOP ! ;D
running=True
y = 20
message = ""
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
        if e.type==MOUSEBUTTONDOWN:
            back=screen.copy()
            screen.blit(back,(0,0))
            cmx,cmy=mouse.get_pos()
            
    
   #curback=screen.copy()
   #screen.blit(curback,(0,0))
   #screen.blit(cursorPic,(mx,my))        
    
                                                 
    #mixer.music.play()
    
    omx,omy=mx,my
    mx,my=mouse.get_pos()
    omb=mb
    mb=mouse.get_pressed()
    keys=key.get_pressed()

    #star button stuff
    starlist=[(mx,my-40),(mx+28,my+35),(mx-40,my-10),(mx+40,my-10),(mx-28,my+35)]
    pentlist=[(mx-14,my-10),(mx+14,my-10),(mx+18,my+10),(mx,my+18),(mx-18,my+14)]
    randCol=(randint(0,255),randint(0,255),randint(0,255))
    #note button stuff
#List for the Eighth Note Polygon
    #eighthlist=[(mx,my-38),(mx+12,my-36),(mx+22,my-32),(mx+28,my-20),(mx+34,my-18),(mx+42,my-15)]    
    #Gets the drawColour (the colour the use wants to use from the palette)
    if colourRect.collidepoint(mx,my):
        if mb[0]==1:
            drawColour=screen.get_at((mx,my))
            draw.rect(screen,drawColour,(204,566,50,50))
        elif mb[2]==1:
            drawColour2=screen.get_at((mx,my))
            draw.rect(screen,drawColour2,(254,566,40,40))

    #Images of the starting images for the tools
    screen.blit(newPic,(204,633))
    screen.blit(openPic,(271,633))
    screen.blit(savePic,(204,700))
    screen.blit(playPic,(271,700))

    screen.blit(pencilPic,(600,633))
    screen.blit(brushPic,(600,700))
    screen.blit(eraserPic,(667,633))
    screen.blit(fillPic,(667,700))
    screen.blit(rectPic,(734,633))
    screen.blit(rectfillPic,(734,700))
    screen.blit(ellipsePic,(801,633))
    screen.blit(ellipsefillPic,(801,700))
    screen.blit(starPic,(868,633))
    screen.blit(notePic,(868,700))
    screen.blit(linePic,(935,633))
    screen.blit(sprayPic,(935,700))

    screen.blit(size1Pic,(567,633))
    screen.blit(size2Pic,(567,665))
    screen.blit(size3Pic,(567,697))
    screen.blit(size4Pic,(567,729))

    if size1Rect.collidepoint(mx,my):
        #screen.blit(size1Pic,(567,633))
        if mb[0]==1:
            size=2
            cirsize=0
    if size2Rect.collidepoint(mx,my):
        #screen.blit(size1Pic,(567,665))
        if mb[0]==1:
            size=6
            cirsize=2
    if size3Rect.collidepoint(mx,my):
        #screen.blit(size1Pic,(567,697))
        if mb[0]==1:
            size=10
            cirsize=3
    if size4Rect.collidepoint(mx,my):
        #screen.blit(size1Pic,(567,729))
        if mb[0]==1:
            size=14
            cirsize=5
            

    if newRect.collidepoint(mx,my):
        screen.blit(newhoverPic,(204,633))
        if mb[0]==1:
            curTool="new"
    if openRect.collidepoint(mx,my):
        screen.blit(openhoverPic,(271,633))
        if mb[0]==1:
            curTool="open"
    if saveRect.collidepoint(mx,my):
        screen.blit(savehoverPic,(204,700))
        if mb[0]==1:
            curTool="save"
    if playRect.collidepoint(mx,my):
        screen.blit(playhoverPic,(271,700))
        if mb[0]==1:
            curTool="play"

    if curTool=="new":
        screen.blit(newselectPic,(204,633))
        if mb[0]==1:
            draw.rect(screen,(255,255,255),canvasRect)
    if curTool=="open":
        screen.blit(openselectPic,(271,633))
        if mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(picLoad,(343,97))
            screen.set_clip(None)
    if curTool=="save":
        screen.blit(saveselectPic,(204,700))
        if mb[0]==1:
            image.save(screen.subsurface(canvasRect),"myPicture.bmp")
    if curTool=="play":
        screen.blit(playselectPic,(271,700))
        #if mb[0]==1:
            #mixer.music.pause()
            #if mb[2]==1:
                #mixer.music.unpause()
            
    #if the tools are hovered over/clicked, blit screen with hover image
    #and change the current tool to the selected one
    if pencilRect.collidepoint(mx,my):
        screen.blit(pencilpressedPic,(600,633))
        if mb[0]==1:
            curTool="pencil"
    if brushRect.collidepoint(mx,my):
        screen.blit(brushhoverPic,(600,700))
        if mb[0]==1:
            curTool="brush"
    if eraserRect.collidepoint(mx,my):
        screen.blit(eraserhoverPic,(667,633))
        if mb[0]==1:
            curTool="eraser"
            screen.blit(desceraser,(339,633))
    if fillRect.collidepoint(mx,my):
        screen.blit(fillhoverPic,(667,700))
        if mb[0]==1:
            curTool="fill"
    if rectRect.collidepoint(mx,my):
        screen.blit(recthoverPic,(734,633))
        if mb[0]==1:
            curTool="rect"
    if rectfillRect.collidepoint(mx,my):
        screen.blit(rectfillhoverPic,(734,700))
        if mb[0]==1:
            curTool="rectfill"
    if ellipseRect.collidepoint(mx,my):
        screen.blit(ellipsehoverPic,(801,633))
        if mb[0]==1:
            curTool="ellipse"
    if ellipsefillRect.collidepoint(mx,my):
        screen.blit(ellipsefillhoverPic,(801,700))
        if mb[0]==1:
            curTool="ellipsefill"
    if starRect.collidepoint(mx,my):
        screen.blit(starhoverPic,(868,633))
        if mb[0]==1:
            curTool="star"
    if noteRect.collidepoint(mx,my):
        screen.blit(notehoverPic,(868,700))
        if mb[0]==1:
            curTool="note"
    if lineRect.collidepoint(mx,my):
        screen.blit(linehoverPic,(935,633))
        if mb[0]==1:
            curTool="line"
    if sprayRect.collidepoint(mx,my):
        screen.blit(sprayhoverPic,(935,700))
        if mb[0]==1:
            curTool="spray"

    if curTool=="pencil":
        screen.blit(pencilselectPic,(600,633))
        if mb[0]==1:
            back=screen.copy()
        if mb[0]==1 and omb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(back,(0,0))
            draw.line(screen,drawColour,(omx,omy),(mx,my),1)
            screen.set_clip(None)
        if mb[2]==1:
            back=screen.copy() 
        if mb[2]==1 and omb[2]==1:
            screen.set_clip(canvasRect)
            screen.blit(back,(0,0))
            draw.line(screen,drawColour2,(omx,omy),(mx,my),1)
            screen.set_clip(None)
    elif curTool=="brush":
        screen.blit(brushselectPic,(600,700))
        if mb[0]==1:
            back=screen.copy()
        if mb[0]==1 and omb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(back,(0,0))
            draw.line(screen,drawColour,(omx,omy),(mx,my),size)
            draw.circle(screen,drawColour,(mx,my),cirsize)
            screen.set_clip(None)
        if mb[2]==1:
            back=screen.copy()
        if mb[2]==1 and omb[2]==1:
            screen.set_clip(canvasRect)
            screen.blit(back,(0,0))
            draw.line(screen,drawColour2,(omx,omy),(mx,my),size)
            draw.circle(screen,drawColour2,(mx,my),cirsize)
            screen.set_clip(None)
    elif curTool=="eraser":
        screen.blit(eraserselectPic,(667,633))
        if mb[0]==1:
            back=screen.copy()
        if mb[0]==1 and omb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(back,(0,0))
            draw.line(screen,(255,255,255),(omx,omy),(mx,my),size)
            draw.circle(screen,(255,255,255),(mx,my),cirsize)
            screen.set_clip(None)
    elif curTool=="fill":
        screen.blit(fillselectPic,(667,700))
        if mb[0]==1:
            if mx>343 and mx<990:
                if my>94 and my<622:
                    #colourfill=screen.get_at((mx,my))
                    draw.rect(screen,drawColour,canvasRect)
        if mb[2]==1:
            if mx>343 and mx<990:
                if my>94 and my<622:
                    #colourfill=screen.get_at((mx,my))
                    draw.rect(screen,drawColour2,canvasRect)
    elif curTool=="rect":
        screen.blit(rectselectPic,(734,633))
        screen.set_clip(canvasRect)
        if mb[0]==1:
            screen.blit(back,(0,0))
            draw.rect(screen,drawColour,(cmx,cmy,mx-cmx,my-cmy),size)
        elif mb[2]==1: 
            screen.blit(back,(0,0))
            draw.rect(screen,drawColour2,(cmx,cmy,mx-cmx,my-cmy),size)
        screen.set_clip(None)
        
    elif curTool=="rectfill":
        screen.blit(rectfillselectPic,(734,700))
        screen.set_clip(canvasRect)
        if mb[0]==1:
            screen.blit(back,(0,0))
            draw.rect(screen,drawColour,(cmx,cmy,mx-cmx,my-cmy))
        if mb[2]==1:
            screen.set_clip(canvasRect)
            screen.blit(back,(0,0))
            draw.rect(screen,drawColour2,(cmx,cmy,mx-cmx,my-cmy))
        screen.set_clip(None)
    elif curTool=="ellipse":
        screen.blit(ellipseselectPic,(801,633))
        screen.set_clip(canvasRect)
        if mb[0]==1:
            screen.blit(back,(0,0))
            elli=Rect(cmx,cmy,mx-cmx,my-cmy)
            elli.normalize()
            if elli.width>4 and elli.height>4:
                draw.ellipse(screen,drawColour,elli,size)
        if mb[2]==1:
            screen.blit(back,(0,0))
            elli=Rect(cmx,cmy,mx-cmx,my-cmy)
            elli.normalize()
            if elli.width>4 and elli.height>4:
                draw.ellipse(screen,drawColour2,elli,size)
        screen.set_clip(None)
    elif curTool=="ellipsefill":
        screen.blit(ellipsefillselectPic,(801,700))
        screen.set_clip(canvasRect)
        if mb[0]==1:
            screen.blit(back,(0,0))
            elli=Rect(cmx,cmy,mx-cmx,my-cmy)
            elli.normalize()
            draw.ellipse(screen,drawColour,elli)
        if mb[2]==1:
            screen.blit(back,(0,0))
            elli=Rect(cmx,cmy,mx-cmx,my-cmy)
            elli.normalize()
            draw.ellipse(screen,drawColour2,elli)
        screen.set_clip(None)
    elif curTool=="star":
        screen.blit(starselectPic,(868,633))
        screen.set_clip(canvasRect)
        if mb[0]==1:
            screen.blit(back,(0,0))
            draw.polygon(screen,randCol,starlist)
            draw.polygon(screen,randCol,pentlist)
        screen.set_clip(None)
    elif curTool=="line":
        screen.blit(lineselectPic,(935,633))
        screen.set_clip(canvasRect)
        if mb[0]==1:
            screen.blit(back,(0,0))
            draw.line(screen,drawColour,(cmx,cmy),(mx,my),size)
        if mb[2]==1:
            screen.blit(back,(0,0))
            draw.line(screen,drawColour2,(cmx,cmy),(mx,my),size)
        screen.set_clip(None)
    elif curTool=="spray":
        screen.blit(sprayselectPic,(935,700))
        if mb[0]==1 and omb[0]==1:
            screen.set_clip(canvasRect)
            draw.circle
            draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),(mx,my,omx-mx,omy-my),size)
            screen.set_clip(None)
    elif curTool=="note":
        screen.blit(noteselectPic,(868,700))
        if mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(back,(0,0))
            draw.line(screen,randCol,(mx,my-35),(mx,my+35),4)
            draw.circle(screen,randCol,(mx-16,my+32),18)
            #draw.polygon(screen,randCol,eighthlist,1)
                        
            #screen.blit(back,(0,0))
            #draw.line(screen,randCol,(mx,my-35),(mx,my+35),4)
            #draw.circle(screen,randCol,(mx-16,my+32),18)
            #draw.polygon(screen,(0,0,255),eighthlist,1)
                   

                   
#STAMP STUFFFFFFFFFFSSS ;3
    screen.blit(mioPic,(350,5))
    screen.blit(ritsuPic,(442,5))
    screen.blit(mugiPic,(534,5))
    screen.blit(azusaPic,(626,5))
    screen.blit(yuiPic,(718,5))
    screen.blit(nodokaPic,(810,5))
    screen.blit(uiPic,(902,5))
    
#hover images and select images
    if mioRect.collidepoint(mx,my):
        screen.blit(miohoverPic,(350,5))
        if mb[0]==1:
            curTool="StampMio"
    if ritsuRect.collidepoint(mx,my):
        screen.blit(ritsuhoverPic,(442,5))
        if mb[0]==1:
            curTool="StampRitsu"
    if mugiRect.collidepoint(mx,my):
        screen.blit(mugihoverPic,(534,5))
        if mb[0]==1:
            curTool="StampMugi"
    if azusaRect.collidepoint(mx,my):
        screen.blit(azusahoverPic,(626,5))
        if mb[0]==1: 
            curTool="StampAzusa"
    if yuiRect.collidepoint(mx,my):
        screen.blit(yuihoverPic,(718,5))
        if mb[0]==1:
            curTool="StampYui"
    if nodokaRect.collidepoint(mx,my):
        screen.blit(nodokahoverPic,(810,5))
        if mb[0]==1:
            curTool="StampNodoka"
    if uiRect.collidepoint(mx,my):
        screen.blit(uihoverPic,(902,5))
        if mb[0]==1:
            curTool="StampUi"
            
#If the stamp is ... allow the user to use the stamp
#on the canvas
    if curTool=="StampMio":
        screen.blit(mioselectPic,(350,5))
        if mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(back,(0,0))
            screen.blit(mioStamp,(mx-50,my-130))
            screen.set_clip(None)
    if curTool=="StampRitsu":
        screen.blit(ritsuselectPic,(442,5))
        if mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(back,(0,0))
            screen.blit(ritsuStamp,(mx-50,my-130))
    if curTool=="StampMugi":
        screen.blit(mugiselectPic,(534,5))
        if mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(back,(0,0))
            screen.blit(mugiStamp,(mx-50,my-130))
            screen.set_clip(None)
    if curTool=="StampAzusa":
        screen.blit(azusaselectPic,(626,5))
        if mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(back,(0,0))
            screen.blit(azusaStamp,(mx-50,my-130))
            screen.set_clip(None)
    if curTool=="StampYui":
        screen.blit(yuiselectPic,(718,5))
        if mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(back,(0,0))
            screen.blit(yuiStamp,(mx-50,my-130))
            screen.set_clip(None)
    if curTool=="StampNodoka":
        screen.blit(nodokaselectPic,(810,5))
        if mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(back,(0,0))
            screen.blit(nodokaStamp,(mx-50,my-130))
            screen.set_clip(None)
    if curTool=="StampUi":
        screen.blit(uiselectPic,(902,5))
        if mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(back,(0,0))
            screen.blit(uiStamp,(mx-50,my-130))
            screen.set_clip(None)

    if mb[1]==1:
        txt = getName()                     # this is how you would call my getName function
                                            # your main loop will stop looping until user hits enter
        txtPic = comicFont.render(txt, True, (255,0,0))
        screen.blit(txtPic,(100,100))

    display.flip()

font.quit()
del comicFont

quit()
