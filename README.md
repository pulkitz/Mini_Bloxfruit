# 🏝️ Mini Bloxfruit — A Python Loot Game

Welcome to **Mini Bloxfruit**, a small but addictive terminal-based loot game inspired by the Blox Fruits universe 🍇  
Dig, grind, and collect rare fruits, relics, and belly — if luck is on your side 👀

---

## 🎮 Gameplay

Run the script, and you’ll be greeted with your menu:

WELCOME
TO MINI BLOXFRUIT*

DIG

KILL

TRADE

Show Inventory

yaml
Copy code

### ⚒️ DIG
- Try your luck and dig for treasure.  
- You might find **belly**, **fruits**, **weapons**, or even **legendary relics**!  
- There’s a **5-second cooldown** between digs to keep things fair.

### 💰 BELLY
- Any item ending in “belly” adds to your total belly count.
- Example:  
  `"10 belly"`, `"150 belly"`, `"1000 belly"` → combine into one balance!

### 📦 Inventory
Check what you’ve collected anytime by choosing option `4`.

---

## 💎 Rarity System
Each item has its own drop probability:

| Rarity       | Example Item      | Drop Chance |
|---------------|------------------|--------------|
| Common        | 1 belly, Wooden_Sword | 25%–10% |
| Uncommon      | Spirit_fruit, Shadow_fruit | 7%–5% |
| Rare          | Phoenix_fruit     | 3% |
| Legendary     | Dragon_fruit, Ancient_Relic | 1% or less 😱 |

---

## ⚙️ Features
- 🌀 Weighted RNG drop system using `random.choices()`
- 🕓 Cooldown between actions
- 💰 Stacked belly system
- 🎯 Dynamic rarity reactions (common/rare/legendary)
- 🧾 Inventory tracking

---

## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/Mini-Bloxfruit.git
cd Mini-Bloxfruit
2. Run the game
bash
Copy code
python bloxfruit.py
```
---

### 🧠 Future Ideas
Add combat mechanics for “KILL” option ⚔️

Trading system between items 💱

Save inventory data to a file 💾

Color-coded rarity messages (gold = legendary!) 🌈

---

### 🧑‍💻 Author
Pulkit — a student, dev, and the proud creator of Mini Bloxfruit.
If you like this, star ⭐ the repo and flex your luck 🍀
