import pygame
pygame.init()
screen=pygame.display.set_mode([400,500])
screen.fill('dark blue')
playing=True
class Circle():
    def __init__(self,color,pos,radius,border):
        self.c=color
        self.p=pos
        self.r=radius
        self.b=border
        self.s=screen

    def draw(self):
        pygame.draw.circle(self.s,self.c,self.p,self.r,self.b)
    
    def grow(self):
        self.r=self.r+5
        pygame.draw.circle(self.s,self.c,self.p,self.r,self.b)
        

circle1=Circle('pink',(200,200),70,10)
circle2=Circle('purple',(200,200),50,10)
circle3=Circle('blue',(200,200),30,10)
while playing:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            playing=False
        if (event.type==pygame.MOUSEBUTTONDOWN):
            circle1.grow()
            circle2.grow()
            circle3.grow()
        if event.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            circle4=Circle('orange',(pos),5,1)
            circle4.draw()
            pygame.display.update()

    circle1.draw()
    circle2.draw()
    circle3.draw()
    pygame.display.update()
   