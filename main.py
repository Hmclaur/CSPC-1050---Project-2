"""
Author:         Hugh McLaurin
Date:           Saturday, April 27
Assignment:     Project 2
Course:         CPSC1050
Lab Section:    001
GitHub Link: https://github.com/Hmclaur/CSPC-1050---Project-2
CODE DESCRIPTION:  In this project, I have created a game where you have to secape from a cave by selecting different tunnels and fighting monsters.  You can also recieve rewards and puchase upgrades from a shop.  

"""



import random
import json

# Player class representing the player's attributes
class Player:
    def __init__(self):
        self.hp = 20
        self.gold = 0
        self.damage = 1

    
# Function to roll a dice with given number of sides
def roll_dice(sides):
    return random.randint(1, sides)

# Function to save the game state to a file
def save_game_state(player, room_count):
    # Create a dictionary with player's attributes and room count
    save_data = {
        "hp": player.hp,
        "gold": player.gold,
        "damage": player.damage,
        "room_count": room_count
    }
    # Write the save data to a file
    with open("save_game.txt", "w") as file:
        json.dump(save_data, file)

# Function to get a valid choice from the player
def get_valid_choice():
    # Loop until a valid choice is entered
    while True:
        # Prompt the user to choose a tunnel or exit
        choice = input("Choose a tunnel (1 or 2) or type 'exit':")

        # Check if the choice is valid
        if choice in ['1', '2', 'exit', 'back']:
            return choice  # Return the valid choice
            
        else:
            # If the choice is not valid, print an error message
            print("Invalid choice. Please enter 1, 2, or 'exit'.")

# Function to load the game state from a file
def load_game_state():
    # Try to load game state from file
    try:
        # Open the save_game.txt file in read mode
        with open("save_game.txt", "r") as file:
            # Load the save data from the file using JSON
            save_data = json.load(file)
            # Create a new Player object
            player = Player()
            # Set player's attributes based on saved data
            player.hp = save_data["hp"]
            player.gold = save_data["gold"]
            player.damage = save_data["damage"]
            room_count = save_data["room_count"]
        # Return the loaded player and room count
        return player, room_count

    # If the save_game.txt file is not found
    except FileNotFoundError:
        # Print a message indicating that no save game was found
        print("No save game found.")
        # Return None values for player and room count
        return None, None


# Function to process the contents of a treasure chest
def process_treasure_chest(player):
    # Randomly determine the contents of the treasure chest
    treasure_contents = random.choice(["gold", "damage up", "health potion"])

    # If the treasure contains gold
    if treasure_contents == "gold":
        # Roll a dice to determine the amount of gold found
        gold_found = roll_dice(3) * 10
        # Add the found gold to the player's gold
        player.gold += gold_found
        # Display a message informing the player about the gold found
        print("You found", gold_found, "gold!")

    # If the treasure contains a damage boost
    elif treasure_contents == "damage up":
        # Increase the player's damage by 1
        player.damage += 1
        # Display a message informing the player about the damage boost
        print("You found a damage boost! Your damage is now", player.damage)

    # If the treasure contains a health potion
    elif treasure_contents == "health potion":
        # Increase the player's health by 10
        player.hp += 10
        # Display a message informing the player about the health potion
        print("You found a health potion! Your health is now", player.hp)

# Function representing a battle between player and monster
def battle(player, monster_hp):
    # Display the start of the battle
    print("Battle starts!")

    # Loop until either the player or the monster runs out of hit points
    while player.hp > 0 and monster_hp > 0:
        # Player attacks the monster
        player_attack = roll_dice(player.damage)
        monster_attack = roll_dice(monster_hp)
        print("You attack the monster for", player_attack, "damage.")
        monster_hp -= player_attack

        # Check if the monster has been defeated
        if monster_hp <= 0:
            print("You defeated the monster!")
            return True  # Return True to indicate the player won the battle

        # Monster attacks the player
        print("The monster attacks you for", monster_attack, "damage.")
        player.hp -= monster_attack

        # Check if the player has been defeated
        if player.hp <= 0:
            player.hp = 0  # Ensure player's health doesn't go below 0
            print("Your health is now", player.hp)  # Inform the player of their health

    # If the loop ends, the player has been defeated
    print("You were defeated by the monster!")
    return False  # Return False to indicate the player lost the battle


