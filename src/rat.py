import pygame
import random
from config import rat_squeak_sound

def spawn_rat(screen_width, screen_height, brick_size, rats, holes):
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
    rats.append({'x': x, 'y': y, 'direction': direction})
    holes.append((x, y))
    rat_squeak_sound.play()  # Play rat squeak sound when a rat is spawned

def move_rats(rats, rat_speed, screen_width, screen_height, holes):
    for rat in rats:
        if rat['direction'] == 'down':
            rat['y'] += rat_speed
        elif rat['direction'] == 'up':
            rat['y'] -= rat_speed
        elif rat['direction'] == 'right':
            rat['x'] += rat_speed
        elif rat['direction'] == 'left':
            rat['x'] -= rat_speed
        # Check if rat reaches opposite edge to make a hole and disappear
        if rat['x'] < 0 or rat['x'] > screen_width or rat['y'] < 0 or rat['y'] > screen_height:
            holes.append((rat['x'], rat['y']))
            rats.remove(rat)

def draw_rat(screen, rat, snake_block, shadow_color, eye_color, pupil_color, fang_color, rat_color):
    # Draw shadow
    pygame.draw.ellipse(screen, shadow_color, [rat['x'] + 4, rat['y'] + 4, snake_block, snake_block])
    # Draw rat body
    pygame.draw.ellipse(screen, rat_color, [rat['x'], rat['y'], snake_block, snake_block])
    # Draw rat eyes
    pygame.draw.ellipse(screen, eye_color, [rat['x'] + 4, rat['y'] + 4, 4, 4])
    pygame.draw.ellipse(screen, eye_color, [rat['x'] + snake_block - 8, rat['y'] + 4, 4, 4])
    pygame.draw.ellipse(screen, pupil_color, [rat['x'] + 6, rat['y'] + 6, 2, 2])
    pygame.draw.ellipse(screen, pupil_color, [rat['x'] + snake_block - 6, rat['y'] + 6, 2, 2])
    # Draw rat ears
    pygame.draw.ellipse(screen, rat_color, [rat['x'] + 2, rat['y'] - 4, 6, 6])
    pygame.draw.ellipse(screen, rat_color, [rat['x'] + snake_block - 8, rat['y'] - 4, 6, 6])
    # Draw rat teeth
    pygame.draw.rect(screen, fang_color, [rat['x'] + snake_block // 2 - 2, rat['y'] + 10, 2, 4])
    pygame.draw.rect(screen, fang_color, [rat['x'] + snake_block // 2 + 2, rat['y'] + 10, 2, 4])
    # Draw rat tail
    tail_length = 20
    tail_end_x = rat['x']
    tail_end_y = rat['y'] + tail_length
    pygame.draw.line(screen, rat_color, (rat['x'] + snake_block // 2, rat['y'] + snake_block), (tail_end_x, tail_end_y), 2)
