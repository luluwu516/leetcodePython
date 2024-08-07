class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


def main():
    # declaration and input
    s = Solution()
    num = int(input("\nEnter the number of stones in the heap: "))

    # processing
    res = s.canWinNim(num)

    # output
    print("\nResult:")
    print(f"You can{'' if res else ' not'} win the game.\n")


if __name__ == "__main__":
    main()
