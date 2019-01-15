from pygame import*
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
    curTool="fill"
    if curTool=="fill":
        if mb[0]==1:
            if mx>312 and mx<1006:
                if my>94 and my<664:
                    colourfill=screen.get_at((mx,my))
                    print colourfill
    display.flip()
quit()
                    
