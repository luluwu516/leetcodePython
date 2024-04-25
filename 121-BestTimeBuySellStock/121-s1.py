from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell

        return profit


def main():
    # declaration
    s = Solution()

    # input
    prices = input("Enter the prices (separated by comma): ").split(",")
    prices = [int(n) for n in prices]

    # processing
    res = s.maxProfit(prices)

    # output
    print("\nResult:")
    print("The maximum profit is:", res)


if __name__ == "__main__":
    main()
