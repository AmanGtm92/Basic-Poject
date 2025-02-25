import random

print("\n🎮 Welcome to Rock, Paper, Scissors Game! ✊✋✌️")

choices = ["rock", "paper", "scissors"]

while True:
    print("\nChoose: Rock ✊, Paper ✋, or Scissors ✌️")
    user_choice = input("Enter your choice: ")
    
    if user_choice not in choices:
        print("❌ Invalid choice! Please choose Rock, Paper, or Scissors.")
        continue
    computer_choice = input("Enter second player choice :- ")
   # computer_choice = random.choice(choices)
    print("\n🤖 Computer chose: ",computer_choice)

    if user_choice == computer_choice:
        print("😑 It's a Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("🎉 You Win!")
    else:
        print("💀 You Lose!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing! 🚀")
        break