#Priyonto Saha
#Paint Program
#This program includes:
    #Pencil
    #Eraser
    #Brush
    #ScreenFill
    #Line
    #SprayPaint
    #Unfilled Rectangles
    #Filled Rectangles
    #Unfilled Ellipses
    #Ellipses
    #A variety of different colours
    #Save
    #Load
    #10 stamps
    #3 stamp sizes

'''Need instructions, add waddles egg, start screen'''
#Importing modules that will be used
from pygame import *
from random import *
from math import *
from tkinter import *
import os
root=Tk()                                 
root.withdraw()

#This sets the screen to the top left corner of the monitor
init()#This also initializes music and font
os.environ['SDL_VIDEO_WINDOW_POS']='0,25'

screen=display.set_mode((1200,700))#Setting the screen and screen size

#Some Basic Instructions:
print("Escape will exit the program")
print("M pauses the music")
print("Clicking the previewbox will pick a random colour.")
print("Scrolling will change the size.")      
#Some basic colours    
W=255,255,255
R=255,0,0
G=0,255,0
B=0,0,255
BL=0,0,0
drawC=BL
previewC=W

#Setting the Background
background=image.load("PaintPics/Background.png")
screen.blit(background,(0,0))

#Tool Icons and Buttons
#The variable names are kept consistent through out their rectangle name,
#tool name, image name, icon name, etc.

    #In this section, we create our rectangles for our buttons
pencilRect=Rect(20,80,50,50)    
eraserRect=Rect(80,80,50,50)
brushRect=Rect(20,140,50,50)
clearRect=Rect(80,140,50,50)    #This tool fills the whole screen
lineRect=Rect(20,200,50,50)
sprayRect=Rect(80,200,50,50)    #Spraypaint
urectRect=Rect(20,260,50,50)    #Unfilled Rectangle
rectRect=Rect(80,260,50,50)     #Filled Rectangle
uellipseRect=Rect(20,320,50,50) #Unfilled Ellipse
ellipseRect=Rect(80,320,50,50)  #Filled Ellipse
saveRect=Rect(20,655,50,40)
loadRect=Rect(80,655,50,40)
stampsize1Rect=Rect(1100,380,95,70) #These are for our different stamp size buttons
stampsize2Rect=Rect(1100,455,95,70)
stampsize3Rect=Rect(1100,530,95,70)
    #Here we load pictures, o stands for original as we will scale them.
opencil=image.load("IconPics/pencil.png")
oeraser=image.load("IconPics/eraser.png")
obrush=image.load("IconPics/brush.png")
oclear=image.load("IconPics/clear.png")
oline=image.load("IconPics/line.png")
ospray=image.load("IconPics/spray.png")
orect=image.load("IconPics/rect.png")
ourect=image.load("IconPics/urect.png")
oellipse=image.load("IconPics/ellipse.png")
ouellipse=image.load("IconPics/uellipse.png")
osave=image.load("IconPics/save.png")
oload=image.load("IconPics/load.png")
    #Here we scale our pictures into icons
pencilIcon=transform.smoothscale(opencil,(50,50))
eraserIcon=transform.smoothscale(oeraser,(50,50))
brushIcon=transform.smoothscale(obrush,(50,50))
clearIcon=transform.smoothscale(oclear,(50,50))
lineIcon=transform.smoothscale(oline,(50,50))
sprayIcon=transform.smoothscale(ospray,(50,50))
rectIcon=transform.smoothscale(orect,(50,50))
urectIcon=transform.smoothscale(ourect,(50,50))
ellipseIcon=transform.smoothscale(oellipse,(50,50))
uellipseIcon=transform.smoothscale(ouellipse,(50,50))
saveIcon=transform.smoothscale(osave,(40,40))
loadIcon=transform.smoothscale(oload,(40,40))
    #Here we draw white rectangles where the icons will go
