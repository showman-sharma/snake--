import pygame
import random
import math
from config import hedgehog_squeak_sound

def spawn_hedgehog(screen_width, screen_height, brick_size, hedgehogs, holes):
    edge = random.choice(['top', 'bottom', 'left', 'right'])
    if edge == 'top':
        x, y = random.randint(brick_size, screen_width - brick_size), 0
        direction = 'down'
    elif edge == 'bottom':
        x, y = random.randint(brick_size, screen_width - brick_size), screen_height
        direction = 'up'
    elif edge == 'left':
        x, y = 0, random.randint(brick_size, screen_height - brick_size)
        direction = 'right'
    else:  # right
        x, y = screen_width, random.randint(brick_size, screen_height - brick_size)
        direction = 'left'
    hedgehogs.append({'x': x, 'y': y, 'direction': direction})
    holes.append((x, y))
    hedgehog_squeak_sound.play()  # Play hedgehog squeak sound when a hedgehog is spawned

def move_hedgehogs(hedgehogs, hedgehog_speed, screen_width, screen_height, holes):
    for hedgehog in hedgehogs:
        if hedgehog['direction'] == 'down':
            hedgehog['y'] += hedgehog_speed
        elif hedgehog['direction'] == 'up':
            hedgehog['y'] -= hedgehog_speed
        elif hedgehog['direction'] == 'right':
            hedgehog['x'] += hedgehog_speed
        elif hedgehog['direction'] == 'left':
            hedgehog['x'] -= hedgehog_speed
        # Check if hedgehog reaches opposite edge to make a hole and disappear
        if hedgehog['x'] < 0 or hedgehog['x'] > screen_width or hedgehog['y'] < 0 or hedgehog['y'] > screen_height:
            holes.append((hedgehog['x'], hedgehog['y']))
            hedgehogs.remove(hedgehog)

def draw_hedgehog(screen, hedgehog, snake_block, shadow_color, eye_color, pupil_color, hedgehog_color):
    # Draw shadow
    pygame.draw.ellipse(screen, shadow_color, [hedgehog['x'] + 4, hedgehog['y'] + 4, snake_block, snake_block])
    # Draw hedgehog body
    pygame.draw.ellipse(screen, hedgehog_color, [hedgehog['x'], hedgehog['y'], snake_block, snake_block])
    # Draw hedgehog eyes
    pygame.draw.ellipse(screen, eye_color, [hedgehog['x'] + 4, hedgehog['y'] + 4, 4, 4])
    pygame.draw.ellipse(screen, eye_color, [hedgehog['x'] + snake_block - 8, hedgehog['y'] + 4, 4, 4])
    pygame.draw.ellipse(screen, pupil_color, [hedgehog['x'] + 6, hedgehog['y'] + 6, 2, 2])
    pygame.draw.ellipse(screen, pupil_color, [hedgehog['x'] + snake_block - 6, hedgehog['y'] + 6, 2, 2])
    # Draw spikes
    for i in range(0, 360, 30):
        angle = math.radians(i)
        spike_length = 10
        spike_end_x = hedgehog['x'] + snake_block // 2 + spike_length * math.cos(angle)
        spike_end_y = hedgehog['y'] + snake_block // 2 + spike_length * math.sin(angle)
        pygame.draw.line(screen, hedgehog_color, (hedgehog['x'] + snake_block // 2, hedgehog['y'] + snake_block // 2), (spike_end_x, spike_end_y), 2)
