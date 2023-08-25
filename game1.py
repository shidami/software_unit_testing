import random


# Function to generate a random number
def generate_number():
    return str(random.randint(1000, 9999))


# Function to verify a random number
def validate_input(guess):
    return len(guess) == 4 and guess.isdigit()


# Function to get hints of game rule
def give_hints(number, guess):
    hints = []
    for i in range(4):
        if guess[i] == number[i]:
            hints.append("o")
        elif guess[i] in number:
            hints.append("x")
    return "".join(hints)


class GuessGame:

    def __init__(self):
        # save a random number to self number variant
        self.number = generate_number()
        # save the number of attempt to attempt variant
        self.attempts = 0

    def guess(self, guess_num):
        self.attempts += 1
        return give_hints(self.number, guess_num)

    def play(self):
        while True:
            user_guess = input("Enter your guess (or 'quit' to exit): ")
            if user_guess == 'quit':
                print("Thanks for playing!")
                break
            if not validate_input(user_guess):
                print("Invalid input. Please enter a 4-digit number.")
                continue

            hints = self.guess(user_guess)
            print(f"Hints: {hints}")
            if hints == "oooo":
                print(
                    f"Congratulations! \
                        You guessed it in {self.attempts} attempts!"
                    )
                play_again = input("Do you want to play again? (yes/no): ")
                if play_again.lower() == 'yes':
                    self.number = generate_number()
                    self.attempts = 0
                else:
                    print("Thanks for playing!")
                    break


if __name__ == "__main__":
    game = GuessGame()
    game.play()
