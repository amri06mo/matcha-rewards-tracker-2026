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
    - Platform fee: $100 \times 0.10 + 10 = 11$
    - Net Profit: $100 - 10 - 11 = 79$
    - Matcha Units (9$ each): $79 / 9 = 8$ Lattes (rounded down)
4. **EXPECTED OUTPUT:** The screen should display a net profit of **79.00$**, a reward of **8 Matcha Lattes**, and the **"Ceremonial Matcha Latte"** tier.

---

## Test Scenario 2: The "break even" or loss 💔
The goal of this test is to ensure the system handles low-profit or negative-profit scenarios gracefully.

1. **ACTION:** Select option '1' (Add an item) from the menu
2. **INPUT:**
    - Item name: 'Fast fashion tee'
    - Buy price: '8.00'
    - Sell price: '10.00'
3. **EXPECTED LOGIC CALCULATION:**
    - Profit: $(10 \ times 0.9) - 8 - 2.00 = 0.00$
4. **EXPECTED OUTPUT:** The screen should display a profit of **$0.00**, but the reward message should state: **"Not enough for a matcha yet. Keep grinding!"** and assign the **"Matcha made at home."** tier.

---

## Test Scenario 3: Data Persistence & History 🧾
The goal here is to prove the data is actually saved to the CSV and retrieved correctly.

1. **ACTION:** Select option `3` to view the recent history.
2. **EXPECTED RESULT:** Console displays "Vintage Crewneck" and "Fast fashion tee" with their profits.
3. **ACTION:** Select option `5` to exit, then restart by using `uv run main.py`.
4. **ACTION:** Select option `2` to view total matchas earned.
5. **EXPECTED RESULT:** The program will display the lifetime profit and the total matchas earned proving data persisted even after being closed out. 

---

## Test Scenario 4: Anti - Crash safety check 🛡️
The goal for this test is to ensure the program handles typos and symbols without crashing.

1. **ACTION**: Select option `1` to add a new item into the inventory.
2. **INPUT**: It'll ask for the buy price, add `$15.00` WITH THE DOLLAR SIGN.
3. **INPUT**: It'll also ask for the seling price, say `twenty` AS A WORD
4. **EXCPECTED RESULT**: It should strip the dollar sign and accept it as `15.00`, for `twenty` it should display `❌ Invalid Input!!` and prompt again. 
5. **EXPECTED RESULT**: The program should run and not crash.

---

## Test Scenario 5: Data Visualization
The goal is to verify the Matplotlib library renders the data visually.

1. **ACTION**: Select option `4` to view the profit graph
2. **EXPECTED RESULT**: A pop-up window will appear with a bar chart.
3. **ACTION**: Close the window and return to the main menu.