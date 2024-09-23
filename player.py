from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from circleshape import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw (self, screen):
        super().draw(screen)
        pygame.draw.polygon (screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:  # move up
            self.move(dt)

        if keys[pygame.K_s]:  # move down
            self.move(-dt)

        if keys[pygame.K_a]:  # rotate left
            self.rotate(-dt)

        if keys[pygame.K_d]:  # rotate right
            self.rotate(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.timer <= 0:
            boom = Shot(self.position.x, self.position.y)
            angle = pygame.Vector2(0, 1).rotate(self.rotation)
            boom.velocity = angle * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN


