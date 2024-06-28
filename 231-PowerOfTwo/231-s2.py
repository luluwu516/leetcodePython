class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n != 1:
            if n % 2:
                return False
            n /= 2

        return True


def main():
    # declaration
    s = Solution()

    # input
    num = int(input("Enter a number: "))

    # processing
    res = s.isPowerOfTwo(num)

    # output
    print("\nResult:")
    print(f"The number is {'a' if res else 'not a'} power of two")


if __name__ == "__main__":
    main()
