from belajar_modul import hero, item, enemy, area, rank

def main():
    player = hero.Hero("Player", 100)
    sword = item.Item("Sword", "A sharp sword")
    enemy1 = enemy.Enemy("Dragon", 50)
    forest = area.Area("Forest")
    beginner = rank.Rank("Beginner", 1)

    player.attack(enemy1.name)
    player.use_item(sword.name)
    sword.use(player.name)
    enemy1.attack(player.name)
    forest.explore()
    print(f"Player is at {beginner.name} level {beginner.level}")

if __name__ == "__main__":
    main()