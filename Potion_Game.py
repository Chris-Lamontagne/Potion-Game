import random


def main():
    # Define the available ingredients.
    ingredients = [
        "Eye of Newt",
        "Dragon Scale",
        "Phoenix Feather",
        "Unicorn Horn",
        "Mermaid Tears",
        "Troll Toenail"
    ]

    # Randomly select 4 unique ingredients for the secret potion.
    secret_potion = random.sample(ingredients, 4)

    print("Welcome to the Magical Potion Game!")
    print("Your goal is to guess the correct sequence of 4 ingredients to create the magical potion.\n")
    print("Available ingredients:")
    for idx, ingredient in enumerate(ingredients, start=1):
        print(f"{idx}. {ingredient}")
    print("\nAfter each guess, you'll get hints:")
    print(" - How many ingredients are in the correct position.")
    print(" - How many ingredients are correct but in the wrong position.\n")

    attempts = 0

    while True:
        # Prompt the player to enter their guess as four numbers.
        guess_input = input("Enter your guess as four numbers separated by spaces (e.g. 1 3 5 6): ")
        guess_numbers = guess_input.split()

        if len(guess_numbers) != 4:
            print("Please enter exactly four numbers.\n")
            continue

        try:
            # Convert the numbers into list indices (0-based).
            guess_indices = [int(num) - 1 for num in guess_numbers]
            if any(index < 0 or index >= len(ingredients) for index in guess_indices):
                print(
                    "One or more numbers are out of range. Please choose numbers corresponding to the available ingredients.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers only.\n")
            continue

        # Create the guessed potion based on the indices.
        guess = [ingredients[i] for i in guess_indices]
        attempts += 1

        # Calculate the number of ingredients in the correct position.
        correct_position = sum(1 for i in range(4) if guess[i] == secret_potion[i])

        # Calculate the total number of matching ingredients (regardless of position)
        common = 0
        for ing in set(guess):
            common += min(guess.count(ing), secret_potion.count(ing))
        wrong_position = common - correct_position

        print(
            f"\nAttempt {attempts}: {correct_position} in the correct position, {wrong_position} correct but in the wrong position.\n")

        # Check if the guess matches the secret potion.
        if guess == secret_potion:
            print(f"Congratulations! You've created the magical potion in {attempts} attempts!")
            break


if __name__ == "__main__":
    main()
