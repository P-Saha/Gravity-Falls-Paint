from pygame import *
from random import *

screen = display.set_mode((1024,768))
spacePic = image.load("images/space.jpg") 
used = set()
running =True
screen.blit(spacePic,(0,0))
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
            
    for i in range(5000):
        x,y = randint(0,1023),randint(0,767)
        if (x,y) not in used:
            used.add((x,y))
            r,g,b,a = screen.get_at((x,y))
            r2 = min(255,int(r * .393 + g *.769 + b * .189))
            g2 = min(255,int(r * .349 + g *.686 + b * .168))
            b2 = min(255,int(r * .272 + g *.534 + b * .131))
            screen.set_at((x,y),(r2,g2,b2))
  
    display.flip()
    time.wait(10)

quit()
