class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1


def main():
    # declaration
    s = Solution()

    # input
    num = int(input("Enter a number: "))

    # processing
    res = s.isPowerOfFour(num)

    # output
    print("\nResult:")
    print(f"The number is {'a' if res else 'not a'} power of four")


if __name__ == "__main__":
    main()
