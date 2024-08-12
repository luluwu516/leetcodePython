class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n != 1:
            if n % 3:
                return False
            n /= 3

        return True


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
