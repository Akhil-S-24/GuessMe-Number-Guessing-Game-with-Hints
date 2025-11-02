import random
import time

def guess_me():
    print("\n🎯 Welcome to GuessMe – The Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible!\n")

    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1–100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠️ Please guess a number between 1 and 100.")
                continue

            # Check the guess
            if guess == secret_number:
                print(f"🎉 Correct! You guessed the number in {attempts} attempts!")
                break
            elif abs(secret_number - guess) <= 3:
                print("🔥 Very close! You're almost there!")
            elif guess < secret_number:
                print("📉 Too low! Try a higher number.")
            else:
                print("📈 Too high! Try a lower number.")

        except ValueError:
            print("⚠️ Please enter a valid number.")

    # Ask to play again
    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again == "yes":
        print("\nRestarting the game...")
        time.sleep(1)
        guess_me()
    else:
        print("\nThanks for playing GuessMe! 👋 Goodbye!")

# Run the game
if __name__ == "__main__":
    guess_me()
