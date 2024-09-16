class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 0
        high = num
        while low <= high:
            mid = low + (high - low) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                low = mid + 1
            else:
                high = mid - 1

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
