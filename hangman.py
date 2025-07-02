import random
import os

class HangmanGame:
    def __init__(self):
        self.word_bank = {
            "Animals": ["elephant", "giraffe", "kangaroo", "penguin", "rhinoceros",
                        "cheetah", "octopus", "butterfly", "chameleon", "dolphin"],
            "Countries": ["canada", "brazil", "japan", "australia", "germany",
                          "egypt", "italy", "thailand", "argentina", "norway"],
            "Fruits": ["watermelon", "strawberry", "pineapple", "blueberry", "raspberry",
                       "blackberry", "pomegranate", "mango", "kiwi", "dragonfruit","apple","banana","durian","pear"],
            "Sports": ["basketball", "volleyball", "badminton", "swimming", "gymnastics",
                       "wrestling", "cycling", "archery", "fencing", "boxing"]
        }
        self.max_attempts = 6  # Standard hangman with 6 body parts

        # Hangman ASCII art stages (6 stages + empty)
        self.hangman_art = [
            """
            -----
            |   |
                |
                |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
                |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
            |   |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
           /|   |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
           /|\\  |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
           /|\\  |
           /    |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
           /|\\  |
           / \\  |
                |
            --------
            """
        ]

    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def select_category(self):
        """Let the player select a word category."""
        self.clear_screen()
        print("Select a category:")
        categories = list(self.word_bank.keys())
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

        while True:
            try:
                choice = int(input("Enter your choice (1-{}): ".format(len(categories))))
                if 1 <= choice <= len(categories):
                    return categories[choice - 1]
                print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")

    def get_random_word(self, category):
        """Get a random word from the selected category."""
        return random.choice(self.word_bank[category])

    def display_game(self, word_progress, used_letters, attempts_left, category):
        """Display the current game state."""
        self.clear_screen()
        print("\n=== Hangman Game ===")
        print(f"Category: {category}")

        # Display hearts for attempts left
        hearts = "💗 " * attempts_left
        print(f"Lives left: {hearts}\n")

        # Display hangman art based on attempts used
        stage = self.max_attempts - attempts_left
        print(self.hangman_art[stage])

        print("\nWord: " + " ".join(word_progress))
        print("\nUsed letters: " + " ".join(sorted(used_letters)) + "\n")

    def play_game(self):
        """Main game loop."""
        category = self.select_category()
        secret_word = self.get_random_word(category)
        word_progress = ["_"] * len(secret_word)
        used_letters = set()
        attempts_left = self.max_attempts
        game_won = False

        while attempts_left > 0 and not game_won:
            self.display_game(word_progress, used_letters, attempts_left, category)

            # Check for win condition
            if "_" not in word_progress:
                game_won = True
                break

            print("Enter a letter or 'quit' to exit:")
            user_input = input("> ").lower()

            if user_input == "quit":
                print(f"\nGame ended. The word was: {secret_word}")
                return
            elif len(user_input) != 1 or not user_input.isalpha():
                print("\nPlease enter a single letter.")
                input("Press Enter to continue...")
                continue
            elif user_input in used_letters:
                print("\nYou've already tried that letter.")
                input("Press Enter to continue...")
                continue

            used_letters.add(user_input)

            if user_input in secret_word:
                for i, letter in enumerate(secret_word):
                    if letter == user_input:
                        word_progress[i] = letter
                print("\nCorrect guess!")
            else:
                attempts_left -= 1
                print("\nWrong guess! You lost a life 💔")

            input("Press Enter to continue...")

        self.display_game(word_progress, used_letters, attempts_left, category)
        if game_won:
            print("\nCongratulations! You won!")
            input("\nPress Enter to return to the main menu...")

    def main_menu(self):
        """Display the main menu and handle user choices."""
        while True:
            self.clear_screen()
            print("\n=== Hangman Game ===")
            print("1. Play Game")
            print("2. Exit")

            choice = input("\nEnter your choice (1-4): ")

            if choice == "1":
                self.play_game()
            elif choice == "2":
                print("\nThanks for playing! Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")
                input("Press Enter to continue...")


if __name__ == "__main__":
    game = HangmanGame()
    game.main_menu()
