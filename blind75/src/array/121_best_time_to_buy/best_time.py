# time complexity is O(n) as each element is visited only once
# space complexity is O(1)


def maxProfit(prices):
    # initialize a max price var
    # iterate through all prices and check if the max sum is higher
    max_profit = 0
    min_price = float("inf")
    for price in prices:
        if price < min_price:
            min_price = price

        if price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit
