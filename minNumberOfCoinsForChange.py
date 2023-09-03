def minNumberOfCoinsForChange(n, denoms):
    num_coins = [float("inf") for _ in range(n + 1)]
    num_coins[0] = 0
    for d in denoms:
        for amount in range(d, n + 1):
            num_coins[amount] = min(num_coins[amount], num_coins[amount - d] + 1)

    return num_coins[-1] if num_coins[-1] != float("inf") else -1
