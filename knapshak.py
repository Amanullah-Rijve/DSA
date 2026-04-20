def knapsack(weights, values, capacity):
    n = len(weights)

    # create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # build table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],  # take item
                    dp[i-1][w]  # don't take
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]


# Example
weights = [1, 3, 4, 5]
values = [10, 40, 50, 70]
capacity = 7

print("Maximum value:", knapsack(weights, values, capacity))