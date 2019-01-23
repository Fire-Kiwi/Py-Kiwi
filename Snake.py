import pygame, sys, random, time
from pygame.locals import *
print ("SNAKE!")
FPS = 5
pygame.init()
fpsClock=pygame.time.Clock()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
pygame.display.set_caption('THE COLORS OF SNAKE')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((210,180,140))
clock = pygame.time.Clock()

pygame.key.set_repeat(1, 40)

GRIDSIZE=10
GRID_WIDTH = SCREEN_WIDTH / GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE
UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)
screen.blit(surface, (0,0))
def intro(): 
    font = pygame.font.Font('freesansbold.ttf', 72)
    surfer = font.render('SNAKE', True,(255,255,255))
    recter = surfer.get_rect()
    recter.midtop = (320, 240)
    screen.blit(surfer, recter)
    pygame.display.flip()
    pygame.display.update()
    time.sleep(2)
    surface.fill((0,0,0))
    font = pygame.font.Font('freesansbold.ttf', 30)
    surfer = font.render('Ctrls: Arrow Keys', True,(255,255,255))
    screen.blit(surfer, recter)
    recter.midtop = (320, 240)
    pygame.display.flip()
    pygame.display.update()
    time.sleep(2)
    surface.fill((0,0,0))
    surfer = font.render('Also, walls don\'t hurt you in this version', True,(255,255,255))
    screen.blit(surfer, recter)
    recter.midtop = (320, 240)
    pygame.display.flip()
    pygame.display.update()
    time.sleep(2)
    surface.fill((0,0,0))
    surfer = font.render('Well, have fun!', True,(255,255,255))
    screen.blit(surfer, recter)
    recter.midtop = (320, 240)
    pygame.display.flip()
    pygame.display.update()
    time.sleep(2)
    surface.fill((0,0,0))
def draw_box(surf, color, pos):
    r = pygame.Rect((pos[0], pos[1]), (GRIDSIZE, GRIDSIZE))
    pygame.draw.rect(surf, color, r)

class Snake(object):
    def __init__(self):
        self.lose()
        self.color = (0,255,0)
        print(self.color)

    def get_head_position(self):
        return self.positions[0]

    def lose(self):
        self.length = 3
        self.positions =  [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
    def point(self, pt):
        if self.length > 3 and (pt[0] * -1, pt[1] * -1) == self.direction:
            return
        else:
            self.direction = pt

    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (((cur[0]+(x*GRIDSIZE)) % SCREEN_WIDTH), (cur[1]+(y*GRIDSIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.lose()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
    
    def draw(self, surf):
        for p in self.positions:
            draw_box(surf, self.color, p)

class Apple(object):
    def __init__(self):
        self.position = (0,0)
        self.color = (255,0,0)
        self.randomize()

    def randomize(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_HEIGHT-1) * GRIDSIZE)

    def draw(self, surf):
        draw_box(surf, self.color, self.position)

def check_eat(snake, apple):
    if snake.get_head_position() == apple.position:
        snake.length += 2
        apple.randomize()
        
if __name__ == '__main__':
    snake = Snake()
    apple = Apple()
    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    snake.point(UP)
                elif event.key == K_DOWN:
                    snake.point(DOWN)
                elif event.key == K_LEFT:
                    snake.point(LEFT)
                elif event.key == K_RIGHT:
                    snake.point(RIGHT)

        
        surface.fill((0,0,0))
        snake.move()
        check_eat(snake, apple)
        snake.draw(surface)
        apple.draw(surface)
        font = pygame.font.Font(None, 36)
        text = font.render(str(snake.length), 1, (255, 255, 255))
        textpos = text.get_rect()
        textpos.centerx = 20
        surface.blit(text, textpos)
        screen.blit(surface, (0,0))

        pygame.display.flip()
        pygame.display.update()
        fpsClock.tick(20)
