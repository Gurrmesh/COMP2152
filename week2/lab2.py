import random
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
diceOptions = [1,2,3,4,5,6]

input("Roll the dice: ")
weaponRoll = random.choice(diceOptions)
print("You rolled the nmber: " + str(weaponRoll))
try:
    weaponRoll = random.randint(1, 6)
    hero_weapon = weapons[weaponRoll - 1] 
    print(f"Hero's weapon: {hero_weapon}")
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")
    if hero_weapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")
except ValueError:
    print("Error: Invalid input, please enter a valid integer.")
except IndexError:
    print("Error: Weapon roll out of valid range.")
