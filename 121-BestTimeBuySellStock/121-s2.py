from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        maxProfit = prices[1] - prices[0]
        for i in range(len(prices) - 1):
            for j in range(i, len(prices)):
                profit = prices[j] - prices[i]
                if profit > maxProfit:
                    maxProfit = profit

        if maxProfit < 0:
            return 0

        return maxProfit


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
