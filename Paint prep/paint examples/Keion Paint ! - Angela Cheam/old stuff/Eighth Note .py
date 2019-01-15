from pygame import*
from random import*
screen=display.set_mode((1024,768))
omb=mb=(0,0,0) 
mx,my=0,0

running=True
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
  
    #Variables for the mouse stuff
    omx,omy=mx,my
    mx,my=mouse.get_pos()
    omb=mb
    mb=mouse.get_pressed()
    keys=key.get_pressed()

    randCol=(randint(0,255),randint(0,255),randint(0,255))
    #List for the Star Polygon
    starlist=[(mx,my-40),(mx+28,my+35),(mx-40,my-10),(mx+40,my-10),(mx-28,my+35)]
    pentlist=[(mx-14,my-10),(mx+14,my-10),(mx+18,my+10),(mx,my+18),(mx-18,my+14)]
    
    #List for the Eighth Note Polygon
    if mb[0]==1:
        eighthlist=[(mx,my-40),(mx+8,my-40),(mx+14,my-38),(mx+18,my-35),(mx+20,my-25),(mx+24,my-28),
                    (mx+30,my-18),(mx+24,my-20),(mx+20,my-18)]
        draw.line(screen,randCol,(mx,my-35),(mx,my+35),4)
        draw.circle(screen,randCol,(mx-16,my+32),18)
        draw.polygon(screen,(0,0,255),eighthlist,1)
    display.flip()
quit()
