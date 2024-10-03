import random

def relationship_guessing_game():
    # List of possible relationships
    relationships = [
        "Love", "Marriage", "Friends", "Soulmates", 
        "Enemies", "Best Friends", "Crush", "Acquaintances", 
        "Complicated", "Rivals", "Partners", "Secret Admirer"
    ]
    
    print("Welcome to the Relationship Guessing Game!")
    print("========================================")
    
    # Get inputs from users
    name1 = input("Enter the first person's name: ").strip().capitalize()
    name2 = input("Enter the second person's name: ").strip().capitalize()

    # Randomly select a relationship from the list
    guessed_relationship = random.choice(relationships)
    
    # Display the relationship guess result
    print("\n=====================")
    print(f"Relationship result for {name1} and {name2}:")
    print(f"\u2665 {guessed_relationship} \u2665")
    print("=====================")
    
    # Ask if the user wants to play again
    play_again = input("\nWould you like to try again? (yes/no): ").strip().lower()
    if play_again == "yes":
        relationship_guessing_game()
    else:
        print("Thanks for playing! Have a great day!")

# Start the game
if __name__ == "__main__":
    relationship_guessing_game()
