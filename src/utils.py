import pygame
import random
import math

# Utility functions
def draw_grass(screen):
    screen.fill((34, 139, 34))

def draw_brick_fencing(screen, brick_size, shadow_color, brick_color):
    for x in range(0, screen.get_width(), brick_size):
        pygame.draw.rect(screen, brick_color, [x, 0, brick_size, brick_size])
        pygame.draw.rect(screen, brick_color, [x, screen.get_height() - brick_size, brick_size, brick_size])
        pygame.draw.rect(screen, shadow_color, [x + 2, 2, brick_size - 4, brick_size - 4], 1)
        pygame.draw.rect(screen, shadow_color, [x + 2, screen.get_height() - brick_size + 2, brick_size - 4, brick_size - 4], 1)
    for y in range(0, screen.get_height(), brick_size):
        pygame.draw.rect(screen, brick_color, [0, y, brick_size, brick_size])
        pygame.draw.rect(screen, brick_color, [screen.get_width() - brick_size, y, brick_size, brick_size])
        pygame.draw.rect(screen, shadow_color, [2, y + 2, brick_size - 4, brick_size - 4], 1)
        pygame.draw.rect(screen, shadow_color, [screen.get_width() - brick_size + 2, y + 2, brick_size - 4, brick_size - 4], 1)

def draw_apple(screen, x, y, shadow_color, apple_color, leaf_color):
    # Draw shadow
    pygame.draw.ellipse(screen, shadow_color, [x + 4, y + 4, 20, 20])
    # Draw apple body
    pygame.draw.ellipse(screen, apple_color, [x, y, 20, 20])
    # Draw apple leaf
    pygame.draw.polygon(screen, leaf_color, [(x + 10, y), (x + 15, y - 10), (x + 5, y - 10)])

def message(screen, msg, color):
    font = pygame.font.SysFont(None, 50)
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [screen.get_width() / 6, screen.get_height() / 3])

def create_blood_splatter(x, y, blood_splatters):
    for _ in range(20):
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(5, 15)
        blood_x = x + radius * math.cos(angle)
        blood_y = y + radius * math.sin(angle)
        blood_splatters.append((blood_x, blood_y))

def draw_blood_splatter(screen, blood_splatters):
    for blood_x, blood_y in blood_splatters:
        pygame.draw.circle(screen, (255, 0, 0), (int(blood_x), int(blood_y)), 3)

def draw_wall_holes(screen, holes):
    for x, y in holes:
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 10)

def draw_wooden_board(screen, wood_texture, msg, color):
    board_width = 400
    board_height = 200
    board_x = (screen.get_width() - board_width) // 2
    board_y = (screen.get_height() - board_height) // 2

    # Draw the wooden board
    wood_texture = pygame.transform.scale(wood_texture, (board_width, board_height))
    screen.blit(wood_texture, (board_x, board_y))

    # Draw the message on the wooden board
    font = pygame.font.SysFont(None, 30)
    mesg = font.render(msg, True, color)
    text_rect = mesg.get_rect(center=(board_x + board_width // 2, board_y + board_height // 2))
    screen.blit(mesg, text_rect)
