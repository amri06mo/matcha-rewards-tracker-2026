"""
Bcog 200 Final project : Matcha Reward Tracker
America I. Morfin
"""

import math
import csv

# Function Outlines

def calculate_net_profit(buy_price, sell_price):
    """Calculates profit after a 10% platform fee."""
    fee = sell_price * 0.10
    profit = sell_price - fee - buy_price
    return round(profit, 2)

def calculate_matcha_units(profit):
    """Returns number of $9 lattes earned. Returns 0 if profit is less than $9."""
    matcha_cost = 9.00
    if profit >= matcha_cost:
        return int(profit // matcha_cost)
    return 0

def assign_reward_tier(profit):
    """Categorizes the 'vibe' of the flip based on the profit."""
    if profit >= 50:
        return "Ceremonial Matcha Latte 🌟🍵"
    elif profit >= 9:
        return "Cafe Matcha latte 🧘‍♀️🍵"
    else:
        return "Matcha made at home 🫩🏡"

# System Methods

def save_to_inventory(item_name, buy, sell, profit, tier):
    """Opens 'inventory.csv and appens a new row with the new item data."""
    row_to_add = [item_name, buy, sell, profit, tier]

    with open('inventory.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row_to_add)

def display_menu():
    print("\n--- 🍵 Matcha Reward Tracker Demo ---")
    print("1) Add new thrift flip")
    print("2) View total matchas earned")
    print("3) Exit")

    choice = input("Select an option:")

    if choice == '1':
        item = input("Item name: ")
        buy = float(input("Buy Price ($): "))
        sell = float(input("Sell Price ($): "))

        profit = calculate_net_profit(buy, sell)
        drinks = calculate_matcha_units(profit)
        tier = assign_reward_tier(profit)

        print("-" * 30)
        print(f"✅ Item: {item}")
        print(f"💵 Net Profit: ${profit: .2f}")
        print(f"🍵 Rewards Earned: {drinks} Matchas")
        print(f"🏆 Status: {tier}")
        print("-" * 30)

        save_to_inventory(item, buy, sell, profit, tier)
        display_menu()

    elif choice == '2':
        calculate_lifetime_stats()
        display_menu()
    
    elif choice == '3':
        print("Goodbye! LOCK IN!...make that money!🍵")

    else:
        print("Invalid choice. Please pick 1, 2, or 3.")
        display_menu()

def calculate_lifetime_stats():
    """Reads the inventory.csv file and calculates total profit and total lattes."""
    total_profit = 0.0
    try:
        with open('inventory.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if row:
                    total_profit += float(row[3])
        
        total_lattes = calculate_matcha_units(total_profit)

        print("\n--- Your lifetime Stats ---")
        print(f"💵 Total Lifetime Profit: ${total_profit:.2f}")
        print(f"🍵 Total Matchas Earned: {total_lattes}")
        print("-------------------------------")

    except FileNotFoundError:
        print("\n🙅‍♀️ No inventory found. Start Flipping to see stats!")

if __name__ == "__main__":
    # Starts program
    display_menu()