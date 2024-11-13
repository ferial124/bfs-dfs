def coin_change(coins, amount):
    coins.sort(reverse=True)
    coin_count = 0

    for coin in coins:
        if amount == 0:
            break

        coin_count += amount // coin
        amount %= coin

    if amount != 0:
        return -1

    return coin_count


coins = [1, 5, 10, 25]
amount = 63
print(f"Minimum coins needed: {coin_change(coins, amount)}")
