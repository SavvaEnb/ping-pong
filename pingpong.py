from pygame import *
clock = time.Clock()
speed_x = 3
speed_y = 3
window = display.set_mode((700, 500))
background = transform.scale(
    image.load('табл.webp'),
    (700, 500))




class GameSprite(sprite.Sprite):
    def __init__(self, filename, x, y, speed, sizeX = 65, sizeY = 65):
        super().__init__()
        self.image = transform.scale(image.load(filename), (sizeX, sizeY))
        self.rect = self.image.get_rect()
        self.rect.x = x        
        self.rect.y = y
        self.speed  = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
            
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.direction ='top' 
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        draw.rect(window, (self.color_1, self.color_2, self.color_3), self.rect)
        draw.rect(window, (0,0,0), self.rect, 3)
    
     
    def update(self):
        if self.rect.y <= 0:
            self.direction = 'down'
        elif self.rect.y>= 500 - 230:
            self.direction = 'top'
        if self.direction == 'top':
            self.rect.y -= 3
        else:
            self.rect.y += 3


class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        self.rect.x += speed_x
        self.rect.y += speed_y

        if self.rect.y > 500-50 or self.rect.y < 0:
            speed_y *= -1
        

class Player(GameSprite):
   def update(self):
       keys_pressed = key.get_pressed()
       if keys_pressed[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys_pressed[K_s] and self.rect.y < 500 - 80:
           self.rect.y += self.speed


roket = Player('rocet.png', 15, 400, 5)
ball = Ball('шарик.png', 499 , 100, 5)
w1 = Wall(240, 247, 247, 600, 100 , 10, 230)


font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 80)
# 9, 56, 224,
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER LOSE!', True, (180, 0, 0))

game = True
finish = False
while game:



    if not finish:
        window.blit(background, (0, 0))
        w1.draw_wall()
        roket.update()
        roket.reset()
        ball.update()
        ball.reset()
        w1.update()
        # w1.reset()
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))

    if sprite.collide_rect(roket, ball):
        speed_x *= -1

    if sprite.collide_rect(w1, ball):
        speed_x *= -1



    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(60)
    display.update()
















