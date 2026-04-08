import random

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
  print("Let's play rock, paper, or scissors")
  player_choice = input("rock, paper, scissors : ").lower()
  choices = ["rock", "paper", "scissors"]
  while player_choice not in choices: # Tambahkan validasi di sini
    player_choice = input("invalid choice. choose rock, paper, or scissors: ").lower()
  computer_choice = random.choice(choices)
  print("Computer chose: " + computer_choice)
  if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
    winner = "Player"
  elif (player_choice == computer_choice):
    winner = "Tie"
  else:
      winner = "Computer"
  if winner == "Player":
    print("You won")
  elif winner == "Computer":
    print("Computer won")
  else:
    print("It's a tie")
  if winner == "Player":
    player_wins += 1
  elif winner == "Computer":
    computer_wins += 1
  print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")
if player_wins > computer_wins:
  print("Congratulations! You won.")
else:
  print("Computer won!")

while True:
  play_again = input("Do you want to play again? (yes/no): ").lower()
  if play_again != 'yes':
    print("Thanks for playing!")
    break
