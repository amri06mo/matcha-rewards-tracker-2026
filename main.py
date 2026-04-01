"""
Bcog 200 Final project : Matcha Reward Tracker
America I. Morfin
"""

import math
import csv

# Function Outlines

def calculate_net_profit(buy_price, sell_price):
    """
    - amri06mo
    Takes two floats, subtracts 10% off the sell_price, then returns the net profit.
    """
    pass

def calculate_matcha_units(profit, matcha_cost):
    """
    - amri06mo
    Divides the profit by the cost, then returns integer of matcha drinks earned.
    """
    pass

def assign_reward_tier(profit):
    """
    - amri06mo
    Uses elif/if logic to return a string representing a Matcha Tier.
    """
    pass

# System Methods

def save_to_inventory(item_name, buy, sell, profit, tier):
    """
    - amri06mo
    Opens 'inventory.csv' and appends a new row with the new item data.
    """
    pass

def display_menu():
    """
    -amri06mo
    Asks the user if they want to:
    1) Add an item
    2) View total matcha's earned
    3) Exit
    """
    pass

if __name__ == "__main__":
    # Starts program
    display_menu()