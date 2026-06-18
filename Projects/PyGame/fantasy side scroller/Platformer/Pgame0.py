'''***********************************************************
              PLATFORMER GAME WITH ANIMATED PLAYER
 ************************************************************
 This program uses the Pygame library to create a simple
 2D platformer where a player can move left, right, and jump.
 The world is made of tiles, and the background scrolls slowly
 to simulate movement or depth.
*************************************************************

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
# --- 1. IMPORT PYGAME LIBRARY ---
import pygame  # This is the main game library used for graphics, input, and sound.

# --- 2. INITIALIZE PYGAME ---
pygame.init()  # You must call this before using any Pygame functions.

# --- 3. BASIC CONFIGURATION ---
TILE_SIZE = 50              # Each block (tile) in the world is 50x50 pixels.
WIDTH, HEIGHT = 1000, 1000  # Screen resolution in pixels.
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create a game window.
pygame.display.set_caption("Platformer with Animated Player")  # Window title.
clock = pygame.time.Clock()  # Used to control the frame rate (FPS).

# ============================================================
# 4. LOAD IMAGES USED IN THE GAME
# ============================================================

# Create a dictionary that stores all game images.
# Each key represents the tile type or object name.
images = {
    "bg": pygame.image.load("img/sky.png").convert(),  # Background image
    "sun": pygame.image.load("img/sun.png").convert_alpha(),  # Sun (with transparency)
    1: pygame.transform.scale(pygame.image.load("img/dirt.png"), (TILE_SIZE, TILE_SIZE)),  # Dirt tile
    2: pygame.transform.scale(pygame.image.load("img/grass.png"), (TILE_SIZE, TILE_SIZE))  # Grass tile
}

# The background image is resized to fit the whole screen.
images["bg"] = pygame.transform.scale(images["bg"], (WIDTH, HEIGHT))

# ============================================================
# 5. WORLD DATA MATRIX
# ============================================================
# Each number represents a different type of tile in the level.
# 0 = empty space (no block)
# 1 = dirt tile
# 2 = grass tile
# The game will draw a block wherever a 1 or 2 appears.

world_data = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0],
    [1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# ============================================================
# 6. CREATE WORLD TILE OBJECTS
# ============================================================
# This creates a list called "tiles" that stores both:
# - the image to draw
# - the rectangular area (Rect) for each tile
# The Rect helps detect collisions with the player.

tiles = [
    (images[tile], pygame.Rect(col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))
    for row, line in enumerate(world_data)     # Go through each row
    for col, tile in enumerate(line)           # Go through each column
    if tile in images                          # Only draw valid tiles (1 or 2)
]

# ============================================================
# 7. HELPER FUNCTION TO DRAW GRID (OPTIONAL)
# ============================================================
# This is useful for debugging — it shows the boundaries of each tile.
def draw_grid():
    for i in range(0, WIDTH, TILE_SIZE):
        pygame.draw.line(screen, (255,255,255), (i,0), (i,HEIGHT))  # Vertical lines
        pygame.draw.line(screen, (255,255,255), (0,i), (WIDTH,i))   # Horizontal lines

# ============================================================
# 8. BACKGROUND ANIMATION SETTINGS
# ============================================================
scroll = 0          # Current scroll position (x offset)
scroll_speed = 0.3  # How fast the background moves

# ============================================================
# 9. PLAYER SETTINGS AND PHYSICS VARIABLES
# ============================================================
player_x, player_y = 200, 200  # Initial position of the player on the screen
player_vel_y = 0               # Vertical velocity (used for jumping and gravity)
player_speed = 5               # Movement speed (left/right)
gravity = 0.5                  # How strong gravity pulls down
jump_power = -10               # The upward velocity when the player jumps
on_ground = False              # Keeps track of whether player is standing on a block
facing_right = True            # Used to flip the sprite direction
player_frame = 0               # Current frame for the running animation
player_frame_speed = 0.15      # Controls how fast the running animation changes frames

# ============================================================
# 10. LOAD PLAYER IMAGES
# ============================================================
# Idle = standing still

player_idle = pygame.image.load("img/player/idle.png").convert_alpha()


# Run = list of 3 images (frames)
player_run = [pygame.image.load(f"img/player/run{i}.png").convert_alpha() for i in range(1,4)]



# Jump = image used while in the air
player_jump = pygame.image.load("img/player/jump.png").convert_alpha()
# Start with the idle image
player_image = player_idle

# ============================================================
# 11. MAIN GAME LOOP
# ============================================================
# The game keeps running until 'run' becomes False (for example, when you close the window)
run = True
while run:
    clock.tick(60)  # Limit the frame rate to 60 frames per second
    screen.fill((0,0,0))  # Clear the screen with black color before drawing everything

    # --- BACKGROUND SCROLLING ---
    # Draw two backgrounds next to each other to create an infinite scrolling effect.
    screen.blit(images["bg"], (scroll, 0))
    screen.blit(images["bg"], (scroll + WIDTH, 0))
    scroll -= scroll_speed  # Move the background slowly to the left
    if abs(scroll) > WIDTH:
        scroll = 0  # Reset scroll when one image has moved out of view

    # --- DRAW SUN ---
    screen.blit(images["sun"], (100, 100))  # Just for decoration

    # --- DRAW WORLD (TILES) ---
    for img, rect in tiles:
        screen.blit(img, rect)

    # --- OPTIONAL DEBUG GRID ---
    draw_grid()

    # ========================================================
    # 12. PLAYER INPUT (MOVEMENT)
    # ========================================================
    keys = pygame.key.get_pressed()  # Check which keys are being pressed right now

    # Move left
    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    # Move right
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Jump only when on the ground
    if keys[pygame.K_SPACE] and on_ground:
        player_vel_y = jump_power
        on_ground = False  # Player is now in the air

    # ========================================================
    # 13. APPLY GRAVITY AND UPDATE PLAYER POSITION
    # ========================================================
    player_vel_y += gravity   # Add gravity to vertical velocity
    player_y += player_vel_y  # Apply vertical movement

    # ========================================================
    # 14. COLLISION DETECTION WITH TILES
    # ========================================================
    # Check if player touches the ground (any solid tile)
    on_ground = False  # Reset before checking
    player_rect = pygame.Rect(player_x, player_y, player_idle.get_width(), player_idle.get_height())

    for _, tile_rect in tiles:
        if player_rect.colliderect(tile_rect):  # If rectangles overlap, there is a collision
            # If player is falling down and hits the top of a block
            if player_vel_y > 0 and player_rect.bottom <= tile_rect.bottom:
                player_y = tile_rect.top - player_rect.height  # Place player on top of the block
                player_vel_y = 0                               # Stop vertical movement
                on_ground = True                               # Mark player as on the ground

    # ========================================================
    # 15. PLAYER ANIMATION LOGIC
    # ========================================================
    if not on_ground:
        # If the player is jumping or falling, show jump sprite
        player_image = player_jump
    else:
        # If player is moving left or right, play running animation
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            player_frame += player_frame_speed
            # Loop animation frames (0,1,2)
            if player_frame >= len(player_run):
                player_frame = 0
            player_image = player_run[int(player_frame)]
        else:
            # Standing still
            player_image = player_idle

    # ========================================================
    # 16. FLIP PLAYER IMAGE BASED ON MOVEMENT DIRECTION
    # ========================================================
    if keys[pygame.K_LEFT]:
        facing_right = False
    elif keys[pygame.K_RIGHT]:
        facing_right = True

    # If facing left, flip the image horizontally
    if not facing_right:
        player_image = pygame.transform.flip(player_image, True, False)

    # ========================================================
    # 17. DRAW PLAYER ON SCREEN
    # ========================================================
    screen.blit(player_image, (player_x, player_y))

    # ========================================================
    # 18. EVENT HANDLING
    # ========================================================
    for event in pygame.event.get():
        # If the user clicks the "X" button, close the game
        if event.type == pygame.QUIT:
            run = False

    # ========================================================
    # 19. UPDATE SCREEN
    # ========================================================
    pygame.display.flip()  # Refresh the screen and show the new frame

# ============================================================
# 20. EXIT GAME
# ============================================================
pygame.quit()  # Properly close the Pygame window and end the program
