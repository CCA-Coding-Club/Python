# platformer_english.py
# Simple Platformer Game made with Pygame
# Controls: Left/Right arrows or A/D to move, Space to jump
''' 
cd ~/Desktop/code
python3 -m venv venv
python3 -m venv venv
source venv/bin/activate
(venv) gtz@gtz-Latitude-7400:~/Desktop/code$
pip install pygame
Successfully installed pygame-2.6.1
python3 Mygame.py
deactivate
'''
import pygame       # Import pygame for making games
import sys          # Import sys to allow exiting the game

# -------- CONSTANTS -----------
WIDTH, HEIGHT = 800, 600       # Screen width and height
FPS = 60                       # Frames per second (game speed)
GRAVITY = 0.8                  # Gravity pulling the player down
PLAYER_SPEED = 5               # Horizontal movement speed
JUMP_SPEED = 15                # Jump force
WHITE = (255,255,255)          # Color white
BLACK = (0,0,0)                # Color black
BLUE = (60,130,200)            # Player color
GREEN = (80,180,100)           # Platform color
YELLOW = (255,215,0)           # Star color

# -------- CLASSES ------------

class Platform(pygame.sprite.Sprite):  # Class for solid platforms
    def __init__(self, x, y, w, h):
        super().__init__()                                   # Initialize parent class
        self.image = pygame.Surface((w, h))                   # Create a rectangular surface
        self.image.fill(GREEN)                                # Fill it with green
        self.rect = self.image.get_rect(topleft=(x, y))       # Position of the platform


class Player(pygame.sprite.Sprite):  # Class for the player
    def __init__(self, x, y):
        super().__init__()                                   # Initialize parent class
        self.image = pygame.Surface((40, 60))                 # Player shape (rectangle)
        self.image.fill(BLUE)                                # Fill with blue color
        self.rect = self.image.get_rect(topleft=(x, y))       # Set position
        self.vel_x = 0                                       # Horizontal velocity
        self.vel_y = 0                                       # Vertical velocity
        self.on_ground = False                               # Check if standing on a platform

    def update(self, platforms):
        keys = pygame.key.get_pressed()                      # Get pressed keys
        self.vel_x = 0                                       # Reset horizontal speed

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:          # Move left
            self.vel_x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:         # Move right
            self.vel_x = PLAYER_SPEED

        self.rect.x += self.vel_x                            # Apply horizontal movement
        self.collide(self.vel_x, 0, platforms)               # Handle side collisions

        self.vel_y += GRAVITY                                # Apply gravity
        if self.vel_y > 25:                                  # Limit falling speed
            self.vel_y = 25
        self.rect.y += int(self.vel_y)                       # Apply vertical movement
        self.on_ground = False                               # Assume falling
        self.collide(0, self.vel_y, platforms)               # Handle vertical collisions

    def jump(self):
        if self.on_ground:                                   # Jump only if on the ground
            self.vel_y = -JUMP_SPEED                         # Apply jump velocity
            self.on_ground = False                           # Now in the air

    def collide(self, vel_x, vel_y, platforms):              # Collision detection
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform):    # Check overlap
                if vel_x > 0: self.rect.right = platform.rect.left   # Hit right side
                if vel_x < 0: self.rect.left = platform.rect.right   # Hit left side
                if vel_y > 0:                                   # Falling down
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True                       # Landed
                if vel_y < 0:                                   # Hitting from below
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0


class Star(pygame.sprite.Sprite):  # Class for the collectible goal
    def __init__(self, x, y):
        super().__init__()                                   # Initialize parent class
        self.image = pygame.Surface((24, 24))                # Create star shape
        self.image.fill(YELLOW)                              # Fill with yellow
        self.rect = self.image.get_rect(center=(x, y))       # Set position


# -------- FUNCTIONS ----------

def create_level():                                          # Function to build level
    platforms = pygame.sprite.Group()                        # Create platform group
    platforms.add(Platform(0, HEIGHT - 40, WIDTH, 40))       # Ground
    platforms.add(Platform(50, 450, 150, 20))                # Floating platforms
    platforms.add(Platform(260, 360, 140, 20))
    platforms.add(Platform(460, 300, 120, 20))
    platforms.add(Platform(620, 220, 130, 20))
    platforms.add(Platform(350, 520, 200, 20))
    return platforms


def main():                                                  # Main game function
    pygame.init()                                            # Initialize pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))        # Create window
    pygame.display.set_caption("Mini Platformer")            # Set title
    clock = pygame.time.Clock()                              # Control frame rate
    font = pygame.font.SysFont(None, 36)                     # Create font for text

    player = Player(100, HEIGHT - 120)                       # Create player
    player_group = pygame.sprite.GroupSingle(player)         # Player group

    platforms = create_level()                               # Create platforms
    stars = pygame.sprite.Group()                            # Create star group
    star = Star(680, 190)                                    # Place one star
    stars.add(star)

    won = False                                              # Track win condition

    while True:                                              # Game loop
        dt = clock.tick(FPS)                                 # Maintain FPS

        for event in pygame.event.get():                     # Event handling
            if event.type == pygame.QUIT:                    # Window closed
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:                 # Key pressed
                if event.key == pygame.K_SPACE:              # Space to jump
                    player.jump()
                if event.key == pygame.K_r and won:          # R to restart
                    player.rect.topleft = (100, HEIGHT - 120)
                    player.vel_x = player.vel_y = 0
                    won = False
                    stars.empty()
                    stars.add(Star(680, 190))

        if not won:                                          # Update only if not won
            player_group.update(platforms)                   # Update player

            if pygame.sprite.spritecollide(player, stars, dokill=True):  # Touch star
                won = True                                   # Win condition

        screen.fill(WHITE)                                   # Clear screen
        platforms.draw(screen)                               # Draw platforms
        stars.draw(screen)                                   # Draw star
        player_group.draw(screen)                            # Draw player

        if won:                                              # Show messages
            text = font.render("You got the star! Press R to play again.", True, BLACK)
            screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 20))
        else:
            instr = font.render("Arrows/A-D to move, Space to jump", True, BLACK)
            screen.blit(instr, (10, 10))

        pygame.display.flip()                                # Refresh screen


if __name__ == "__main__":                                  # Run only if main file
    main()                                                   # Start the game




