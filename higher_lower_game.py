import random

def print_intro():
    print("\nWelcome to the Higher or Lower Game!")
    print("=====================================")
    print("Two players take turns guessing whether the next number will be higher or lower.")
    print("First to 5 points wins!\n")

def get_guess(player_name):
    while True:
        guess = input(f"{player_name}, do you think the next number will be Higher (H) or Lower (L)? ").strip().upper()
        if guess in ['H', 'L']:
            return guess
        else:
            print("Invalid input. Please enter H or L.")

def play_turn(player_name, current_number):
    print(f"\nCurrent number is: {current_number}")
    guess = get_guess(player_name)
    next_number = random.randint(1, 100)
    print(f"The next number is: {next_number}")

    if guess == 'H' and next_number > current_number:
        print("\u2705 Correct! It's higher.")
        return 1
    elif guess == 'L' and next_number < current_number:
        print("\u2705 Correct! It's lower.")
        return 1
    elif next_number == current_number:
        print("\u2696\ufe0f It's the same! No points.")
        return 0
    else:
        print("\u274C Incorrect.")
        return 0

def main():
    print_intro()

    player1 = input("Enter Player 1 name: ").strip() or "Player 1"
    player2 = input("Enter Player 2 name: ").strip() or "Player 2"

    scores = {player1: 0, player2: 0}
    current_number = random.randint(1, 100)

    while max(scores.values()) < 5:
        for player in [player1, player2]:
            print(f"\n--- {player}'s Turn ---")
            points = play_turn(player, current_number)
            scores[player] += points
            current_number = random.randint(1, 100)

            print(f"Scoreboard: {player1}: {scores[player1]} | {player2}: {scores[player2]}")

            if scores[player] >= 5:
                break

    winner = player1 if scores[player1] >= 5 else player2
    print(f"\n\U0001F389 {winner} wins the game with {scores[winner]} points! Congratulations!")

if __name__ == "__main__":
    main()
