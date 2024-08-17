class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 4 == 0:
            n /= 4

        return n == 1


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
