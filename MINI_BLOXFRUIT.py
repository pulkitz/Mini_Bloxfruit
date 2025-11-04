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

# Fruit rarity and power level
fruits = {
    None: 0,  # no fruit user
    "Chop-Chop Fruit": 1,
    "Flame-Flame Fruit": 2,
    "Ice-Ice Fruit": 2,
    "Dark-Dark Fruit": 3,
    "Quake-Quake Fruit": 4,
    "Lightning Fruit": 4
}

# Melee weapon strength
weapons = {
    "Wooden Bat": 1,
    "Cutlass": 2,
    "Dagger": 2,
    "Dual Katana": 3,
    "Dark Saber": 4,
    "Titan Blade": 5
}

# Base reward tiers (these will get multiplied)
base_rewards = [50, 100, 200, 400, 800, 1500, 2500]

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
                        print(f"{item}: {qty}")

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
                        
                else :
                        print("invalid ")
                #---------------------------------------------------------------------------------------------
        else:
                print("wait for 5 seconds")
                time.sleep(3)

