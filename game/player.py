import pygame

class player:
    def __init__(self):
        self.idle_image = pygame.image.load("assets/player/eggidle.png").convert_alpha()
        self.moving_images = []
        for i in range(1, 5):
            image = pygame.image.load(f"assets/player/moving/eggroll{i}.png").convert_alpha()
            self.moving_images.append(image)
        self.image = self.idle_image

        self.x = 400
        self.speed = 5

        self.floor_y = 600
        self.y = self.floor_y - self.idle_image.get_height()

        self.y_velocity = 0
        self.gravity = 0.5
        self.jump_strength = -12
        self.on_floor = True

        self.moving = False
        self.animation_index = 0
        self.animation_timer = 0
        self.animation_speed = 150

    @property # please dont touch this i forgot waht it does but its important
    def rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))

    def movement(self):
        keys = pygame.key.get_pressed()
        self.moving = False
        if keys[pygame.K_a]:
            self.x -= self.speed
            self.moving = True
        if keys[pygame.K_d]:
            self.x += self.speed
            self.moving = True

    def jump(self):
        if self.on_floor:
            self.y_velocity = self.jump_strength
            self.on_floor = False

    def apply_gravity(self, dt):

        frame_time = dt / 16.67
        self.y_velocity += self.gravity * frame_time
        self.y += self.y_velocity * frame_time
        player_height = self.idle_image.get_height()

        if self.y + player_height >= self.floor_y:
            self.y = self.floor_y - player_height
            self.y_velocity = 0
            self.on_floor = True
        else:
            self.on_floor = False

    def animation(self, dt):
        if self.moving:
            self.animation_timer += dt
            if self.animation_timer >= self.animation_speed:
                self.animation_index += 1
                if self.animation_index >= len(self.moving_images):
                    self.animation_index = 0
                self.animation_timer = 0
            self.image = self.moving_images[self.animation_index]
        else:
            self.image = self.idle_image
            self.animation_index = 0
            self.animation_timer = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
