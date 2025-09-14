This Python project is a two-player Pong game built with the turtle library, adapted for a mobile-friendly experience using a touch-based control scheme.
​Key Features and Functionality
​This is a classic arcade-style Pong game with a twist—the controls are designed for touchscreens, not a keyboard.
​Touch-Based Controls: The paddles are not controlled by a keyboard. Instead, a tap on the top half of the screen moves a paddle up, and a tap on the bottom half moves it down. Tapping the right side of the screen controls the right paddle, while tapping the left side controls the left paddle. This makes it suitable for mobile play.
​Two-Player Gameplay: The game supports two players, each controlling a paddle on either side of the screen.
​Dynamic Difficulty: As the game progresses and the ball hits the paddles, its speed increases, making the game more challenging over time.
​Scoring and Timer: The game includes a scoreboard that tracks each player's points. A countdown timer limits the match to 60 seconds.
​Win/Loss Condition: The game ends when the timer runs out. A final message announces the winner based on the score, or a draw if both players have the same score.
​Collision Detection: The ball bounces off the top and bottom walls, as well as the paddles. If a player misses the ball, the other player scores a point, and the ball resets to the center.
​How it's Structured
​The code is organized into three main classes:
​Paddle: This class creates and manages the paddles, handling their size, position, and movement.
​Ball: This class creates the ball and manages its movement and speed.
​Scoreboard: This class handles the display of scores and the game timer, and it prints the final result at the end of the match.
​The main game loop continuously updates the ball's position, checks for collisions with the walls and paddles, and manages the game's state based on the timer.