# Function to interact with the merchant
def visit_merchant(player):
    # Welcome message from the merchant
    print("Merchant: Welcome, traveler! What would you like to buy?\nIf you don't have any money, then you can get out of here!")

    # Loop until the player makes a valid choice or exits
    while True:
        # Display options for the player
        print("1. Damage boost (5 gold)")
        print("2. Health potion (10 gold)")
        print("Type 'exit' to leave without buying anything")
        choice = input("Enter your choice: ")

        # If the player chooses to buy a damage boost
        if choice == '1':
            # Check if the player has enough gold
            if player.gold >= 5:
                # Apply the damage boost and deduct gold
                player.damage += 1
                player.gold -= 5
                print("You bought a damage boost! Your damage is now", player.damage)
                break
            else:
                # Inform the player that they don't have enough gold
                print("You don't have enough gold to buy a damage boost.")

        # If the player chooses to buy a health potion
        elif choice == '2':
            # Check if the player has enough gold
            if player.gold >= 10:
                # Apply the health potion and deduct gold
                player.hp += 10
                player.gold -= 10
                print("You bought a health potion! Your health is now", player.hp)
                break
            else:
                # Inform the player that they don't have enough gold
                print("You don't have enough gold to buy a health potion.")

        # If the player chooses to exit without buying anything
        elif choice.lower() == 'exit':
            print("Merchant: 'Good Riddance'")  # Farewell message from the merchant
            break

        # If the player enters an invalid choice
        else:
            print("Invalid choice. Please enter '1', '2', or 'exit'.")


# Main function controlling the flow of the game
def main():
    # Loop until a valid choice is made
    while True:
        # Ask the player if they want to load a saved game
        choice = input("Do you want to load a saved game? (yes/no): ")

        # If the player chooses to load a saved game
        if choice.lower() == "yes":
            # Load the game state
            player, room_count = load_game_state()
            # If no saved game is found, start a new game
            if player is None:
                player = Player()
                room_count = 1
            break

        # If the player chooses not to load a saved game, start a new game
        elif choice.lower() == "no":
            player = Player()
            room_count = 1
            break

        # If an invalid choice is entered, prompt the player to enter 'yes' or 'no'
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    # Print welcome message and player's initial hit points
    print("Welcome to the RPG game!")
    print(f"You wake up in a cave with {player.hp} hit points.")

    # Main game loop
    while room_count <= 10 and player.hp > 0:
        print("\nRoom", room_count)
        print("You have", player.hp, "hit points and", player.gold, "gold.")

        # Get player's choice for the current room
        choice = get_valid_choice()

        # If the player chooses to exit the game
        if choice == 'exit':
            print("Exiting the game.")

            # Prompt the player to save the game before exiting
            while True:
                choice = input("Do you want to save the game? (yes/no): ").lower()

                # If the player chooses to save the game
                if choice == "yes":
                    save_game_state(player, room_count)
                    exit(1)

                # If the player chooses not to save the game, exit without saving
                elif choice == "no":
                    exit(1)

                # If an invalid choice is entered, prompt the player to enter 'yes' or 'no'
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")

        # Roll a dice to determine the event in the room
        tunnel = roll_dice(3)

        # If the event is finding a treasure chest
        if tunnel == 1:
            print("You found a treasure chest!")

            # Process the treasure chest based on the player's choice
            if choice == '1':
                process_treasure_chest(player)

            elif choice == '2':
                process_treasure_chest(player)

        # If the event is encountering a monster
        elif tunnel == 2:
            print("You encountered a monster!")

            # Initiate a battle with the monster based on the player's choice
            if choice == '1':
                monster_hp = roll_dice(6)

                if battle(player, monster_hp):
                    player.gold += roll_dice(6) * 2

            elif choice == '2':
                monster_hp = roll_dice(6)

                if battle(player, monster_hp):
                    player.gold += roll_dice(6) * 2

        # If the event is meeting a merchant
        elif tunnel == 3:
            print("You met a merchant!")

            # Visit the merchant and make purchases based on the player's choice
            if choice == '1':
                visit_merchant(player)

            elif choice == '2':
                visit_merchant(player)

        # Move to the next room
        room_count += 1

    # Check win/lose conditions after exiting the main game loop
    if room_count > 10:
        print("Congratulations! You win!")

    elif player.hp <= 0:
        print("Game over! You lose.")

# Entry point of the program
if __name__ == "__main__":
    main()

