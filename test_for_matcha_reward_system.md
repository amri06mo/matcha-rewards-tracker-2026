# Test Plan: Matcha Reward Tracker
America I Morfin (amri06mo)

This file gives instructions for the testing procedure, making sure that the Matcha Reward Tracker is completely functional.

## Pre-test set up
1. ensure that 'main.py' is in your directory.
2. If an 'inventory.csv' already exists, delete it to start with a fresh database. 
3. Run the program using 'uv run main.py'

## Test Scenario 1: Successfull high-value sale 🌟
The goal here is to confirm that the math, the reward conversion, and tier system will all work for a profitable item.

1. **ACTION:** Select option '1' (Add an item) from the menu
2. **INPUT:** - Item name: 'Vintage Crewneck'
    - Buy Price: '10.00'
    - Sell Price: '100.00'
3. **EXPECTED LOGIC CALCULATION:**
    - Platform fee: $100 \times 0.10 = 10$
    - Net Profit: $100 - 10 - 10 = 80$
    - Matcha Units (9$ each): $80 / 9 = 8$ Lattes (rounded down)
4. **EXPECTED OUTPUT:** The screen should display a net profit of **80.00$**, a reward of **8 Matcha Lattes**, and the **"Ceremonial Matcha Latte"** tier.

---

## Test Scenario 2: The "break even" or loss 💔
The goal of this test is to ensure the system handles low-profit or negative-profit scenarios gracefully.

1. **ACTION:** Select option '1' (Add an item) from the menu
2. **INPUT:**
    - Item name: 'Fast fashion tee'
    - Buy price: '8.00'
    - Sell price: '10.00'
3. **EXPECTED LOGIC CALCULATION:**
    - Profit: $(10 \ times 0.9) - 8 = 1.00$
4. **EXPECTED OUTPUT:** The screen should display a profit of **$1.00**, but the reward message should state: **"Not enough for a matcha yet. Keep grinding!"** and assign the **"Matcha made at home."** tier.

---

## Test Scenario 3: Data Persistence (The "big project" check)
The goal here is to prove the data is actually saved to teh CSV

1. **ACTION:** Select option '3' to exit the program
2. **ACTION:** Open the folder on your computer and locate 'inventory.csv'.
3. **EXPECTED RESULT:** The file should contain two rows of data corresponding to the "Vintage crewneck" and the "Fast fashion tee" with all calculated fields present.
4. **ACTION:** Restart the program and select option '2' (View total matchas earned).
5. **EXPECTED RESULT:** The program should read the csv and display a total lifetime profit of **$81.00** and **9 total lattes** earned.