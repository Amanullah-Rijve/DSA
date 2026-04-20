def coin_change(coins, amount):
    # create DP array
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed for amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


# Example
coins = [1, 2, 5]
amount = 11

print("Minimum coins:", coin_change(coins, amount))