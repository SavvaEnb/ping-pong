from pygame import *
clock = time.Clock()
window = display.set_mode((700, 500))
background = transform.scale(
    image.load('images.webp'),
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
   def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        draw.rect(window, (self.color_1, self.color_2, self.color_3), self.rect)
      


class Player(GameSprite):
   def update(self):
       keys_pressed = key.get_pressed()
       if keys_pressed[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys_pressed[K_s] and self.rect.y < 500 - 80:
           self.rect.y += self.speed


roket = Player('rocet.png', 15, 400, 5)

w1 = Wall(154, 205, 50, 600, 100 , 10, 230)

game = True
finish = False
while game:

    if not finish:
        window.blit(background, (0, 0))
        w1.draw_wall()
        roket.update()
        roket.reset()


    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(60)
    display.update()
