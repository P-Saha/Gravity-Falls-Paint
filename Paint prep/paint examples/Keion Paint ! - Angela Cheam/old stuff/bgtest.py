#Keion Program -- Rough Stuffs.

#get the goods from the package downloaded, variable for the surface
from pygame import*
from random import*
screen=display.set_mode((1024,768))
#Try.
display.set_caption(".:Keion Paint:.")

#Load BG
keionBackground=image.load("images/k-onPaint1.png") 
screen.blit(keionBackground,(0,0))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
        if e.type==MOUSEBUTTONDOWN:
            back=screen.copy()
            screen.blit(back,(0,0))
    display.flip()
quit()
