import pygame
import random
import math
from config import *

def spawn_mole(screen_width, screen_height, brick_size, moles, holes):
    x, y = random.randint(brick_size, screen_width - brick_size), random.randint(brick_size, screen_height - brick_size)
    direction = random.choice(['left', 'right', 'up', 'down'])
    moles.append({'x': x, 'y': y, 'direction': direction})
    holes.append((x, y))
    mole_squeak_sound.play()  # Play mole squeak sound when a mole is spawned

def move_moles(moles, foodx, foody, holes, new_apple_position_callback):
    for mole in moles:
        # if mole['target'] is None:
        #     mole['target'] = (foodx, foody)
        target_x, target_y = (foodx, foody)#mole['target']
        if mole['x'] < target_x:
            mole['x'] += mole_speed
        elif mole['x'] > target_x:
            mole['x'] -= mole_speed
        if mole['y'] < target_y:
            mole['y'] += mole_speed
        elif mole['y'] > target_y:
            mole['y'] -= mole_speed


def draw_mole(screen, mole, shadow_color, eye_color, pupil_color, mole_color, mole_snout_color, mole_nose_color):
    # Draw shadow
    pygame.draw.ellipse(screen, shadow_color, [mole['x'] + 4, mole['y'] + 4, snake_block, snake_block])
    # Draw mole body
    pygame.draw.ellipse(screen, mole_color, [mole['x'], mole['y'], snake_block, snake_block])
    # Draw mole eyes
    pygame.draw.ellipse(screen, eye_color, [mole['x'] + 4, mole['y'] + 4, 4, 4])
    pygame.draw.ellipse(screen, eye_color, [mole['x'] + snake_block - 8, mole['y'] + 4, 4, 4])
    pygame.draw.ellipse(screen, pupil_color, [mole['x'] + 6, mole['y'] + 6, 2, 2])
    pygame.draw.ellipse(screen, pupil_color, [mole['x'] + snake_block - 6, mole['y'] + 6, 2, 2])
    # Draw mole snout
    pygame.draw.ellipse(screen, mole_snout_color, [mole['x'] + snake_block // 2 - 4, mole['y'] + snake_block // 2, 8, 8])
    pygame.draw.circle(screen, mole_nose_color, [mole['x'] + snake_block // 2, mole['y'] + snake_block // 2 + 4], 2)
    # Draw mole hands
    pygame.draw.rect(screen, mole_color, [mole['x'] - 4, mole['y'] + snake_block // 2 - 2, 4, 8])
    pygame.draw.rect(screen, mole_color, [mole['x'] + snake_block, mole['y'] + snake_block // 2 - 2, 4, 8])

def draw_ring(screen, x, y, is_mole_hole=False):
    if is_mole_hole:
        pygame.draw.circle(screen, ring_color, (int(x), int(y)), 10, 10)  # Draw the brown ring
        pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), 5)  # Draw the small black dot inside the ring
    else:
        pygame.draw.circle(screen, ring_color, (int(x), int(y)), 20, 20)  # Draw the brown ring
        pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), 10)  # Draw the normal black hole
