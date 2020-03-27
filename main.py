# Snake game by Aslan Aliyev

import pygame
import random
import math
import operator

# Initialise the pygame
pygame.init()

# Pygame window features
(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))

# Name of the game icon
icon = pygame.image.load("snake.png")
pygame.display.set_caption("Smart Python")
pygame.display.set_icon(icon)

# Screen colour
screen_color = [0, 0, 0]
snake_block = 20
# Draw a snake
red_dot = (255, 0, 0)
snake_position_y = 240
snake_position_x = 240
y_increase = 20
x_increase = 0
#
white_color = (255,255,255)
blue = (0,0,255)
black_dot = (0, 0, 0)
# Draw a bite
black_dot = (0, 0, 0)
bite_position_y = random.randint(0,400)
bite_position_10_y = bite_position_y % 20
bite_position_y -= bite_position_10_y
print(bite_position_y)
bite_position_x = random.randint(0,400)
bite_position_10_x = bite_position_x % 20
bite_position_x -= bite_position_10_x
print(bite_position_x)

# Screen grids. Size of grids (width, height)
width_grid = 20
height_grid = 20
color = [0, 0, 0]

# create block size of square
block_size = 19
# Distance between snake and worm
def collision(snake_pos_x, snake_pos_y, worm_pos_x, worm_pos_y):
    distance = math.sqrt(math.pow(snake_pos_x-worm_pos_x,2) + math.pow(snake_pos_y - worm_pos_y,2))
    if distance < 20:
        return True
    else:
        return False

#
snake_list = []
length_of_snake = 1
# Define function for snake
def best_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, white_color, [x[0], x[1], snake_block, snake_block])

############# Loop for creating a window (prevent from disappearing) ####################################
running = True
while running:
    screen.fill(blue)
    for event in pygame.event.get():
        # Activate close button
        if event.type == pygame.QUIT:
            running = False
        # Control the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_increase = -snake_block
                y_increase = 0
            elif event.key == pygame.K_RIGHT:
                x_increase = snake_block
                y_increase = 0
            elif event.key == pygame.K_UP:
                y_increase = -snake_block
                x_increase = 0
            elif event.key == pygame.K_DOWN:
                y_increase = snake_block
                x_increase = 0

    #Create grids on the screen
    for row in range(height):
        for column in range(width):
            rect = pygame.Rect(column * (block_size + 1), row * (block_size + 1), block_size, block_size)
            pygame.draw.rect(screen, color, rect)

    # create snake on the screen
    snake_position_y += y_increase
    snake_position_x += x_increase
    print(snake_position_x)

    if snake_position_x > width or snake_position_x < 0 or snake_position_y > height or snake_position_y < 0:
        running = False

    #pygame.draw.rect(screen, red_dot, pygame.Rect(snake_position_x, snake_position_y, snake_block, snake_block))
    # Draw a bite on the screen
    pygame.draw.rect(screen, red_dot, pygame.Rect(bite_position_x, bite_position_y, snake_block, snake_block))
    #
    snake_head =[]
    snake_head.append(snake_position_x)
    snake_head.append(snake_position_y)
    snake_list.append(snake_head)

    if len(snake_list) > length_of_snake:
        del snake_list[0]

    best_snake(snake_block, snake_list)



    #####
    colision_state = collision(snake_position_x, snake_position_y, bite_position_x, bite_position_y)
    # Snake reaches the worm, create again
    if colision_state == True:
        bite_position_y = random.randint(0, 400)
        bite_position_10_y = bite_position_y % 20
        bite_position_y -= bite_position_10_y
        bite_position_x = random.randint(0, 400)
        bite_position_10_x = bite_position_x % 20
        bite_position_x -= bite_position_10_x
        pygame.draw.rect(screen, red_dot, pygame.Rect(bite_position_x, bite_position_y, snake_block, snake_block))
        length_of_snake += 1
        # Add a new segment



    # Update every iteration to have a motion
    pygame.display.update()

a = (5, 5)
b = (5, 5)
c = a + b
k = tuple(map(operator.add, a, b))
print(k)
