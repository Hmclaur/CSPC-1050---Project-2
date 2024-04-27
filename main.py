import random
import json

# Player class representing the player's attributes
class Player:
    def __init__(self):
        self.hp = 20
        self.gold = 0
        self.damage = 1

# Room class representing different rooms in the game
class Room:
    def __init__(self, name, description, room_type, exits):
        self.name = name
        self.description = description
        self.room_type = room_type
        self.exits = exits

    def __str__(self):
        return f"{self.name}: {self.description}\nType: {self.room_type}\n\nExits:\n{', '.join(self.exits)}"

# Function to roll a dice with given number of sides
def roll_dice(sides):
    return random.randint(1, sides)

# Function to save the game state to a file
def save_game_state(player, room_count):
    save_data = {
        "hp": player.hp,
        "gold": player.gold,
        "damage": player.damage,
        "room_count": room_count
    }
    with open("save_game.txt", "w") as file:
        json.dump(save_data, file)

# Function to get a valid choice from the player
def get_valid_choice():
    while True:
        choice = input("Choose a tunnel (1 or 2) or type 'exit':")

        if choice in ['1', '2', 'exit', 'back']:
            return choice
            
        else:
            print("Invalid choice. Please enter 1, 2, or 'exit'.")

# Function to load the game state from a file
def load_game_state():

    try:
        with open("save_game.txt", "r") as file:
            save_data = json.load(file)
            player = Player()
            player.hp = save_data["hp"]
            player.gold = save_data["gold"]
            player.damage = save_data["damage"]
            room_count = save_data["room_count"]
        return player, room_count

    except FileNotFoundError:
        print("No save game found.")
        return None, None

# Function to process the contents of a treasure chest
def process_treasure_chest(player):
    treasure_contents = random.choice(["gold", "damage up", "health potion"])

    if treasure_contents == "gold":
        gold_found = roll_dice(3) * 10
        player.gold += gold_found
        print("You found", gold_found, "gold!")

    elif treasure_contents == "damage up":
        player.damage += 1
        print("You found a damage boost! Your damage is now", player.damage)

    elif treasure_contents == "health potion":
        player.hp += 10
        print("You found a health potion! Your health is now", player.hp)

# Function representing a battle between player and monster
def battle(player, monster_hp):
    print("Battle starts!")
    while player.hp > 0 and monster_hp > 0:
        player_attack = roll_dice(player.damage)
        monster_attack = roll_dice(monster_hp)
        print("You attack the monster for", player_attack, "damage.")
        monster_hp -= player_attack

        if monster_hp <= 0:
            print("You defeated the monster!")
            return True

        print("The monster attacks you for", monster_attack, "damage.")
        player.hp -= monster_attack

        if player.hp <= 0:
            player.hp = 0

        print("Your health is now", player.hp)

    print("You were defeated by the monster!")
    return False

# Function to interact with the merchant
def visit_merchant(player):
    print("Merchant: Welcome, traveler! What would you like to buy?\nIf you don't have any money, then you can get out of here!")

    while True:
        print("1. Damage boost (5 gold)")
        print("2. Health potion (10 gold)")
        print("Type 'exit' to leave without buying anything")
        choice = input("Enter your choice: ")

        if choice == '1':
            if player.gold >= 5:
                player.damage += 1
                player.gold -= 5
                print("You bought a damage boost! Your damage is now", player.damage)
                break

            else:
                print("You don't have enough gold to buy a damage boost.")

        elif choice == '2':

            if player.gold >= 10:
                player.hp += 10
                player.gold -= 10
                print("You bought a health potion! Your health is now", player.hp)
                break

            else:
                print("You don't have enough gold to buy a health potion.")
        elif choice.lower() == 'exit':
            print("Merchant: 'Good Riddance'")
            break

        else:
            print("Invalid choice. Please enter '1', '2', or 'exit'.")

# Main function controlling the flow of the game
def main():
    while True:
        choice = input("Do you want to load a saved game? (yes/no): ")

        if choice.lower() == "yes":
            player, room_count = load_game_state()
            if player is None:
                player = Player()
                room_count = 1
            break

        elif choice.lower() == "no":
            player = Player()
            room_count = 1
            break

        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    print("Welcome to the RPG game!")
    print(f"You wake up in a cave with {player.hp} hit points.")

    while room_count <= 10 and player.hp > 0:
        print("\nRoom", room_count)
        print("You have", player.hp, "hit points and", player.gold, "gold.")

        choice = get_valid_choice()

        if choice == 'exit':
            print("Exiting the game.")

            while True:
                choice = input("Do you want to save the game? (yes/no): ").lower()

                if choice == "yes":
                    save_game_state(player, room_count)
                    exit(1)

                elif choice == "no":
                    exit(1)

                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")

        tunnel = roll_dice(3)

        if tunnel == 1:
            print("You found a treasure chest!")

            if choice == '1':
                process_treasure_chest(player)

            elif choice == '2':
                process_treasure_chest(player)

        elif tunnel == 2:
            print("You encountered a monster!")

            if choice == '1':
                monster_hp = roll_dice(6)

                if battle(player, monster_hp):
                    player.gold += roll_dice(6) * 2

            elif choice == '2':
                monster_hp = roll_dice(6)

                if battle(player, monster_hp):
                    player.gold += roll_dice(6) * 2

        elif tunnel == 3:
            print("You met a merchant!")

            if choice == '1':
                visit_merchant(player)

            elif choice == '2':
                visit_merchant(player)

        room_count += 1

    if room_count > 10:
        print("Congratulations! You win!")

    elif player.hp <= 0:
        print("Game over! You lose.")

# Entry point of the program
if __name__ == "__main__":
    main()