draw.rect(screen,(W),pencilRect)
draw.rect(screen,(W),eraserRect)
draw.rect(screen,(W),brushRect)
draw.rect(screen,(W),clearRect)
draw.rect(screen,(W),lineRect)
draw.rect(screen,(W),sprayRect)
draw.rect(screen,(W),urectRect)
draw.rect(screen,(W),rectRect)
draw.rect(screen,(W),uellipseRect)
draw.rect(screen,(W),ellipseRect)
draw.rect(screen,(W),saveRect)
draw.rect(screen,(W),loadRect)
draw.rect(screen,(W),stampsize1Rect)
draw.rect(screen,(W),stampsize2Rect)
draw.rect(screen,(W),stampsize3Rect)
    #Here we place the icons on the white rectangles created earlier
screen.blit(pencilIcon,(pencilRect.x,pencilRect.y))
screen.blit(eraserIcon,(eraserRect.x,eraserRect.y))
screen.blit(brushIcon,(brushRect.x,brushRect.y))
screen.blit(clearIcon,(clearRect.x,clearRect.y))
screen.blit(lineIcon,(lineRect.x,lineRect.y))
screen.blit(sprayIcon,(sprayRect.x,sprayRect.y))
screen.blit(urectIcon,(urectRect.x,urectRect.y))
screen.blit(rectIcon,(rectRect.x,rectRect.y))
screen.blit(uellipseIcon,(uellipseRect.x,uellipseRect.y))
screen.blit(ellipseIcon,(ellipseRect.x,ellipseRect.y))
screen.blit(saveIcon,(saveRect.x+5,saveRect.y)) #Save and load are slightly different because 
screen.blit(loadIcon,(loadRect.x+5,loadRect.y)) #their button has a different size

#Stamps
#Just like we did our tool icons, we will also be doing our stamp icons.
#The stamp variable names are based off of their character.
    #Creating rectangles:
dipperRect=Rect(150,610,90,80)
mabelRect=Rect(245,610,90,80)
grunkleRect=Rect(340,610,90,80)
soosRect=Rect(435,610,90,80)
wendyRect=Rect(530,610,90,80)
fordRect=Rect(625,610,90,80)
billRect=Rect(720,610,90,80)
waddlesRect=Rect(815,610,90,80)
logoRect=Rect(910,610,90,80)
barfRect=Rect(1005,610,90,80)
    #Loading in images 
odipper=image.load("PaintPics/Dipper.png")
omabel=image.load("PaintPics/Mabel.png")
ogrunkle=image.load("PaintPics/Grunkle.png")
osoos=image.load("PaintPics/Soos.png")
owendy=image.load("PaintPics/Wendy.png")
oford=image.load("PaintPics/Ford.png")
obill=image.load("PaintPics/Bill.png")
owaddles=image.load("PaintPics/Waddles2.png")
ologo=image.load("PaintPics/Logo.png")
obarf=image.load("PaintPics/Barf.png")
    #Scaling the images:
        #Here we are scaling using what the dimensions of the original picture was to scale the stamps
        #as to not distort the image of our stamps
        #The scaling here was made so that the characters fit well on their buttons 
