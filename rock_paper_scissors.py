import random

def get_user_choice():
    print("Choose one: rock, paper, scissors")
    choice = input("Your choice: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Try again.")
        choice = input("Your choice: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    user = get_user_choice()
    computer = get_computer_choice()
    print(f"Computer chose: {computer}")
    result = determine_winner(user, computer)
    print(result)

if __name__ == "__main__":
    play()
