import time
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
    
    return result

# Приклад використання:
amount = 113
print(find_coins_greedy(amount))  # {50: 2, 10: 1, 2: 1, 1: 1}


def find_min_coins(amount):
    # List of coin denominations sorted in ascending order
    coins = [1, 2, 5, 10, 25, 50]
    # dp[i] will hold the minimum number of coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: no coins needed to make amount 0
    # coin_used[i] will track which coin was last used to achieve the minimum for amount i
    coin_used = [0] * (amount + 1)

    # Fill the dp array
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    # Backtrack to find the coin combination
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Тестування для різних значень суми
test_amounts = [113, 1234, 5895, 10123]

for amount in test_amounts:
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time
    
    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time
    
    print(f"Сума: {amount}")
    print(f"Жадібний алгоритм: {greedy_result}, Час виконання: {greedy_time:.6f} секунд")
    print(f"Динамічне програмування: {dp_result}, Час виконання: {dp_time:.6f} секунд")
    print()