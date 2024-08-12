class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False

        return self.isPowerOfThree(n / 3)


def main():
    # declaration
    s = Solution()

    # input
    num = int(input("Enter a number: "))

    # processing
    res = s.isPowerOfThree(num)

    # output
    print("\nResult:")
    print(f"The number is {'a' if res else 'not a'} power of three")


if __name__ == "__main__":
    main()
