# Matcha Rewards Tracker (BCOG 200 Final Project)

🤔 What is it?: 

This Project will be a functional inventory and profit-tracking system for the resale market. The system allows users to log thrifted items, calculate net profits (accounting for platform selling fees and initial costs), and then translate that financial data into a "Matcha reward" system. By converting currency into a personal "Matcha" metric and assigning reward tiers based on profit levels, the tool turns inventory management into a fun lifestyle oriented experience🍵!


🙃 Functions:

a. calculate_net_profit(buy_price, sell_price) : This function will take the item's purchase price and sale prices as inputs to calculate the actual earnings. It will automatically subract a 10% platform fee from the original cost to ensure user knows exactly how much "real" money was made before any spending.

b. calculate_matcha_units(profit, matcha_cost) : This function will convert the net profit made into "matcha currency" by dividing the profit by the cost of one latte (e.g., $9.00). It returns a rounded numerical number representing the total number of drinks earned, or a specific message if the profit is too low to afford a drink.

c. assign_reward_tier(profit) : this function will use conditional logic to assign a specific status based on the profit amount. It'll categorize the flip into tiers ranging from "matcha made at home" for smaller profits to "Ceremonial matcha latte" for high value sales to provide the user with immediate feedback.

Data Structure: The inventory.csv file uses the following order: Item Name, Buy Price, Sell Price, Net profit, Reward Tier.