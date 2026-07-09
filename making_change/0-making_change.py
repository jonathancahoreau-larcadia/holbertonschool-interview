#!/usr/bin/python3
"""Making change module."""


def makeChange(coins, total):
    """Return the fewest number of coins needed to reach total."""
    if total <= 0:
        return 0

    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    coins = sorted(coins)

    for amount in range(1, total + 1):
        for coin in coins:
            if coin > amount:
                break

            candidate = dp[amount - coin] + 1

            if candidate < dp[amount]:
                dp[amount] = candidate

    if dp[total] == float("inf"):
        return -1

    return dp[total]
