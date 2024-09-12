import math


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = math.sqrt(num)
        # return n - int(n) == 0
        return n % 1 == 0

        # return int(num ** 0.5) * int(num ** 0.5) == num


def main():
    # declaration and input
    s = Solution()
    num = int(input("Enter an integer: "))

    # processing
    res = s.isPerfectSquare(num)

    # output
    print("\nResult:")
    print(f"{num} is{'' if res else ' not'} perfect square\n")


if __name__ == "__main__":
    main()
