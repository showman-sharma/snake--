# game.py

import pygame
import random
from utils import * #draw_grass, draw_brick_fencing, draw_apple, message, create_blood_splatter, draw_blood_splatter, draw_wall_holes, draw_wooden_board, draw_ring, new_apple_position
from snake import draw_snake
from rat import spawn_rat, move_rats, draw_rat
from hedgehog import spawn_hedgehog, move_hedgehogs, draw_hedgehog
from mole import spawn_mole, move_moles, draw_mole
from config import *


def gameLoop():
    global rat_spawn_time, hedgehog_spawn_time, mole_spawn_time, snake_speed, blink_start_time, blink_duration, blink_phase
    game_over = False
    game_close = False

    

    # Pygame initialization
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('3D Look Snake Game')
    clock = pygame.time.Clock()

    welcome_screen(screen, wood_texture)

    user_name = get_user_name(screen, wood_texture)
    
    high_score = get_high_score(high_score_file)
    # high_score = int(high_scores[0][1]) if high_scores else 0

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    holes = []
    blood_splatters = []

    rats = []
    hedgehogs = []
    moles = []

    score = 0

    rat_spawn_time = pygame.time.get_ticks()
    hedgehog_spawn_time = pygame.time.get_ticks()
    mole_spawn_time = pygame.time.get_ticks()

    blink_start_time = None
    blink_duration = 0
    blink_phase = 0
    snake_speed = snake_normal_speed
    
    foodx, foody = new_apple_position()
    button_continue = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 30, 120, 40)
    button_quit = pygame.Rect(screen_width // 2 + 30, screen_height // 2 + 30, 120, 40)

    # Start playing the slither sound in a loop
    pygame.mixer.music.load(snake_slither_sound)
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

    while not game_over:

        while game_close:
            
            pygame.mixer.music.stop()  # Stop the slither sound when the game is over
            draw_grass(screen)
            draw_brick_fencing(screen, brick_size, shadow_color, brick_color)
            draw_blood_splatter(screen, blood_splatters)
            draw_wall_holes(screen, holes)
            # draw_wooden_board(screen, wood_texture, "You Lost! Press Q-Quit or C-Play Again", (255, 0, 0))
            draw_wooden_board(screen, wood_texture, f"SCORE : {score}", (255, 0, 0))
            draw_buttons(screen, button_continue, button_quit)
            pygame.display.update()

            

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        save_score(user_name, score, high_score_file=high_score_file)
                        high_score = get_high_score(high_score_file)
                    if event.key == pygame.K_r:
                        save_score(user_name, score, high_score_file=high_score_file)
                        high_score = get_high_score(high_score_file)
                        gameLoop()
            # for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                    save_score(user_name, score, high_score_file=high_score_file)
                    high_score = get_high_score(high_score_file)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_continue.collidepoint(event.pos):
                        save_score(user_name, score, high_score_file=high_score_file)
                        high_score = get_high_score(high_score_file)
                        gameLoop()
                    if button_quit.collidepoint(event.pos):
                        game_over = True
                        game_close = False
                        save_score(user_name, score, high_score_file=high_score_file)
                        high_score = get_high_score(high_score_file)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                    

        x1 += x1_change
        y1 += y1_change
        
        # Check for collision with the wall
        if x1 >= screen_width - brick_size or x1 < brick_size or y1 >= screen_height - brick_size or y1 < brick_size:
            create_blood_splatter(x1, y1, blood_splatters)
            snake_squish_sound.play()  # Play snake squish sound when the snake crashes into the wall
            game_close = True

        draw_grass(screen)
        draw_brick_fencing(screen, brick_size, shadow_color, brick_color)

        # Draw score and high score
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        high_score_text = font.render(f"High Score: {max(score,high_score)}", True, (255, 255, 255))
        screen.blit(score_text, [10+ brick_size, 10+brick_size])
        screen.blit(high_score_text, [10+brick_size, 40+brick_size])
        
        # Draw rings where moles have spawned or exited
        for hole in holes:
            draw_ring(screen, hole[0], hole[1], is_mole_hole=True)

        draw_blood_splatter(screen, blood_splatters)  # Draw blood splatters before other objects
        draw_wall_holes(screen, holes)
        draw_apple(screen, foodx, foody, shadow_color, apple_color, leaf_color)

        # Handle rats
        if pygame.time.get_ticks() - rat_spawn_time > 5000:  # Spawn a rat every 5 seconds
            spawn_rat(screen_width, screen_height, brick_size, rats, holes)
            rat_spawn_time = pygame.time.get_ticks()

        move_rats(rats, rat_speed, screen_width, screen_height, holes)

        for rat in rats:
            draw_rat(screen, rat, snake_block, shadow_color, eye_color, pupil_color, fang_color, rat_color)
            if abs(rat['x'] - x1) < snake_block and abs(rat['y'] - y1) < snake_block:
                length_of_snake += 2
                score += 2
                create_blood_splatter(rat['x'], rat['y'], blood_splatters)  # Add blood splatter
                rats.remove(rat)
                rat_squish_sound.play()  # Play rat squish sound when the snake eats a rat

        # Handle hedgehogs
        if pygame.time.get_ticks() - hedgehog_spawn_time > 10000:  # Spawn a hedgehog every 10 seconds
            spawn_hedgehog(screen_width, screen_height, brick_size, hedgehogs, holes)
            hedgehog_spawn_time = pygame.time.get_ticks()

        move_hedgehogs(hedgehogs, hedgehog_speed, screen_width, screen_height, holes)

        if blink_start_time and pygame.time.get_ticks() - blink_start_time < blink_duration:
            # Blinking logic
            elapsed_time = pygame.time.get_ticks() - blink_start_time
            blink_phase = (elapsed_time // blink_interval) % 6
            if blink_phase < 4:
                current_color = blink_colors[blink_phase % 2]
            else:
                current_color = blink_colors[2]
            draw_snake(screen, snake_list, snake_block, shadow_color, eye_color, pupil_color, fang_color, current_color)
        else:
            if blink_start_time:
                snake_speed = snake_normal_speed
            blink_start_time = None
            draw_snake(screen, snake_list, snake_block, shadow_color, eye_color, pupil_color, fang_color, snake_color)

        for hedgehog in hedgehogs:
            draw_hedgehog(screen, hedgehog, snake_block, shadow_color, eye_color, pupil_color, hedgehog_color)
            if abs(hedgehog['x'] - x1) < snake_block and abs(hedgehog['y'] - y1) < snake_block:
                blink_start_time = pygame.time.get_ticks()
                snake_speed = snake_slow_speed
                create_blood_splatter(hedgehog['x'], hedgehog['y'], blood_splatters)  # Add blood splatter
                blink_duration = 7000  # 2 seconds for blink + 5 seconds slow
                hedgehogs.remove(hedgehog)
                buzzer_sound.play()  # Play warning buzzer sound when the snake eats a hedgehog

        # Handle moles
        if pygame.time.get_ticks() - mole_spawn_time > 15000:  # Spawn a mole every 15 seconds
            spawn_mole(screen_width, screen_height, brick_size, moles, holes)
            mole_spawn_time = pygame.time.get_ticks()

        move_moles(moles, foodx, foody, holes, lambda: new_apple_position())

        for mole in moles:
            draw_mole(screen, mole, shadow_color, eye_color, pupil_color, mole_color, mole_snout_color, mole_nose_color)
            if abs(mole['x'] - x1) < snake_block and abs(mole['y'] - y1) < snake_block:
                length_of_snake += 1

                create_blood_splatter(mole['x'], mole['y'], blood_splatters)  # Add blood splatter
                moles.remove(mole)
                mole_squeak_sound.play()  # Play mole squeak sound when the snake eats a mole

            if abs(mole['x'] - foodx) < mole_block and abs(mole['y'] - foody) < mole_block:
                foodx, foody = new_apple_position()
                crunch_sound.play()  # Play crunch sound when the mole eats an apple
                holes.append((mole['x'], mole['y']))
                moles.remove(mole)

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                snake_crunch_sound.play()  # Play snake crunch sound when the snake eats itself
                game_close = True

        draw_snake(screen, snake_list, snake_block, shadow_color, eye_color, pupil_color, fang_color, snake_color)  # Draw snake last

        pygame.display.update()

        if abs(x1 - foodx) < snake_block and abs(y1 - foody) < snake_block:
            foodx, foody = new_apple_position()
            length_of_snake += 1
            score += 1
            crunch_sound.play()  # Play crunch sound when the snake eats an apple

        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

if __name__ == "__main__":
    pygame.font.init()  # Initialize the font module
    gameLoop()
