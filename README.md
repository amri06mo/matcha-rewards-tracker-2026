# Matcha Rewards Tracker (BCOG 200 Final Project)

### 🤔 What is it?: 

The **Matcha Rewards Tracker** is a functional inventory and profit-tracking system designed for the resale market. The system allows users to log thrifted items, calculate net profits (accounting for platform selling fees and initial costs), and then translate that financial data into a "Matcha reward" system. 

By converting currency into a personal "Matcha" metric and assigning reward tiers, this tool turns boring inventory management into a fun, lifestyle oriented experience 🍵💗!

### 🙃 Functions:

* **`calculate_net_profit(buy, sell)`**: Calculates earnings after the 10% platform and a $1.00 flat fee.
* **`calculate_matcha_units(profit)`**: Converts net profit into "matcha currency" based on a $9.00 latte cost.
* **`assign_reward_tier(profit)`**: Uses conditional logic to categorize the flips into "Home made" vs. "Ceremonial" tiers.
* **`show_profit_graph()`**: **[NEW]** Uses `matplotlib` to generate a customized pink bar chart of all flips.
* **`view_recent_flips()`**: **[NEW]** Retrieves and displays the 5 most recent entries from the database.
* **`get_valid_float()`**: **[NEW]** An input safety funtion that prevents the program from crashing if the user enters symbols like `$` or letters.

---

### Data & Storage

* **`inventory.csv`**: This serves as the permanent data base, it stores:
    `Item name | Buy Price | Sell Price | Net Profit | Reward Tier`
* **Persistence**: Data is saved instantly and remains available after the program is closed. 

---

### How to run
1. Ensure you have `uv` installed.
2. Install dependencies:
    `uv add matplotlib`
3. Launch the tracker:
    `uv run main.py`