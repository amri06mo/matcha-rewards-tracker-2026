"""
BCOG 200: Unit Test Logic Plan
Project: Matcha Reward Tracker
America I. Morfin (amri06mo)
"""

# Importing functions from main.py
from main import calculate_net_profit, calculate_matcha_units, assign_reward_tier

def run_tests():
    print("---🍵Matcha Reward Tracker: Unit Test Plan 🍵 ---")

    # TEST SCENARIO 1: High-Value Sale
    # Input: Buy $10, Sell $100
    # Fees: (100 * 0.10) + 1.00 = $11.00
    # Profit: 100 - 11 - 10 $79.00
    profit1 = calculate_net_profit(10.0, 100.0)
    assert profit1 == 79.0, f"❌ Scenario 1 Failed: Expected 79.0, got {profit1}"
    print("✅ Logic Check: Scenario 1 Profit ($79.00) verified.")

    # Input: $79.00 Profit / $9.00 Matcha -> Expected Units: 8
    units1 = calculate_matcha_units(79.0)
    assert units1 == 8, f"❌ Scenario 1 Units Failed: Expected 8, got {units1}"
    print("✅ Logic Check: Scenario 1 Matcha Units (8) verified.")

    # TEST SCENARIO 2: Break Even / Low Profit
    # Input: Buy $8, Sell $10
    # Fee: (10 * 0.10) + 1.00 = $2.00
    # Profit: 10 - 2 - 8 = 0.00
    profit2 = calculate_net_profit(8.0, 10.00)
    assert profit2 == 0.0, f"❌ Scenario 2 Failed: Expected 0.0, got {profit2}"
    print("✅ Logic Check: Scenario 2 Profit ($1.00) verified.")

    # Input: $0.00 Profit -> Expected Tier: "Matcha made at home."
    tier2 = assign_reward_tier(0.0)
    assert "Matcha made at home" in tier2, f"❌ Tier Failed: Got {tier2}"
    print("✅ Logic Check: Scenario 2 Tier assignment verified.")

    print("\n[Status]: All technical asserts are aligned with Narrative Scenarios.")

if __name__ == "__main__":
    run_tests()