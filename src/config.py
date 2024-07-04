import pygame

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('3D Look Snake Game with Detailed Rats and Hedgehogs')

# Colors
snake_color = (0, 204, 102)
shadow_color = (50, 50, 50)
apple_color = (204, 0, 0)
leaf_color = (0, 153, 0)
eye_color = (255, 255, 255)
pupil_color = (0, 0, 0)
fang_color = (255, 255, 255)
grass_color = (34, 139, 34)
brick_color = (139, 69, 19)
blood_color = (255, 0, 0)
rat_color = (105, 105, 105)
hedgehog_color = (160, 82, 45)
hole_color = (0, 0, 0)
blink_colors = [(255, 0, 0), (0, 204, 102), (0, 0, 255)]

# Game variables
clock = pygame.time.Clock()
snake_block = 20
snake_normal_speed = 15
snake_slow_speed = 0.75 * snake_normal_speed
snake_speed = snake_normal_speed
rat_speed = 0.75 * snake_normal_speed
hedgehog_speed = 0.75 * snake_normal_speed
brick_size = 20
blood_splatters = []
rats = []
hedgehogs = []
rat_spawn_time = 0
hedgehog_spawn_time = 0
holes = []
blink_start_time = None
blink_duration = 2000  # 2 seconds
blink_phase = 0
blink_interval = 250  # 0.25 second per blink

# Initialize Pygame mixer for sound
pygame.mixer.init()

# Load sounds
crunch_sound = pygame.mixer.Sound("assets/sounds/crunch.mp3")
rat_squish_sound = pygame.mixer.Sound("assets/sounds/rat_squish.mp3")
snake_squish_sound = pygame.mixer.Sound("assets/sounds/snake_squish.mp3")
buzzer_sound = pygame.mixer.Sound("assets/sounds/buzzer.mp3")
rat_squeak_sound = pygame.mixer.Sound("assets/sounds/rat_squeak.mp3")
hedgehog_squeak_sound = pygame.mixer.Sound("assets/sounds/hedgehog_squeak.mp3")
snake_crunch_sound = pygame.mixer.Sound("assets/sounds/snake_crunch.mp3")

# Load images
wood_texture = pygame.image.load("assets/images/wood_texture.png")
grass_texture = pygame.image.load("assets/images/grass_texture.png")
