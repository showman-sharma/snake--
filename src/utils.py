# utils.py

import pygame
import random
import math
from config import *
import csv
import pandas as pd
import os

def draw_grass(screen):
    screen.fill(grass_color)

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
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 5)

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
    text_rect = mesg.get_rect(center=(board_x + board_width // 2, board_y + board_height // 2-30))
    screen.blit(mesg, text_rect)

def draw_ring(screen, x, y, is_mole_hole=False):
    if is_mole_hole:
        pygame.draw.circle(screen, (160, 82, 45), (int(x), int(y)), 10)  # Draw the brown ring
        pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), 5)  # Draw the small black dot inside the ring
    else:
        pygame.draw.circle(screen, (160, 82, 45), (int(x), int(y)), 20)  # Draw the brown ring
        pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), 10)  # Draw the normal black hole

def new_apple_position():
    foodx = round(random.randrange(brick_size, screen_width - snake_block - brick_size) / 20.0) * 20.0
    foody = round(random.randrange(brick_size, screen_height - snake_block - brick_size) / 20.0) * 20.0
    return foodx, foody

def get_high_score(high_score_file=high_score_file):
    if not os.path.exists(high_score_file):
        return 0
    try:
        df = pd.read_csv(high_score_file)
        return df['score'].max()
    except Exception as e:
        print(f"Error reading high score file: {e}")
        return 0

def save_score(name, score, high_score_file=high_score_file):
    if not os.path.exists(high_score_file):
        df = pd.DataFrame(columns=['name', 'score'])
    else:
        df = pd.read_csv(high_score_file)

    new_entry = pd.DataFrame([[name, score]], columns=['name', 'score'])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(high_score_file, index=False)

def get_user_name(screen, wood_texture):
    input_box = pygame.Rect(0, 0, 140, 32)  # Initialize with zero position
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font = pygame.font.Font(None, 32)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        draw_grass(screen)
        draw_wooden_board(screen, wood_texture, "", (255, 0, 0))

        txt_surface = font.render(text, True, pygame.Color('black'))  # Render the text in black
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        input_box.x = (screen.get_width() - input_box.w) // 2  # Center the input box horizontally
        input_box.y = screen.get_height() // 2  # Center the input box vertically

        # Render the "Enter Your Name" message above the input box
        msg_font = pygame.font.Font(None, 50)
        msg_surface = msg_font.render("Enter Your Name:", True, (255, 0, 0))
        msg_x = (screen.get_width() - msg_surface.get_width()) // 2
        msg_y = input_box.y - 50  # Position the message above the input box

        # Draw the message and input box with white background
        screen.blit(msg_surface, (msg_x, msg_y))
        screen.fill((255, 255, 255), input_box)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()

def draw_buttons(screen, button_continue, button_quit):
    pygame.draw.rect(screen, (0, 255, 0), button_continue)
    pygame.draw.rect(screen, (255, 0, 0), button_quit)
    font = pygame.font.Font(None, 35)
    text_continue = font.render('Replay', True, (0, 0, 0))
    text_quit = font.render('Quit', True, (0, 0, 0))
    screen.blit(text_continue, (button_continue.x + 10, button_continue.y + 5))
    screen.blit(text_quit, (button_quit.x + 25, button_quit.y + 5))