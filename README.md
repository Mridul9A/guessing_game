# Guessing Game

A simple web-based guessing game built with Flask. The player tries to guess a random number between 1 and 100.

## Features

- Random number generation between 1 and 100
- Tracks the number of guesses
- Provides feedback if the guess is too high or too low
- Displays the total number of attempts upon guessing correctly

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/guessing_game.git
    cd guessing_game
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install Flask
    ```

## Running the Application

1. Set the Flask app environment variable:
    ```sh
    export FLASK_APP=app.py    # On Windows use `set FLASK_APP=app.py`
    ```

2. Run the Flask app:
    ```sh
    flask run
    ```

3. Open your web browser and go to `http://127.0.0.1:5000/` to play the game.

## Directory Structure

guessing_game/
├── app.py
├── templates/
│ ├── index.html
│ ├── guess.html
│ └── result.html
└── static/
└── style.css


- `app.py`: The main Flask application.
- `templates/`: HTML templates for the game.
- `static/style.css`: CSS for styling the game.

## Usage

1. When you open the game, you will be greeted with a welcome message and a form to enter your guess.
2. Submit your guess, and the application will tell you if the number is higher or lower.
3. Continue guessing until you find the correct number.
4. Once you guess correctly, the total number of attempts will be displayed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
