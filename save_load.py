def save_game(player, room_count):
    # Open the save_game.txt file in write mode
    with open("save_game.txt", "w") as file:
        # Write player's attributes and room count to the file
        file.write(f"{player.hp}\n")  # Write player's health points
        file.write(f"{player.gold}\n")  # Write player's gold
        file.write(f"{player.damage}\n")  # Write player's damage points
        file.write(f"{room_count}\n")  # Write room count

def load_game():
    try:
        # Try to open the save_game.txt file in read mode
        with open("save_game.txt", "r") as file:
            # Read player's attributes and room count from the file
            hp = int(file.readline().strip())  # Read player's health points
            gold = int(file.readline().strip())  # Read player's gold
            damage = int(file.readline().strip())  # Read player's damage points
            room_count = int(file.readline().strip())  # Read room count
            
            # Create a new Player object
            player = Player()
            # Set player's attributes based on saved data
            player.hp = hp
            player.gold = gold
            player.damage = damage

            # Return the loaded player and room count
            return player, room_count
    # If the save_game.txt file is not found
    except FileNotFoundError:
        # Print a message indicating that no save game was found
        print("No save game found.")
        # Return None values for player and room count
        return None, None



