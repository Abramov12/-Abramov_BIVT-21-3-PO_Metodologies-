from Brain_games.engine import run_game
from Brain_games.games import noc, geometric


def main():
    print("Choose a game:")
    print("NOC")
    print("Geometric")

    user_choice = input("Your choice: ")

    if user_choice == "NOC":
        run_game(noc)
    elif user_choice == "Geometric":
        run_game(geometric)
    else:
        print("Oops! Invalid choice. Please try again")

if __name__ == "__main__":
    main()