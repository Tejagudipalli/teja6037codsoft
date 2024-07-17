import random

def play_again():
  """
  Asks the user if they want to play another round.

  Returns:
      bool: True if the user wants to play again, False otherwise.
  """
  while True:
    choice = input("Play again? (y/n): ").lower()
    if choice == 'y':
      return True
    elif choice == 'n':
      return False
    else:
      print("Invalid input. Please enter 'y' or 'n'.")

def determine_winner(user_choice, computer_choice):
  """
  Determines the winner of a rock-paper-scissors round.

  Args:
      user_choice: The user's choice (rock, paper, or scissors).
      computer_choice: The computer's choice (rock, paper, or scissors).

  Returns:
      str: "You win!", "You lose!", or "It's a tie!"
  """
  choices = ["rock", "paper", "scissors"]
  winning_combos = {
    "rock": ["scissors"],
    "paper": ["rock"],
    "scissors": ["paper"]
  }

  if user_choice == computer_choice:
    return "It's a tie!"
  elif computer_choice in winning_combos[user_choice]:
    return "You win!"
  else:
    return "You lose!"

def main():
  """
  The main function that runs the rock-paper-scissors game.
  """
  user_score = 0
  computer_score = 0

  while True:
    print("\nRock Paper Scissors!")

    # Get user input
    while True:
      user_choice = input("Choose rock, paper, or scissors: ").lower()
      if user_choice in ["rock", "paper", "scissors"]:
        break
      else:
        print("Invalid choice. Please enter rock, paper, or scissors.")

    # Generate computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Determine winner and display results
    result = determine_winner(user_choice, computer_choice)
    print(f"You chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    print(result)

    # Update scores (optional)
    if result == "You win!":
      user_score += 1
    elif result == "You lose!":
      computer_score += 1
    print(f"Current score: You - {user_score}, Computer - {computer_score}")

    # Ask to play again
    if not play_again():
      break

if __name__ == "__main__":
  main()


