import pygame

def draw_snake(screen, snake_list, snake_block, shadow_color, eye_color, pupil_color, fang_color, color):
    for i, (x, y) in enumerate(snake_list):
        # Draw shadow
        pygame.draw.ellipse(screen, shadow_color, [x + 4, y + 4, snake_block, snake_block])
        # Draw snake block with gradient for 3D effect
        pygame.draw.ellipse(screen, color, [x, y, snake_block, snake_block])
        pygame.draw.ellipse(screen, (0, 153, 76), [x, y, snake_block, snake_block], 2)
        
        # Draw eyes and fangs on the head
        if i == len(snake_list) - 1:
            # Eyes
            eye_size = 4
            pygame.draw.ellipse(screen, eye_color, [x + 4, y + 4, eye_size, eye_size])
            pygame.draw.ellipse(screen, eye_color, [x + snake_block - 8, y + 4, eye_size, eye_size])
            pygame.draw.ellipse(screen, pupil_color, [x + 6, y + 6, 2, 2])
            pygame.draw.ellipse(screen, pupil_color, [x + snake_block - 6, y + 6, 2, 2])
            
            # Fangs
            fang_length = 6
            fang_width = 2
            pygame.draw.polygon(screen, fang_color, [(x + 8, y + snake_block // 2), (x + 10, y + snake_block // 2 + fang_length), (x + 6, y + snake_block // 2 + fang_length)])
            pygame.draw.polygon(screen, fang_color, [(x + snake_block - 8, y + snake_block // 2), (x + snake_block - 10, y + snake_block // 2 + fang_length), (x + snake_block - 6, y + snake_block // 2 + fang_length)])