dipperIcon=transform.smoothscale(odipper,(672//9,1189//9))  #e.g the original picture was 672 x 1189 
mabelIcon=transform.smoothscale(omabel,(702//10,1137//10))
grunkleIcon=transform.smoothscale(ogrunkle,(1013//5,789//5))
soosIcon=transform.smoothscale(osoos,(2148//21,3573//21))
wendyIcon=transform.smoothscale(owendy,(313//4,588//4))
fordIcon=transform.smoothscale(oford,(880//12,1798//12))
billIcon=transform.smoothscale(obill,(678//10,832//10))
waddlesIcon=transform.smoothscale(owaddles,(369//4,221//4))
logoIcon=transform.smoothscale(ologo,(1395//13,806//13))
barfIcon=transform.smoothscale(obarf,(900//10,835//10)) #We have 3 barf scalings because they will be used as our stamp size icons as well
barfIcon2=transform.smoothscale(obarf,(900//20,835//20))
barfIcon3=transform.smoothscale(obarf,(900//30,835//30))
    #drawing white rectangles
draw.rect(screen,(W),dipperRect)
draw.rect(screen,(W),mabelRect)
draw.rect(screen,(W),grunkleRect)
draw.rect(screen,(W),soosRect)
draw.rect(screen,(W),wendyRect)
draw.rect(screen,(W),fordRect)
draw.rect(screen,(W),billRect)
draw.rect(screen,(W),waddlesRect)
draw.rect(screen,(W),logoRect)
draw.rect(screen,(W),barfRect)
    #putting our icons on our white rectangles
        #Because the images may not fit on the white rectangles we made, we must use screen.set_clip
        #this means that the images will not go off the buttons
screen.set_clip(dipperRect)
screen.blit(dipperIcon,(dipperRect.x,dipperRect.y))
screen.set_clip(mabelRect)
screen.blit(mabelIcon,(mabelRect.x+5,mabelRect.y+10))
screen.set_clip(grunkleRect)
screen.blit(grunkleIcon,(grunkleRect.x-60,grunkleRect.y+5))
screen.set_clip(soosRect)
screen.blit(soosIcon,(soosRect.x-15,soosRect.y+5))
screen.set_clip(wendyRect)
screen.blit(wendyIcon,(wendyRect.x,wendyRect.y))
screen.set_clip(fordRect)
screen.blit(fordIcon,(fordRect.x+5,fordRect.y+5))
screen.set_clip(billRect)
screen.blit(billIcon,(billRect.x+10,billRect.y))
screen.set_clip(waddlesRect)
screen.blit(waddlesIcon,(waddlesRect.x,waddlesRect.y+10))
screen.set_clip(logoRect)
screen.blit(logoIcon,(logoRect.x-10,logoRect.y+5))
screen.set_clip(barfRect)
screen.blit(barfIcon,(barfRect.x+5,barfRect.y))
screen.set_clip(stampsize1Rect)
screen.blit(barfIcon3,(stampsize1Rect.x+30,stampsize1Rect.y+20))
screen.set_clip(stampsize2Rect)
screen.blit(barfIcon2,(stampsize2Rect.x+25,stampsize2Rect.y+15))
screen.set_clip(stampsize3Rect)
screen.blit(barfIcon,(stampsize3Rect.x+10,stampsize3Rect.y-5))
screen.set_clip(None)

#Some other settings and variables needed/used
canvasRect=Rect(150,80,945,520)
paletteRect=Rect(20,500,110,150)
previewRect=Rect(20,380,110,110)
    #These are for indicating what tool,stamp, and stamp size are in use
toolsRect=Rect(10,70,130,305)
stampsRect=Rect(140,605,960,90)
stampsizesRect=Rect(1097,375,100,230)
tools=screen.subsurface(toolsRect).copy()   #These create copies of what the buttons looked like, 
stamps=screen.subsurface(stampsRect).copy() #and are used for indication of the tool being used.
stampsizes=screen.subsurface(stampsizesRect).copy()
draw.rect(screen,(R),pencilRect,2)
draw.rect(screen,(R),stampsize2Rect,2)
    #Here we actually draw the canvas
draw.rect(screen,(W),canvasRect)
    #Here we load our colour palette and put it on.
opalette=image.load("PaintPics/Palette.png")
palette=transform.smoothscale(opalette,(110,150))
screen.blit(palette,(20,500))
    #Tools and settings we start with that may change
tool="pencil"
size=20
music=True
stampsize="2"
stampsizeflag="-1"
comicFont=font.SysFont("Comic Sans MS",10)#Loading font
   
#Music                                  
mixer.music.load("GFMusic.mp3")
mixer.music.play()


#--------------------------------------------------------------------------------------       
running=True
while running:
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    #print(mx,my)   #These were for my testing
    #print(tool)
    #print(drawC)
    select=False
    for e in event.get():
        if e.type==QUIT:
            running=False
        if e.type==MOUSEBUTTONDOWN:
            omx,omy=mx,my   #This is used for our eraser, brush, and pencil (Stands for oldmx,oldmy)
            if e.button==1:
               select=True  #These select flags make sure we do not press buttons while drawing
               start=e.pos  #This is the start position of where the mouse is first pressed before being held
               canvas=screen.subsurface(canvasRect).copy()#This copies the canvas
            #Controls size by scrolling
            if e.button==4:
               size+=1
            if e.button==5:
               size-=1
        if e.type==KEYDOWN:
            #A music pause button
            if e.unicode=="m":
                music=not music
                if music==False:
                    mixer.music.pause()
                if music==True:
                    mixer.music.unpause()
                
            
        
    if key.get_pressed()[K_ESCAPE]: #Escape exits program
        break
    
    #Setting a minimum size of 1 and a maximum size of 110
    if size<1:
        size=1
    elif size>110:
        size=110
        
    draw.rect(screen,(previewC),previewRect)

#Coordinates
    #Here we set coords at the bottom right of the screen based on our canvas
    if canvasRect.collidepoint(mx,my):
        canvasmx=mx-150 #These are the coords of the canvas
        canvasmy=my-80
        coords=(str(canvasmx)+","+str(canvasmy))
    else:
       coords=("Off Canvas")#If the mouse is off the canvas
    coordsPic=comicFont.render(coords,True,(W))
    draw.rect(screen,(BL),(1145,685,55,15))
    screen.blit(coordsPic,(1145,685))
        
#Selection/Buttons
    if select==True: #Along with what was stated before, this also acts similarly to "if mb[0]==1:"
        #Tools                                  #These guidelines work for the rest of the tools and stamps:
        if pencilRect.collidepoint(mx,my):      #If the mouse is touching the button
            screen.blit(tools,(10,70))          #Blit on our tools copy made, reseting the indicator
            screen.blit(stamps,(140,605))       #Blit on our stamps copy made, reseting the indicator
            tool="pencil"                       #Select a tool
            draw.rect(screen,(R),pencilRect,2)  #Indicate tool is pressed
        if eraserRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="eraser"
            draw.rect(screen,(R),eraserRect,2)
        if brushRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="brush"
            draw.rect(screen,(R),brushRect,2)
        if lineRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="line"
            draw.rect(screen,(R),lineRect,2)
        if clearRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="clear"
            draw.rect(screen,(R),clearRect,2)
        if sprayRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="spray"
            draw.rect(screen,(R),sprayRect,2)
        if urectRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="urect"
            draw.rect(screen,(R),urectRect,2)
        if rectRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="rect"
            draw.rect(screen,(R),rectRect,2)
        if uellipseRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="uellipse"
            draw.rect(screen,(R),uellipseRect,2)
        if ellipseRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="ellipse"
            draw.rect(screen,(R),ellipseRect,2)
        #Stamps
        if dipperRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="dipper"
            draw.rect(screen,(R),dipperRect,2)
        if mabelRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="mabel"
            draw.rect(screen,(R),mabelRect,2)
        if grunkleRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="grunkle"
            draw.rect(screen,(R),grunkleRect,2)
        if soosRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="soos"
            draw.rect(screen,(R),soosRect,2)
        if wendyRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="wendy"
            draw.rect(screen,(R),wendyRect,2)
        if fordRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="ford"
            draw.rect(screen,(R),fordRect,2)
        if billRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="bill"
            draw.rect(screen,(R),billRect,2)
        if waddlesRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="waddles"
            draw.rect(screen,(R),waddlesRect,2)
        if logoRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="logo"
            draw.rect(screen,(R),logoRect,2)
        if barfRect.collidepoint(mx,my):
            screen.blit(tools,(10,70))
            screen.blit(stamps,(140,605))
            tool="barf"
            draw.rect(screen,(R),barfRect,2)
        #Save and Load
        if saveRect.collidepoint(mx,my):    #For save and load, they happen instantly, and are not tools
            fname=filedialog.asksaveasfilename(defaultextension=".png")
            if fname!="": #This means that the program won't crash if the field is empty
                image.save(screen.subsurface(canvasRect),fname)
        if loadRect.collidepoint(mx,my):       
            fname=filedialog.askopenfilename(filetypes=[("Images", "*.png;*.bmp;*.jpg;*.jpeg")])
            if fname!="": #This means that the program won't crash if the field is empty
                img=image.load(fname)
                img=transform.smoothscale(img,(canvasRect.width,canvasRect.height))
                screen.blit(img,(canvasRect.x,canvasRect.y))
        #StampSizes
        if stampsize1Rect.collidepoint(mx,my):      #Stampsizes have their own indicator
            screen.blit(stampsizes,(1097,375))      #Blits on copy, reseting indicator
            stampsize="1"                           #Changes the stampsize
            draw.rect(screen,(R),stampsize1Rect,2)  #Indicates the size use
        if stampsize2Rect.collidepoint(mx,my):
            screen.blit(stampsizes,(1097,375))
            stampsize="2"
            draw.rect(screen,(R),stampsize2Rect,2)
        if stampsize3Rect.collidepoint(mx,my):
            screen.blit(stampsizes,(1097,375))
            stampsize="3"
            draw.rect(screen,(R),stampsize3Rect,2)
        
        #Colour
        if paletteRect.collidepoint(mx,my):
            drawC=screen.get_at((mx,my))    #This gets a colour from the palette
        if previewRect.collidepoint(mx,my):
            drawC=(randint(0,255),randint(0,255),randint(0,255)) #The preview screen can act as a colour randomizer

#Stamp Sizes and Scaling
    #Here we scale different stamp for different stamp sizes
    if stampsize=="1": 
        if stampsizeflag!="1":#These flags are used so that the stamps arent't being scaled constantly            
            dipper=transform.smoothscale(odipper,(672//10,1189//10))#e.g. 672 x 1189 were original dimensions of the picture
            mabel=transform.smoothscale(omabel,(702//11,1137//11))
            grunkle=transform.smoothscale(ogrunkle,(1013//6,789//6))
            soos=transform.smoothscale(osoos,(2148//22,3573//22))
            wendy=transform.smoothscale(owendy,(313//4,588//4))
            ford=transform.smoothscale(oford,(880//12,1798//12))
            bill=transform.smoothscale(obill,(678//10,832//10))
            waddles=transform.smoothscale(owaddles,(369//4,221//4))
            logo=transform.smoothscale(ologo,(1395//10,806//10))
            barf=transform.smoothscale(obarf,(900//10,835//10))
            stampsizeflag="1"
    if stampsize=="2": #Stampsize2 is 2 times the size of stampsize1
        if stampsizeflag!="2":
            dipper=transform.smoothscale(odipper,(672//5,1189//5))
            mabel=transform.smoothscale(omabel,(int(702/5.5),int(1137//5.5))) #Integer division no longer works because of decimals
            grunkle=transform.smoothscale(ogrunkle,(1013//3,789//3))
            soos=transform.smoothscale(osoos,(2148//11,3573//11))
            wendy=transform.smoothscale(owendy,(313//2,588//2))
            ford=transform.smoothscale(oford,(880//6,1798//6))
            bill=transform.smoothscale(obill,(678//5,832//5))
            waddles=transform.smoothscale(owaddles,(369//2,221//2))
            logo=transform.smoothscale(ologo,(1395//5,806//5))
            barf=transform.smoothscale(obarf,(900//5,835//5))
            stampsizeflag="2"
    if stampsize=="3":#Stampsize3 is 3 times the size of stampsize1
        if stampsizeflag!="3":
            dipper=transform.smoothscale(odipper,(int(672/3.33),int(1189/3.33)))
            mabel=transform.smoothscale(omabel,(int(702/3.66),int(1137//3.66)))
            grunkle=transform.smoothscale(ogrunkle,(1013//2,789//2))
            soos=transform.smoothscale(osoos,(int(2148/7.33),int(3573/7.33)))
            wendy=transform.smoothscale(owendy,(int(313/1.33),int(588/1.33)))
            ford=transform.smoothscale(oford,(880//4,1798//4))
            bill=transform.smoothscale(obill,(int(678/3.33),int(832/3.33)))
            waddles=transform.smoothscale(owaddles,(int(369/1.33),int(221/1.33)))
            logo=transform.smoothscale(ologo,(int(1395/3.33),int(806/3.33)))
            barf=transform.smoothscale(obarf,(int(900/3.33),int(835/3.33)))
            stampsizeflag="3"        
        
#Preview
    #Here we set up a preview screen to see what will happen when you click, your colour, and your size
    if tool=="pencil":
        previewC=W #Sets the colour of the preview screen to white
        screen.set_at((75,435),drawC)#A small dot thesize of your pencil in the middle
    elif tool=="eraser":
        previewC=drawC #Sets the colour of the preview screen to the user's colour
        draw.circle(screen,W,(75,435),size//2) #A white circle the size of your eraser in the middle
    elif tool=="brush" or tool=="spray" or tool=="uellipse":
        previewC=W
        draw.circle(screen,drawC,(75,435),size//2) #A coloured circle the size of your tool in the center
    elif tool=="line" or tool=="urect":
        previewC=W
        draw.rect(screen,(drawC),(75-size/2,435-size/2,size,size)) #A coloured square the size of your tool in the center
    elif tool=="rect":
        previewC=W
        draw.rect(screen,(drawC),(30,390,90,90)) #A coloured rectangle
    elif tool=="ellipse":
        previewC=W
        draw.circle(screen,drawC,(75,435),50) #A coloured circle
    else:
        previewC=drawC #If a stamp or clear is being used, the preview will just be a colour 
#Tool Use 
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        #print(tool)
        if tool=="pencil":
            draw.line(screen,(drawC),(omx,omy),(mx,my))#Draws a line from your old mx,my to your current mx,my as you use it
        if tool=="eraser":
            dist=hypot(mx-omx,my-omy)   #A formula is used to find all the points on a line similar to our pencil,
            dist=max(dist,1)            #then a circle is drawn on every point, the diameter being our size
            varx=mx-omx
            vary=my-omy
            for i in range(int(dist)):
                bmx=int(omx+(i)/dist*varx)
                bmy=int(omy+(i)/dist*vary)
                draw.circle(screen,(W),(int(bmx),int(bmy)),size//2)
        if tool=="brush":
            dist=hypot(mx-omx,my-omy)   #Same as eraser, but with colour
            dist=max(dist,1)
            varx=mx-omx
            vary=my-omy
            for i in range(int(dist)):
                bmx=int(omx+(i)/dist*varx)
                bmy=int(omy+(i)/dist*vary)
                draw.circle(screen,(drawC),(int(bmx),int(bmy)),size//2)
        if tool=="line":    
            screen.blit(canvas,(150,80)) #Blits a copy of the canvas on so we do not have a flurry of lines
            draw.line(screen, (drawC), start,(mx,my), size) #Draws a line from where the mouse was first held to the current mx,my
            #draw.circle(screen,(drawC),start,size//2)      #I tried to have rounded ends to the line,
            #draw.circle(screen,(drawC),(mx,my),size//2)    #but it did not work well
        if tool=="clear":
            draw.rect(screen,(drawC),canvasRect)#Fills the screen with selected colour
        if tool=="spray":#Spraypaint
            for i in range(size*2):#The higher this range, the more rapid the spraypaint goes
                randx=randint(-size//2,size//2)
                randy=randint(-size//2,size//2)
                if ((randx**2+randy**2)**.5)<size//2:   #This makes the colour spray randomly within a circle
                    screen.set_at((mx+randx,my+randy),drawC)
        if tool=="urect":#Unfilled rectangle, made with a similar concept to the line tool
            screen.blit(canvas,(150,80))#Blitting the canvas for the same reason as the line tool
            draw.rect(screen,(drawC),(start[0],start[1],mx-start[0],my-start[1]),size)
            draw.rect(screen,(drawC),(start[0]-size/2+1,start[1]-size/2+1,size,size))#Little boxes were drawn on every vertex
            draw.rect(screen,(drawC),(start[0]-size/2+1,my-size/2,size,size))
            draw.rect(screen,(drawC),(mx-size/2,start[1]-size/2+1,size,size))
            draw.rect(screen,(drawC),(mx-size/2,my-size/2,size,size))
        if tool=="rect":#Simply a filled rectangle
            screen.blit(canvas,(150,80))
            draw.rect(screen,(drawC),(start[0],start[1],mx-start[0],my-start[1]))
        if tool=="ellipse":#filled ellipse
            screen.blit(canvas,(150,80))
            elRect=Rect(start[0],start[1],mx-start[0],my-start[1])#Ellipses are drawn on rectangles
            elRect.normalize()#prevents crashing as a result of negatives
            draw.ellipse(screen,(drawC),(elRect))
        if tool=="uellipse":#Unfilled Ellipse, made by drawing a filled ellipse of our drawC with a trasparent filled on top
            screen.blit(canvas,(150,80))
            elRect=Rect(start[0],start[1],mx-start[0],my-start[1])  #This rectangle is for our else when our inner ellipse won't fit 
            elRect.normalize()                                      #inside the outer ellipse, so we just draw a filled ellipse
            elRectu=Rect(0,0,elRect.width,elRect.height)            #Outer ellipse rectangle, based off our Elrect
            elRectuSurf=Surface((elRectu.width,elRectu.height),SRCALPHA)#We make these ellipses on a offscreen surface inorder to blit it transparently
            elRectu2=Rect(0+size,0+size,elRectu.width-size*2,elRectu.height-size*2)#Inner ellipse rectangle, will be transparent
            elRectu2.normalize()
            if min(elRectu.width,elRectu.height)>size*2: #Prevents ellipse being angrry for having a width greater than radius
                draw.ellipse(elRectuSurf,(drawC),(elRectu))#Draws the outer ellipse on the surface
                draw.ellipse(elRectuSurf,(209,41,72,0),(elRectu2))#Draws the inner trasnparent ellipse, which is a transparent pretty pink
                screen.blit(elRectuSurf,(elRect.x,elRect.y))#This blits the surface onto the canvas
            else:
                draw.ellipse(screen,(drawC),elRect)#This is our ellipse when no inner ellipse is needed.
                    
#Stamps Use
    #Scaling based off the same dimensions used earlier, but here we must use (mx-(dimension1)/2,my-(dimension2)/2))
    #to center our mouse on the stamp
        if stampsize=="1":
            if tool=="dipper":
                screen.blit(canvas,(150,80))#We blit the canvas for stamps as well
                screen.blit(dipper,(mx-(672//10)/2,my-(1189//10)/2))
            if tool=="mabel":
                screen.blit(canvas,(150,80))
                screen.blit(mabel,(mx-(702//11)/2,my-(1137//11)/2))
            if tool=="grunkle":
                screen.blit(canvas,(150,80))
                screen.blit(grunkle,(mx-(1013//6)/2,my-(789//6)/2))
            if tool=="soos":
                screen.blit(canvas,(150,80))
                screen.blit(soos,(mx-(2148//22)/2,my-(3573//22)/2))
            if tool=="wendy":
                screen.blit(canvas,(150,80))
                screen.blit(wendy,(mx-(313//4)/2,my-(588//4)/2))
            if tool=="ford":
                screen.blit(canvas,(150,80))
                screen.blit(ford,(mx-(880//12)/2,my-(1798//12)/2))
            if tool=="bill":
                screen.blit(canvas,(150,80))
                screen.blit(bill,(mx-(678//10)/2,my-(832//10)/2))
            if tool=="waddles":
                screen.blit(canvas,(150,80))
                screen.blit(waddles,(mx-(369//4)/2,my-(221//4)/2))
            if tool=="logo":
                screen.blit(canvas,(150,80))
                screen.blit(logo,(mx-(1395//10)/2,my-(806//10)/2))
            if tool=="barf":
                screen.blit(canvas,(150,80))
                screen.blit(barf,(mx-(900//10)/2,my-(835//10)/2))
                            
        if stampsize=="2":
            if tool=="dipper":
                screen.blit(canvas,(150,80))
                screen.blit(dipper,(mx-(672//5)/2,my-(1189//5)/2))
            if tool=="mabel":
                screen.blit(canvas,(150,80))
                screen.blit(mabel,(mx-(int(702/5.5))/2,my-(int(1137//5.5))/2))
            if tool=="grunkle":
                screen.blit(canvas,(150,80))
                screen.blit(grunkle,(mx-(1013//3)/2,my-(789//3)/2))
            if tool=="soos":
                screen.blit(canvas,(150,80))
                screen.blit(soos,(mx-(2148//11)/2,my-(3573//11)/2))
            if tool=="wendy":
                screen.blit(canvas,(150,80))
                screen.blit(wendy,(mx-(313//2)/2,my-(588//2)/2))
            if tool=="ford":
                screen.blit(canvas,(150,80))
                screen.blit(ford,(mx-(880//6)/2,my-(1798//6)/2))
            if tool=="bill":
                screen.blit(canvas,(150,80))
                screen.blit(bill,(mx-(678//5)/2,my-(832//5)/2))
            if tool=="waddles":
                screen.blit(canvas,(150,80))
                screen.blit(waddles,(mx-(369//2)/2,my-(221//2)/2))
            if tool=="logo":
                screen.blit(canvas,(150,80))
                screen.blit(logo,(mx-(1395//5)/2,my-(806//5)/2))
            if tool=="barf":
                screen.blit(canvas,(150,80))
                screen.blit(barf,(mx-(806//5)/2,my-(835//5)/2))

        if stampsize=="3":
            if tool=="dipper":
                screen.blit(canvas,(150,80))
                screen.blit(dipper,(mx-(int(672/3.33))/2,my-(int(1189/3.33))/2))
            if tool=="mabel":
                screen.blit(canvas,(150,80))
                screen.blit(mabel,(mx-(int(702/3.66))/2,my-(int(1137//3.66))/2))
            if tool=="grunkle":
                screen.blit(canvas,(150,80))
                screen.blit(grunkle,(mx-(1013//2)/2,my-(789//2)/2))
            if tool=="soos":
                screen.blit(canvas,(150,80))
                screen.blit(soos,(mx-(int(2148/7.33))/2,my-(int(3573/7.33))/2))
            if tool=="wendy":
                screen.blit(canvas,(150,80))
                screen.blit(wendy,(mx-(int(313/1.33))/2,my-(int(588/1.33))/2))
            if tool=="ford":
                screen.blit(canvas,(150,80))
                screen.blit(ford,(mx-(880//4)/2,my-(1798//4)/2))
            if tool=="bill":
                screen.blit(canvas,(150,80))
                screen.blit(bill,(mx-(int(678/3.33))/2,my-(int(832/3.33))/2))
            if tool=="waddles":
                screen.blit(canvas,(150,80))
                screen.blit(waddles,(mx-(int(369/1.33))/2,my-(int(221/1.33))/2))
            if tool=="logo":
                screen.blit(canvas,(150,80))
                screen.blit(logo,(mx-(int(1395/3.33))/2,my-(int(806/3.33))/2))
            if tool=="barf":
                screen.blit(canvas,(150,80))
                screen.blit(barf,(mx-(int(900/3.33))/2,my-(int(835/3.33))/2))
        screen.set_clip(None)#This allows our indicators to work again, and untoggles clip
        omx,omy=mx,my
    display.flip()#The usual display.flip() and quit

quit()
