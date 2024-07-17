import random
import string

def generate_password(length):
  """
  Generates a random password with the specified length containing letters, numbers, and symbols.
  """
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for _ in range(length))
  return password

def main():
  """
  Prompts the user for desired password length, generates a random password, and prints it.
  """
  try:
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print("Generated password:", password)
  except ValueError:
    print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
  main()
