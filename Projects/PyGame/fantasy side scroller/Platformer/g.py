# main.py
import pygame
import sys

# ---------- Config ----------
WIDTH, HEIGHT = 900, 600
FPS = 60
GRAVITY = 0.8
PLAYER_SPEED = 5
PLAYER_JUMP_SPEED = 16

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
SKY = (135, 206, 235)
GROUND_COLOR = (80, 50, 20)
PLATFORM_COLOR = (100, 100, 100)
ENEMY_COLOR = (180, 50, 50)

# ---------- Helper classes ----------
class Camera:
    """Simple camera that follows the player."""
    def __init__(self, width, height):
        self.offset = pygame.Vector2(0, 0)
        self.width = width
        self.height = height

    def follow(self, target_rect):
        # Keep target near center, but allow offset within bounds
        self.offset.x = target_rect.centerx - WIDTH // 2
        self.offset.y = target_rect.centery - HEIGHT // 2
        # Optional: clamp y to not go below 0 (no negative)
        if self.offset.y < 0:
            self.offset.y = 0
        if self.offset.x < 0:
            self.offset.x = 0

    def apply(self, rect):
        return rect.move(-self.offset.x, -self.offset.y)

# ---------- Game objects ----------
class Platform:
    """A static platform; defined by pygame.Rect in world coordinates."""
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, surf, camera):
        r = camera.apply(self.rect)
        pygame.draw.rect(surf, PLATFORM_COLOR, r)

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 60)
        self.vel = pygame.Vector2(0, 0)
        self.on_ground = False
        # Animation frames simple: colored rectangles or you can load images
        self.flip = False
        self.anim_timer = 0
        self.frame = 0

    def handle_input(self, keys):
        self.vel.x = 0
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.vel.x = -PLAYER_SPEED
            self.flip = True
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.vel.x = PLAYER_SPEED
            self.flip = False
        if (keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]) and self.on_ground:
            self.vel.y = -PLAYER_JUMP_SPEED
            self.on_ground = False

    def apply_gravity(self):
        self.vel.y += GRAVITY
        # optional terminal velocity
        if self.vel.y > 25:
            self.vel.y = 25

    def update(self, platforms):
        # Apply physics
        self.apply_gravity()

        # Horizontal movement and collision
        self.rect.x += int(self.vel.x)
        self._horizontal_collide(platforms)

        # Vertical movement and collision
        self.rect.y += int(self.vel.y)
        self._vertical_collide(platforms)

        # simple animation timer
        self.anim_timer += 1
        if self.anim_timer > 8:
            self.anim_timer = 0
            self.frame = (self.frame + 1) % 4

    def _horizontal_collide(self, platforms):
        for p in platforms:
            if self.rect.colliderect(p.rect):
                if self.vel.x > 0:
                    # moving right -> push player to left side of platform
                    self.rect.right = p.rect.left
                elif self.vel.x < 0:
                    # moving left -> push player to right side
                    self.rect.left = p.rect.right
                self.vel.x = 0

    def _vertical_collide(self, platforms):
        self.on_ground = False
        for p in platforms:
            if self.rect.colliderect(p.rect):
                if self.vel.y > 0:
                    # falling -> landed on top
                    self.rect.bottom = p.rect.top
                    self.vel.y = 0
                    self.on_ground = True
                elif self.vel.y < 0:
                    # rising -> hit head
                    self.rect.top = p.rect.bottom
                    self.vel.y = 0

    def draw(self, surf, camera):
        r = camera.apply(self.rect)
        # Simple placeholder "animated" player using rectangles
        body = pygame.Rect(r.x, r.y, r.width, r.height)
        # change color by frame to show motion
        colors = [(30,144,255),(70,130,180),(65,105,225),(25,25,112)]
        pygame.draw.rect(surf, colors[self.frame], body)
        # draw a "face" to show flip
        eye = pygame.Rect(body.x + (5 if not self.flip else 25), body.y + 15, 8, 8)
        pygame.draw.rect(surf, (255,255,255), eye)

class Enemy:
    """Simple patrol enemy that moves horizontally and collides with platforms."""
    def __init__(self, x, y, w=40, h=40, left_bound=None, right_bound=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = 2
        self.dir = 1
        self.left_bound = left_bound
        self.right_bound = right_bound

    def update(self, platforms):
        self.rect.x += self.speed * self.dir
        # reverse on bounds
        if self.left_bound is not None and self.rect.left < self.left_bound:
            self.rect.left = self.left_bound
            self.dir *= -1
        if self.right_bound is not None and self.rect.right > self.right_bound:
            self.rect.right = self.right_bound
            self.dir *= -1
        # simple gravity so enemy falls off edges properly if needed
        self.rect.y += 3
        # check ground under enemy
        grounded = False
        for p in platforms:
            if self.rect.colliderect(p.rect):
                if self.rect.bottom >= p.rect.top and self.rect.bottom - 3 <= p.rect.top + 10:
                    self.rect.bottom = p.rect.top
                    grounded = True
        if not grounded:
            # fall
            self.rect.y += 5

    def draw(self, surf, camera):
        r = camera.apply(self.rect)
        pygame.draw.rect(surf, ENEMY_COLOR, r)

# ---------- Level data ----------
# Define platforms as (x, y, w, h)
LEVEL_PLATFORMS = [
    (0, 560, 3000, 40),         # ground
    (300, 460, 120, 20),
    (460, 380, 120, 20),
    (640, 300, 120, 20),
    (820, 220, 120, 20),
    (1200, 460, 200, 20),
    (1500, 400, 150, 20),
    (1700, 350, 120, 20),
    (2000, 500, 220, 20),
    (2300, 420, 120, 20),
    (2500, 350, 120, 20),
]

ENEMIES = [
    (500, 340, 450, 700),
    (1600, 360, 1500, 1760),
]

# ---------- Main Game ----------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Platformer Tutorial - Melvin")
    clock = pygame.time.Clock()

    # Create platforms & enemies
    platforms = [Platform(*t) for t in LEVEL_PLATFORMS]
    enemies = [Enemy(x, y, left_bound=lb, right_bound=rb) for (x, y, lb, rb) in ENEMIES]

    player = Player(100, 400)
    camera = Camera(3000, 1200)

    font = pygame.font.SysFont(None, 24)

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # seconds per frame (if needed)

        # --- Input ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.handle_input(keys)

        # --- Update ---
        player.update(platforms)
        for e in enemies:
            e.update(platforms)

        # collision between player and enemies -> simple reset on touch
        for e in enemies:
            if player.rect.colliderect(e.rect):
                # simple death -> reset player position
                player.rect.topleft = (100, 400)
                player.vel = pygame.Vector2(0,0)

        # camera follow
        camera.follow(player.rect)

        # --- Draw ---
        screen.fill(SKY)
        # draw background parallax (simple)
        pygame.draw.rect(screen, (200, 230, 255), camera.apply(pygame.Rect(-500, -500, 3000, 200)))
        # draw platforms
        for p in platforms:
            p.draw(screen, camera)
        # draw enemies
        for e in enemies:
            e.draw(screen, camera)
        # draw player
        player.draw(screen, camera)

        # HUD
        txt = font.render("A/D or ←/→ to move, W / SPACE to jump. Touch enemy = reset.", True, BLACK)
        screen.blit(txt, (10, 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
