from pygame import *
from tkinter import *   
#from tkFileDialog import askopenfilename
root = Tk()                                 
root.withdraw()

screen = display.set_mode((1200,675))

canvasRect = Rect(100,50,900,575)
pencilRect = Rect(20,80,40,40)
eraserRect = Rect(65,80,40,40)

running =True
screen.fill((255,255,255))
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 3:
                image.save(screen.subsurface(canvasRect),"myPic.png")

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    draw.rect(screen,(0,255,0),pencilRect,2)
    draw.rect(screen,(0,255,0),eraserRect,2)
    
    draw.rect(screen,(0,0,0), canvasRect,2)
    if mb[0]==1:
        draw.circle(screen, (0,0,0), (mx,my), 3)
        
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),pencilRect,2)
        if mb[0]==1:
            fname = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.bmp;*.jpg;*.jpeg")])
            img = image.load(fname)
            screen.blit(img,(0,0))
            print(fname)
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),eraserRect,2)
        if mb[0]==1:
            fname = filedialog.asksaveasfilename(defaultextension=".png")
            image.save(screen.subsurface(canvasRect),fname)
            print(fname)
    display.flip()


quit()
