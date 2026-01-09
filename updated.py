import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen
WIDTH, HEIGHT = 1100, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy by Dagi")
FPS = 50

# Colors
WHITE = (255, 255, 255)
GRAY= (122, 122, 122)
BLACK = (0, 0, 0)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("Georgia", 40)

# Bird properties
bird_x = 400
bird_radius = 30
gravity = 0.5
jump_strength = -6

# Pipe properties
pipe_width = 60
pipe_gap = 160
pipe_velocity = 7

# LEARNING QUESTION SYSTEM
def ask_learning_question():
    #Ask simple learning questions to allow restart.
    questions = [
        ("5 + 3 = ?", "8"),
        ("9 - 4 = ?", "5"),
        ("8 * 8 = ?", "64"),
        ("What planet do we live on?", "earth"),
        ("What do plants need? (sun or milk)", "sun"),
        ("What gas do humans breathe in? (oxygen or helium)", "oxygen"),
    ]

    question, answer = random.choice(questions)
    user_input = ""

    while True:
        screen.fill(GRAY)

        q_text = font.render(question, True, WHITE)
        screen.blit(q_text, (WIDTH // 2 - q_text.get_width() // 2, HEIGHT // 2 - 50))

        instructions = font.render("Type answer + Enter", True, WHITE)
        screen.blit(instructions, (WIDTH // 2 - instructions.get_width() // 2, HEIGHT // 2))

        input_text = font.render(user_input, True, WHITE)
        screen.blit(input_text, (WIDTH // 2 - input_text.get_width() // 2, HEIGHT // 2 + 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return user_input.lower() == answer.lower()

                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

#Display Game Over screen and allow restart or quit.
def game_over_screen(Score):
    while True:
        screen.fill(GRAY)

        game_over_text = font.render("GAME OVER!", True, WHITE)
        score_text = font.render(f"Score: {Score}", True, WHITE)
        learn_text = font.render("Solve a question to restart!", True, WHITE)
        continue_text = font.render("Press L to learn OR Q to quit", True, WHITE)

        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 120))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 70))
        screen.blit(learn_text, (WIDTH // 2 - learn_text.get_width() // 2, HEIGHT // 2 - 20))
        screen.blit(continue_text, (WIDTH // 2 - continue_text.get_width() // 2, HEIGHT // 2 + 30))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    if ask_learning_question():
                        return  # restart game
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# MAIN GAME LOOP + RESTART SUPPORT
def run_game():
    # Bird setup
    bird_y = HEIGHT // 2
    bird_velocity = 0

    # Pipe setup
    pipes = [create_pipe()]

    Score = 0

    running = True
    while running:
        screen.fill(GRAY)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

        # Bird physics
        bird_velocity += gravity
        bird_y += bird_velocity

        pygame.draw.circle(screen, WHITE,(bird_x, int(bird_y)), bird_radius)

        # Move and draw pipes
        for pipe in pipes:
            pipe[0].x -= pipe_velocity
            pipe[1].x -= pipe_velocity
            pygame.draw.rect(screen, BLACK, pipe[0])
            pygame.draw.rect(screen, BLACK, pipe[1])

        # Add & remove pipes
        if pipes[-1][0].x < WIDTH // 2:
            pipes.append(create_pipe())

        if pipes[0][0].x + pipe_width < 0:
            pipes.pop(0)
            Score += 1

        # Collision detection
        bird_rect = pygame.Rect(bird_x - bird_radius, bird_y - bird_radius, bird_radius * 2, bird_radius * 2)
        for pipe in pipes:
            if pipe[0].colliderect(bird_rect) or pipe[1].colliderect(bird_rect):
                return Score

        # Screen bounds
        if bird_y - bird_radius < 0 or bird_y + bird_radius > HEIGHT:
            return Score

        # Score display
        Score_text = font.render(f"Score: {Score}", True, WHITE)
        screen.blit(Score_text, (10, 10))

        

        # Update screen
        pygame.display.flip()
        clock.tick(20)
    return None


# Create pipes function
def create_pipe():
    pipe_height = random.randint(100, HEIGHT - pipe_gap - 100)
    top_pipe = pygame.Rect(WIDTH, 0, pipe_width, pipe_height)
    bottom_pipe = pygame.Rect(WIDTH, pipe_height + pipe_gap, pipe_width, HEIGHT - pipe_height - pipe_gap)
    return top_pipe, bottom_pipe

# PROGRAM LOOP – GAME + RESTART
while True:
    score = run_game()
    game_over_screen(score)
