def save_game(player, room_count):
    with open("save_game.txt", "w") as file:
        file.write(f"{player.hp}\n")
        file.write(f"{player.gold}\n")
        file.write(f"{player.damage}\n")
        file.write(f"{room_count}\n")

def load_game():
    try:
        with open("save_game.txt", "r") as file:
            hp = int(file.readline().strip())
            gold = int(file.readline().strip())
            damage = int(file.readline().strip())
            room_count = int(file.readline().strip())
            
            player = Player()
            player.hp = hp
            player.gold = gold
            player.damage = damage

            return player, room_count
    except FileNotFoundError:
        print("No save game found.")
        return None, None


