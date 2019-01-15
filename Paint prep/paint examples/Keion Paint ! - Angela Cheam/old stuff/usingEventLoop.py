from pygame import *    
screen = display.set_mode((800,600))
sz=10
running =True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            mouse.set_visible(False)
        if evt.type == MOUSEBUTTONUP:
            mouse.set_visible(True)
        if evt.type == KEYDOWN:
            if evt.key == K_LEFT:
                sz -= 1
            if evt.key == K_RIGHT:
                sz += 1
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    if mb[0]==1:
        draw.circle(screen, (255,0,0), (mx,my), sz)
    display.flip()
quit()

