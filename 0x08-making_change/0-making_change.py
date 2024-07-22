#!/usr/bin/python3
""" this file contains a script that determine
the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """ the function that will determine the fewest
    number of coins needed to meet a given amount total"""
    if total <= 0:
        return 0

    # Initialize the dp array with a value larger than any
    # possible number of coins needed.
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over each coin
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means we cannot make
    # the amount with the given coins.
    return dp[total] if dp[total] != float('inf') else -1
