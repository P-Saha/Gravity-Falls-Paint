from pygame import *
from random import *
    
screen = display.set_mode((1000,600))

font.init()
comicFont = font.SysFont("Arial", 20)
quotes = ["Nan baboraseo.",
        "Waeyo waeyo waejyo eonni?",
        "Hey, T-ARA~",
        "Korjitmar..",
        "Bogoshipeoseo.",
        "Hello! How are you."]
running =True
while running:
    click = False
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            click = True
            
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    if click:
        txtPic = comicFont.render(choice(quotes), True, (255,0,0))
        screen.blit(txtPic,(mx-txtPic.get_width()/2, my-txtPic.get_height()/2))
    if mb[2]==1:
        screen.fill((0,0,0))
    display.flip()

font.quit()
del comicFont
quit()
