import pygame
pygame.init()
screen=pygame.display.set_mode([400,500])
screen.fill('purple')
playing=True

class Rectangle:
    def __init__(self,color,dimension,border):
        self.s=screen
        self.c=color
        self.d=dimension
        self.b=border
    def draw(self):
        pygame.draw.rect(self.s,self.c,self.d,self.b)
    def grow(self):
        self.b=self.b+80
        pygame.draw.rect(self.s,self.c,self.d,self.b)


rect1=Rectangle('pink',pygame.Rect(100,100,50,30),40)

while playing:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            playing=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            rect1.grow()



    rect1.draw()
    pygame.display.update()