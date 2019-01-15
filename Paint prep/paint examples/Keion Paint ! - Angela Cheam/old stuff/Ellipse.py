from pygame import*
screen=display.set_mode((500,500))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
        if e.type==MOUSEBUTTONDOWN:
            back=screen.copy()
            screen.blit(back,(0,0))
            cmx,cmy=mouse.get_pos()

    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    curTool="ellipse"
    
    if curTool=="ellipse": #draw.ellipse(Surface, color, Rect(x,y,width,length), width=0)
        if mb[2]==1:
            elli=Rect(cmx,cmy,mx-cmx,my-cmy)
            elli.normalize()
            draw.ellipse(screen,(0,0,255),elli)
    display.flip()
quit()
