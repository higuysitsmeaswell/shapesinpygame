import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))
blue = (0,0,255)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
class Circle():
    def __init__(self,circle_color,circle_radius,circle_width,pos):
        self.circle_color = circle_color
        self.circle_radius = 50
        self.circle_width = 25
        self.circle_surf = screen
        self.pos = pos
    def draw(self):
        self.draw_circle = pygame.draw.circle(self.circle_surf, self.circle_color,self.pos,self.circle_radius,self.circle_width)
    def grow(self,r):
        self.r = r
        self.circle_radius+=r
        self.draw_circle = pygame.draw.circle(self.circle_surf, self.circle_color,self.pos,self.circle_radius,self.circle_width)


object1 = Circle('blue',78,4,(300,300))
object1.draw()
pygame.display.update()