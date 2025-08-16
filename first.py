import random

class GuessGame:
    def __init__(self, lower=1, upper=100):
        self.lower = lower
        self.upper = upper
        self.number_to_guess = random.randint(self.lower, self.upper)
        self.attempts = 0

    def start(self):
        print(f"Welcome to Guess the Number!")
        print(f"I'm thinking of a number between {self.lower} and {self.upper}.")
        
        while True:
            try:
                guess = int(input("Take a guess: "))
                self.attempts += 1
                if guess < self.number_to_guess:
                    print("Too low! Try again.")
                elif guess > self.number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed it in {self.attempts} attempts.")
                    break
            except ValueError:
                print("Please enter a valid integer.")

# Create a game instance and start the game
if __name__ == "__main__":
    game = GuessGame()
    game.start()
