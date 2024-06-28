class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 == 1:
            return False

        return self.isPowerOfTwo(n / 2)


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
