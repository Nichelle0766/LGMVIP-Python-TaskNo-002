# LGMVIP-Python-TaskNo-002
The Snake game is a classic and simple video game that originated in the late 1970s and gained popularity on early mobile phones and personal computers. Here's an overview of the basic concepts and rules of the Snake game:
Objective:
The primary objective of the Snake game is to control a snake on a game board, guiding it to eat food items, and as a result, growing longer. The challenge lies in avoiding collisions with the walls of the game board and, more critically, with the snake's own body.

Here is an Outline of the code
1. Setting Up the Game:
   
  # Initialize game variables
snake = [(5, 5)]     # Snake starts at position (5, 5)
direction = (1, 0)   # Initial direction: right
food = (0, 0)        # Placeholder for food position
score = 0            # Player's score

  # Function to generate random food position
def generate_food():
    return (random.randint(0, 9), random.randint(0, 9))

  # Function to initialize the game
def initialize_game():
    global snake, direction, food, score
    snake = [(5, 5)]
    direction = (1, 0)
    food = generate_food()
    score = 0

2. Displaying the Game:

  # Function to display the current state of the game
def display_game():
    for row in range(10):
        for col in range(10):
            if (row, col) in snake:
                print("S", end=" ")    # Snake segment
            elif (row, col) == food:
                print("F", end=" ")    # Food
            else:
                print(".", end=" ")    # Empty space
        print()

3. Updating the Game:

# Function to update the game state
def update_game():
    global snake, direction, food, score

    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if head == food:
        snake.append(food)
        food = generate_food()
        score += 1
    else:
        snake = [head] + snake[:-1]

4. Main Loop
5. # Initialize the game
initialize_game()

while True:
    # Display current state
    display_game()
    print("Score:", score)

    # Get user input for direction change
    user_input = input("Enter direction (W/A/S/D): ").upper()

    # Update direction based on user input
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

    # Check for game over conditions
    if (
        snake[0] in snake[1:]
        or snake[0][0] < 0
        or snake[0][0] >= 10
        or snake[0][1] < 0
        or snake[0][1] >= 10
    ):
        print("Game Over! Your score:", score)
        break

*** The game starts with a snake at the center moving to the right.
*** The goal is to eat the food ('F') and grow the snake while avoiding collisions.
*** In each turn, the player inputs a direction (W, A, S, D) to move the snake.
*** The game updates the state, checks for collisions, and continues until the game is over.
