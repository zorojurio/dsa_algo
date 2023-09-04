from typing import List

def coin_change(amount, coins: List):
    coins.sort()
    coin_counter = 0
    index = len(coins) - 1
    while True:
        coin_value = coins[index]
        if amount >= coin_value:
            print(coin_value)
            amount = amount - coin_value
            coin_counter += 1
        if amount < coin_value:
            index -= 1

        if amount == 0:
            break
    print(coin_counter)


coins = [1,2,5,20,50,100]
coin_change(201, coins)