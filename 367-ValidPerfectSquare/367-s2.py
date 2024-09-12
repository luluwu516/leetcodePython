import math


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range((num // 2) + 2):
            if i * i == num:
                return True
            elif i * i > num:
                return False
        return False


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
