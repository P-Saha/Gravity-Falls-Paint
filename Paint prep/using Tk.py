from pygame import *
from tkinter import *   
#from tkFileDialog import askopenfilename
root = Tk()                                 
root.withdraw()

screen = display.set_mode((800,600))
pencilRect = Rect(20,80,40,40)
eraserRect = Rect(65,80,40,40)

running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False


    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    draw.rect(screen,(0,255,0),pencilRect,2)
    draw.rect(screen,(0,255,0),eraserRect,2)
    
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),pencilRect,2)
        if mb[0]==1:
            fname = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.bmp;*.jpg;*.jpeg")])
            print(fname)
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),eraserRect,2)
        if mb[0]==1:
            fname = filedialog.asksaveasfilename(defaultextension=".png")
            print(fname)
            
    display.flip()


quit()
