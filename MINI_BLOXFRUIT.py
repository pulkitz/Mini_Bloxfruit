# Write code below 💖
import random
import time
dig_list = [
    ("1 belly", 0.15),
    ("10 belly", 0.10),
    ("100 belly", 0.10),
    ("Wooden_Sword", 0.08),
    ("Spirit_fruit", 0.07),
    ("Shadow_fruit", 0.06),
    ("Phoenix_fruit", 0.04), #Rare Item
    ("Dragon_fruit", 0.02), #Mythical Item
    ("Ancient_Relic", 0.01) #Legendary Item
]

names = ["Bandit", "Marine", "Thug", "Hunter", "Raider", "Warlord", "Admiral", "Assassin"]
titles = ["of the East", "the Ruthless", "from North Blue", "the Silent", "the Unseen", "of Darkness", "the Mighty"]

fruit_power = {
    "None": 0,
    "Bomb_Fruit": 1,
    "Flame_Fruit": 2,
    "Light_Fruit": 3,
    "Dark_Fruit": 4,
    "Spirit_Fruit": 5
}

weapon_power = {
    "Wooden_Sword": 1,
    "Iron_Sword": 2,
    "Katana": 3,
    "Dark_Blade": 5
}

# Base reward tiers (these will get multiplied)
base_rewards = [50, 100, 200, 400, 800, 1500, 2500]

def generate_enemy(level):
        name = random.choice(names) + " " + random.choice(titles)
        fruit = random.choice(list(fruit_power.keys()))
        weapon = random.choice(list(weapon_power.keys()))
        base_level = fruit_power[fruit] + weapon_power[weapon]
        variation = random.choice([-1, 2, 0, -2, 1]) 
        enemy_level = (base_level + level) //2 + variation
        if enemy_level < 1:
                enemy_level = 1

        return {
                "name": name,
                "fruit": fruit,
                "weapon": weapon,
                "level": enemy_level
        }

def win_prob(level, enemy_level):
        level_diff = level -enemy_level

        prob = 50 + (level_diff * 10)
        return max(10, min(90, prob))

def dig():
        global level 
        #level up system------------------------------------------------------------
        if level %1 == 0:
                print(f"LEVEL UP!! you are now level {int(level)}")
        else:
                pass
        #---------------------------------------------------------------------------
        items, prob = zip(*dig_list)
        return random.choices(items, prob)[0]

inv = {}
level = 0
last_used = 0
while True:
        print("*******************WELCOME*******************")
        print("*************TO MINI BLOXFRUIT*******************")
        print("")
        print("What do you want to do?? choose only the number:")
        print("1. DIG")
        print("2. KILL")
        print("3. TRADE")
        print("4.Show Inventory")



        inp1 = int(input("Enter only the number:   "))
        now = time.time()
        cool = 5

#NON-COOL DOWN TASKS
        if inp1 == 4 :
                for item, qty in inv.items():
                        print("-----INVENTORY-----")
                        print("")
                        print(f"{item}: {qty}")
                        print("")
                        print("-------------------")
                        time.sleep(4)

                continue 

#COOL DOWN TASKS
        if now - last_used >= cool : 
                #DIG TASK------------------------------------------------------------------------------
                if inp1 == 1 :
                        D =  dig()
                        print("diging")
                        time.sleep(0.5)
                        print(".")
                        time.sleep(0.5)
                        print("..")
                        time.sleep(0.5)
                        print("...")
                        time.sleep(0.5)
                        print("....")
                        level += 0.5 #for level increase
                        if D == "Ancient_Relic":
                                print("CONGRATS YOU FOUND A LEGENDARY ITEM!!!")
                                print("you got " + D)

                        elif D == "Dragon_fruit":
                                print("WOW YOU FOUND A MYTHICAL ITEM!!!")
                                print("you got " + D)

                        elif D == "Phoenix_fruit":
                                print("NICE YOU FOUND A RARE ITEM!!!")
                                print("you got " + D)

                        else:
                          print("you got " + D)

                     
                        
                        if "belly" in D:#for belly addition---------------------------------------------------------------------------------
                                amount = int(D.split()[0])
                                if "belly" in inv:
                                                inv["belly"] += amount
                                else:
                                                inv["belly"] = amount
                        else:
                                if D in inv:  
                                                inv[D] += 1
                                else:                     
                                                inv[D] = 1
                        #---------------------------------------------------------------------------------------------

                        last_used = now
                        time.sleep(3)
                #---------------------------------------------------------------------------------------------
                if inp1 == 2:
                        enemy = generate_enemy(level)
                        print(f"A wild {enemy['name']} appeared! (Level {enemy['level']}, Fruit: {enemy['fruit']}, Weapon: {enemy['weapon']})")
                        win_probability = win_prob(level, enemy['level'])
                        print(f"Your chance to win is {win_probability}%")
                        cond = input("Do you want to fight? (y/n): ")
                        if cond.lower() == 'y':
                                print("Fighting...")
                                time.sleep(0.25)
                                print(".")
                                time.sleep(0.25)
                                print("..")
                                time.sleep(0.25)
                                print("...")
                                time.sleep(0.25)
                                print("....")
                                if random.randint(1,100) <= win_probability:
                                        print("you won the battle!")
                                else :
                                        print("you lost the battle!")
                                        last_used = now 

                        else:
                                print("you Ran Away!, come back when you are ready!")
                                last_used = now

                if inp1 == 3:
                        print("Trading feature coming soon!")
                        last_used = now

        else:
                print("wait for 5 seconds")
                time.sleep(3)

