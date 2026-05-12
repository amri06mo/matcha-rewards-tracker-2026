"""
Bcog 200 Final project : Matcha Reward Tracker
America I. Morfin
"""

import math
import csv
import matplotlib.pyplot as plt # New addition!

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
    print("3) View recent history")
    print("4) View Profit Graph 📈") # New!
    print("5) Exit")

    choice = input("Select an option:")

    if choice == '1':
        item = input("Item name: ")
        buy = get_valid_float("Buy Price ($): ")
        sell = get_valid_float("Sell Price ($): ")

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
        view_recent_flips()
        display_menu()

    elif choice == '4':
        show_profit_graph()
        display_menu()

    elif choice == '5':
        print("Goodbye! LOCK IN!...make that money! 🍵")

    else:
        print("Invalid choice. Please pick 1, 2, 3, or 4.")
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

def get_valid_float(prompt): 
    """Prevents the program from crashing if the user types a letter or $ sign."""
    while True:
        try:
            # 1. We get the input, remove $ signs, and strip extra spaces
            raw_input = input(prompt).replace('$', '').strip()
            
            # 2. We turn it into a decimal number (float)
            value = float(raw_input) 
            
            # 3. NOW we can return it
            return value
        except ValueError:
            print("❌ Invalid Input!! Please enter a number (e.g., 11.50).")

def view_recent_flips():
    """Reads the CSV file and shows only the last 5 entries."""
    try:
        with open('inventory.csv', mode='r') as file:
            rows = list(csv.reader(file))
            if len(rows) <= 1: #only header exists
                print("\n 📭 No flips recorded yet!")
                return
            print("\n⏰ Recent History")
            #Shows the last 5 items
            for row in rows[-5:]:
                if row != "Item name": #Skip the header if it's in the last 5
                    print(f"✅ {row}: +${row}")
    except FileNotFoundError:
        print("\n📭 No inventory file found.")

def show_profit_graph():
    names = []
    profits = []
    try:
        with open('inventory.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if row:
                    names.append(row[0])
                    profits.append(float(row[3]))
        
        # Style Settings because we want it to be cute...lol
        plt.figure(figsize=(10, 6))
        
        # Changes 'teal' (original color) to 'hotpink' or 'lightpink'
        plt.bar(names, profits, color='hotpink', edgecolor='deeppink', linewidth=2)
        
        plt.xlabel('Items', fontweight='bold', color='darkmagenta')
        plt.ylabel('Profit ($)', fontweight='bold', color='darkmagenta')
        plt.title('✨ My Thrift Flip Journey ✨', fontsize=14, color='deeppink')
        
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.3) # Adds a soft grid
        plt.tight_layout()
        
        print("\n🌸 Opening your pink profit graph...")
        plt.show()

    except FileNotFoundError:
        print("\n🙅‍♀️ No data found to graph yet.")

if __name__ == "__main__":
    # Starts the program
    display_menu()