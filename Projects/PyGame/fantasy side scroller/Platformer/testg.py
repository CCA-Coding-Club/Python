import pygame
pygame.init()

# --- CONFIG ---
TILE = 50; WIDTH = HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# --- IMÁGENES ---
images = {
    "bg": pygame.transform.scale(pygame.image.load("img/sky.png").convert(), (WIDTH, HEIGHT)),
    "sun": pygame.image.load("img/sun.png").convert_alpha(),
    1: pygame.transform.scale(pygame.image.load("img/dirt.png"), (TILE,TILE)),
    2: pygame.transform.scale(pygame.image.load("img/grass.png"), (TILE,TILE))
}
def load_scaled(path,size): return pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), size)

# --- DATOS DEL MUNDO (DISEÑO MEJORADO) ---
world = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,2,2,2,2,2,2,0,0,0,0,0,0,2,2,2,2,2,2,1],
    [1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

tiles = [(images[t], pygame.Rect(c*TILE,r*TILE,TILE,TILE))
          for r,row in enumerate(world) for c,t in enumerate(row) if t in images]

# --- CLASE JUGADOR ---
class Player:
    def __init__(self,pos=(100,800)): # ¡POSICIÓN INICIAL AJUSTADA!
        size=(60,80)
        self.imgs = {"idle":load_scaled("img/player/idle.png",size),
                      "jump":load_scaled("img/player/jump.png",size),
                      "run":[load_scaled(f"img/player/run{i}.png",size) for i in range(1,4)]}
        self.rect = self.imgs["idle"].get_rect(topleft=pos)
        self.vel_y = 0
        self.speed = 5
        self.gravity = 0.5
        self.jump = -10
        self.on_ground = False
        self.facing = True
        self.frame = 0
        self.frame_speed = 0.15
        
    def update(self,keys,tiles):
        dx = (keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*self.speed
        if keys[pygame.K_SPACE] and self.on_ground: 
            self.vel_y = self.jump
            self.on_ground = False
        
        # 1. MOVIMIENTO Y COLISIÓN HORIZONTAL (EJE X)
        self.rect.x += dx
        for _,t in tiles:
            if self.rect.colliderect(t):
                if dx > 0: 
                    self.rect.right = t.left 
                elif dx < 0: 
                    self.rect.left = t.right 

        # 2. MOVIMIENTO Y COLISIÓN VERTICAL (EJE Y)
        self.vel_y += self.gravity
        self.rect.y += self.vel_y
        self.on_ground = False 

        for _,t in tiles:
            if self.rect.colliderect(t):
                if self.vel_y > 0: # Cayendo (Colisión con el suelo)
                    self.rect.bottom = t.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0: # Subiendo (Colisión con el techo)
                    self.rect.top = t.bottom
                    self.vel_y = 0
                    
        # 3. ANIMACIÓN Y DIBUJO
        moving = dx!=0
        if not self.on_ground: img=self.imgs["jump"]
        elif moving: self.frame=(self.frame+self.frame_speed)%len(self.imgs["run"]); img=self.imgs["run"][int(self.frame)]
        else: img=self.imgs["idle"]
        
        if dx != 0: 
            self.facing = dx > 0
            
        if not self.facing: img=pygame.transform.flip(img,True,False)

        screen.blit(img,img.get_rect(midbottom=self.rect.midbottom))

player = Player()
scroll = 0; scroll_speed=0.3

# --- BUCLE PRINCIPAL ---
running=True
while running:
    clock.tick(60)
    scroll=(scroll-scroll_speed)%WIDTH
    
    # Dibujo del fondo
    screen.blit(images["bg"],(scroll-WIDTH,0))
    screen.blit(images["bg"],(scroll,0))
    screen.blit(images["sun"],(100,100))
    
    # Dibujo de los bloques
    for img,t in tiles: screen.blit(img,t)
    
    # Dibujo de la cuadrícula (para debug)
    for i in range(0,WIDTH,TILE):
        pygame.draw.line(screen,(255,255,255),(i,0),(i,HEIGHT))
        pygame.draw.line(screen,(255,255,255),(0,i),(WIDTH,i))
        
    # Lógica del jugador
    keys=pygame.key.get_pressed()
    player.update(keys,tiles)
    
    # Manejo de eventos
    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False
        
    pygame.display.flip()
    
pygame.quit()