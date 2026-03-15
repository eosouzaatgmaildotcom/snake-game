import pygame
import random

# 1. User Preferences
print("--- Snake Game Setup ---")
try:
    user_width = int(input("Enter screen width (e.g., 800): "))
    user_height = int(input("Enter screen height (e.g., 600): "))
    user_speed = int(input("Enter snake speed (Recommended 10-20): "))
except ValueError:
    print("Invalid input. Using default settings: 600x400 at speed 15.")
    user_width, user_height, user_speed = 600, 400, 15

# 2. Initialize Pygame
pygame.init()

# 3. Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 4. Display Setup
screen = pygame.display.set_mode((user_width, user_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
snake_block = 10

# 5. Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 30)

def Your_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    screen.blit(value, [10, 10])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """Calculates the center of the screen to place the text perfectly."""
    mesg = font_style.render(msg, True, color)
    # Get the rectangle of the rendered text to find its width/height
    mesg_rect = mesg.get_rect(center=(user_width / 2, user_height / 2))
    screen.blit(mesg, mesg_rect)

def gameLoop():
    game_over = False
    game_close = False
    paused = False  # New Pause State

    x1 = user_width / 2
    y1 = user_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, user_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, user_height - snake_block) / 10.0) * 10.0

    while not game_over:

        # --- LOSE SCREEN ---
        while game_close == True:
            screen.fill(blue)
            message("Game Over! C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        # --- EVENT HANDLING ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            if event.type == pygame.KEYDOWN:
                # Toggle Pause with 'P'
                if event.key == pygame.K_p:
                    paused = not paused
                
                # Only allow movement if NOT paused
                if not paused:
                    if event.key == pygame.K_LEFT and x1_change == 0:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT and x1_change == 0:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP and y1_change == 0:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN and y1_change == 0:
                        y1_change = snake_block
                        x1_change = 0

        # --- PAUSE LOGIC ---
        if paused:
            message("PAUSED - Press P to Resume", white)
            pygame.display.update()
            clock.tick(5) # Lower CPU usage while paused
            continue # Skip the rest of the movement logic

        # --- GAME LOGIC ---
        if x1 >= user_width or x1 < 0 or y1 >= user_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)
        
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, user_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, user_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(user_speed)

    pygame.quit()
    quit()

if __name__ == "__main__":
    gameLoop()