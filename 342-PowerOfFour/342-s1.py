class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 4 != 0:
            return False

        return self.isPowerOfFour(n / 4)


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
