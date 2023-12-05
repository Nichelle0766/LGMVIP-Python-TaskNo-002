import random

# Function to initialize the game
def initialize_game():
    global snake, direction, food, score
    snake = [(5, 5)]
    direction = (1, 0)  # Initial direction: right
    food = generate_food()
    score = 0

# Function to generate random food position
def generate_food():
    return (random.randint(0, 9), random.randint(0, 9))

# Function to display the current state of the game
def display_game():
    for row in range(10):
        for col in range(10):
            if (row, col) in snake:
                print("S", end=" ")
            elif (row, col) == food:
                print("F", end=" ")
            else:
                print(".", end=" ")
        print()

# Function to update the game state
def update_game():
    global snake, direction, food, score

    # Update snake position based on the current direction
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Check if the snake eats the food
    if head == food:
        snake.append(food)
        food = generate_food()
        score += 1
    else:
        # Move the snake
        snake = [head] + snake[:-1]

# Main game loop
initialize_game()

while True:
    display_game()
    print("Score:", score)

    # Get user input for direction change
    user_input = input("Enter direction (W/A/S/D): ").upper()

    if user_input == "W":
        direction = (-1, 0)
    elif user_input == "A":
        direction = (0, -1)
    elif user_input == "S":
        direction = (1, 0)
    elif user_input == "D":
        direction = (0, 1)

    # Update the game state
    update_game()

    # Check for game over condition
    if (
        snake[0] in snake[1:]
        or snake[0][0] < 0
        or snake[0][0] >= 10
        or snake[0][1] < 0
        or snake[0][1] >= 10
    ):
        print("Game Over! Your score:", score)
        break
